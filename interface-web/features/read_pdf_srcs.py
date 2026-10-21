import json
from pathlib import Path

from weasyprint import HTML

BASE_DIR = Path(__file__).resolve().parent.parent
DESCRIPTION_FILE = (
    BASE_DIR / "auxiliares" / "code_description_remediation.json"
)


def read_descriptions_json():
    with open(DESCRIPTION_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def prepare_report_data(scan_json):
    # Aceita o JSON retornado pelo ptnetinspector como texto
    # ou como um dicionário já convertido pelo json.loads().
    if isinstance(scan_json, str):
        scan_data = json.loads(scan_json)
    else:
        scan_data = scan_json

    description_dict = read_descriptions_json()

    results = scan_data.get("results", {})
    nodes = results.get("nodes", [])

    devices = [
        dict(node, properties=dict(node.get("properties", {})))
        for node in nodes
        if node.get("type") == "Device"
    ]

    addresses = [
        node for node in nodes
        if node.get("type") == "Address"
    ]

    devices_by_key = {
        device.get("key"): device for device in devices
    }

    for device in devices:
        device["addresses"] = []

    for address in addresses:
        parent = devices_by_key.get(address.get("parent"))
        if parent:
            parent["addresses"].append(address)

    vulnerabilities = {}

    # Vulnerabilidades associadas a dispositivos e endereços.
    for node in nodes:
        properties = node.get("properties", {})

        if node.get("type") == "Address":
            parent = devices_by_key.get(node.get("parent"), {})
            parent_name = parent.get("properties", {}).get(
                "name", "Dispositivo desconhecido"
            )
            ip = properties.get("IP", "IP desconhecido")
            asset_name = f"{parent_name} ({ip})"
        else:
            asset_name = properties.get(
                "name", "Dispositivo desconhecido"
            )

        for item in node.get("vulnerabilities", []):
            code = item.get("vulnCode")
            if not code:
                continue

            if code not in vulnerabilities:
                details = description_dict.get(code, {})
                vulnerabilities[code] = {
                    "code": code,
                    "descricao": details.get(
                        "descricao", "Descrição não disponível."
                    ),
                    "correcao": details.get(
                        "correcao", "Correção não disponível."
                    ),
                    "assets": []
                }

            vulnerabilities[code]["assets"].append(asset_name)

    # Vulnerabilidades no nível da rede.
    for item in results.get("vulnerabilities", []):
        code = item.get("vulnCode")
        if not code:
            continue

        if code not in vulnerabilities:
            details = description_dict.get(code, {})
            vulnerabilities[code] = {
                "code": code,
                "descricao": details.get(
                    "descricao", "Descrição não disponível."
                ),
                "correcao": details.get(
                    "correcao", "Correção não disponível."
                ),
                "assets": ["Rede"]
            }
        elif "Rede" not in vulnerabilities[code]["assets"]:
            vulnerabilities[code]["assets"].append("Rede")

    for vulnerability in vulnerabilities.values():
        vulnerability["assets"] = sorted(
            set(vulnerability["assets"])
        )

    return {
        "command": scan_data.get("command", "-"),
        "status": scan_data.get("status", "-"),
        "message": scan_data.get("message", ""),
        "network_properties": results.get("properties", {}),
        "devices": devices,
        "addresses": addresses,
        "vulnerabilities": sorted(
            vulnerabilities.values(),
            key=lambda item: item["code"]
        )
    }


def generate_pdf(html_content):
    return HTML(
        string=html_content,
        base_url=str(BASE_DIR)
    ).write_pdf()
