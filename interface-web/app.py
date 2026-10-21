import json
import subprocess
from io import BytesIO
from pathlib import Path

from features.list_interfaces import list_network_interfaces
from features.read_pdf_srcs import generate_pdf, prepare_report_data
from flask import Flask, jsonify, render_template, request, send_file

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PTNETINSPECTOR = PROJECT_ROOT / ".venv" / "bin" / "ptnetinspector"


app = Flask(__name__)


@app.route("/")
def hello_world():
    interfaces = list_network_interfaces()
    return render_template("index.html", interfaces=interfaces)


@app.route("/scanreal", methods=["POST"])
def scan_real():
    data_request = request.get_json()

    command_cli = [
        str(PTNETINSPECTOR),
        "-t",
        data_request["inspect_type"],
        "-i",
        data_request["interface_selcted"],
        "-j",
    ]

    print("Comando executado: ", command_cli)

    try:
        response_cli = subprocess.run(
            command_cli,
            check=False,
            capture_output=True,
            text=True
        )

        if "Operation not permitted" in response_cli.stdout:
            return jsonify({"erro": response_cli.stdout}), 400

        if response_cli.returncode != 0:
            return jsonify({
                "erro": response_cli.stderr or response_cli.stdout
            }), 500

        raw_report_data = json.loads(response_cli.stdout)
        raw_report_data.update({"command": " ".join(command_cli)})
        arr_report_data = prepare_report_data(raw_report_data)

        return jsonify({
            "scan_returned": raw_report_data,
            "report": arr_report_data
        })


    except (KeyError, json.JSONDecodeError, OSError) as err:
        print(err)
        return jsonify({"erro": str(err)}), 500


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
