from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
from io import BytesIO
import subprocess
import json
import time
from features.list_interfaces import list_network_interfaces
from features.read_pdf_srcs import prepare_report_data, generate_pdf


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PTNETINSPECTOR = PROJECT_ROOT / ".venv" / "bin" / "ptnetinspector"


app = Flask(__name__)


@app.route('/')
def hello_world():
    interfaces = list_network_interfaces()
    return render_template('index.html', interfaces=interfaces)


# @app.route('/scan', methods=['post'])
# def inspec_passive():
#     inspect_type = request.form['inspect_type'] # Captura o tipo de scan enviado no formulario passivo/agressivo/+agressivo
#     interface = request.form['interface'] # captura interface escolhida para varredura
#     comand_cli = ['ptnetinspector', '-t', inspect_type, '-i', interface, '-j'] # Monta comando para rodar lib pelo terminal
#     try:
#         response_cli = subprocess.run(comand_cli, capture_output=True, text=True) # Roda o comando no terminal e retorna um ???

#         if 'Operation not permitted' in response_cli.stdout: # verifica se o app rodou com permissao de root
#             return render_template('error.html', erro=response_cli.stdout)
#         else:
#             response_in_json = json.loads(response_cli.stdout) # Converte saida de text para json
#             return render_template('resume.html', resumo=response_in_json)
#     except KeyError as err:
#         print(err)
#         return render_template('error.html', erro=err)


@app.route('/scanreal', methods=['post'])
def scan_real():
    data_request = request.get_json()

    comand_cli = [
        "sudo",
        str(PTNETINSPECTOR),
        "-t",
        data_request["inspect_type"],
        "-i",
        data_request["interface_selcted"],
        "-j",
    ]

    print("Comando executado: ", comand_cli)

    try:
        # Função agora no arquivo read_pdf_srcs.py.
        # with open('auxiliares/code_description_map.json', 'r') as code_desc:
        #     description_dict = json.load(code_desc)

        response_cli = subprocess.run(
            comand_cli,
            capture_output=True,
            text=True
        )

        if 'Operation not permitted' in response_cli.stdout:
            return jsonify({'erro': response_cli.stdout}), 400

        if response_cli.returncode != 0:
            return jsonify({
                "erro": response_cli.stderr or response_cli.stdout
            }), 500

        raw_report_data = json.loads(response_cli.stdout)
        raw_report_data.update({"command": " ".join(comand_cli)})
        arr_report_data = prepare_report_data(raw_report_data)

        # O jsonify() converte o dicionário em uma resposta HTTP no formato JSON
        response = jsonify({
            "scan_returned": raw_report_data,
            "report": arr_report_data
        })
        return response

    except (KeyError, json.JSONDecodeError, OSError) as err:
        print(err)
        return jsonify({"erro": str(err)}), 500


# Ainda precisa de mock?
# @app.route('/scan_mock', methods=['post'])
# def scan_mock():
#     time.sleep(1)  # adicionar se quiser loading
    
#     with open("mock_responses/passive.json", "r") as data_json:
#         data_mock = json.load(data_json)

#     with open("auxiliares/code_description_map.json", "r") as code_desc:
#         description_dict = json.load(code_desc)

#     response = {
#         "scan_returned": data_mock,
#         "description_dict": description_dict,
#         "report": prepare_report_data(data_mock)
#     }
#     return response


@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    data = request.get_json()

    if not data or not isinstance(data, dict):
        return jsonify({"erro": "Dados do relatório inválidos."}), 400

    html_content = render_template("report.html", report=data)
    pdf_content = generate_pdf(html_content)

    return send_file(
        BytesIO(pdf_content),
        mimetype="application/pdf",
        as_attachment=True,
        download_name="relatorio_ptnetinspector.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
