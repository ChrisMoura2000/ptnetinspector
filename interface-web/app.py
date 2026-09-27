from flask import Flask, render_template, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/scan', methods=['post'])
def inspec_passive():
    inspect_type = request.form['inspect_type'] # Captura o tipo de scan enviado no formulario passivo/agressivo/+agressivo
    interface = request.form['interface'] # captura interface escolhida para varredura
    comand_cli = ['ptnetinspector', '-t', inspect_type, '-i', interface, '-j'] # Monta comando para rodar lib pelo terminal
    try:        
        reponse_cli = subprocess.run(comand_cli, capture_output=True, text=True) # Roda o comando no terminal e retorna um ???

        response_in_json = json.loads(reponse_cli.stdout) # Converte saida de text para json
        print(response_in_json, "+++++++++++++")
        return render_template('resume.html', resumo=response_in_json)
    except: 
        return render_template('error.html')

@app.route('/scan_mock')
def scan_mock():
    with open('mock_responses/passive.json', 'r') as data_json:
        data_mock = json.load(data_json)
    print(data_mock)
    return render_template('resume.html', resumo=data_mock) 

if __name__ == '__main__':
    app.run(debug=True) 
