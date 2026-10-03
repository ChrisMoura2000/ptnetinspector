from flask import Flask, render_template, request, jsonify
import subprocess
import json
import time
from features.list_interfaces import list_network_interfaces

app = Flask(__name__)

@app.route('/')
def hello_world():
    interfaces = list_network_interfaces()
    return render_template('index.html', interfaces=interfaces)

@app.route('/scan', methods=['post'])
def inspec_passive():
    inspect_type = request.form['inspect_type'] # Captura o tipo de scan enviado no formulario passivo/agressivo/+agressivo
    interface = request.form['interface'] # captura interface escolhida para varredura
    comand_cli = ['ptnetinspector', '-t', inspect_type, '-i', interface, '-j'] # Monta comando para rodar lib pelo terminal
    try:        
        response_cli = subprocess.run(comand_cli, capture_output=True, text=True) # Roda o comando no terminal e retorna um ???
        
        if 'Operation not permitted' in response_cli.stdout: # verifica se o app rodou com permissao de root
            return render_template('error.html', erro=response_cli.stdout)
        else:
            response_in_json = json.loads(response_cli.stdout) # Converte saida de text para json
            return render_template('resume.html', resumo=response_in_json)
    except KeyError as err: 
        print(err)
        return render_template('error.html', erro=err)

    
@app.route('/scanreal', methods=['post'])
def scan_real():
    data_request = request.get_json()
     
    comand_cli = ['ptnetinspector', '-t', data_request['inspect_type'], '-i', data_request['interface_selcted'], '-j']
    print(comand_cli)
    try:        
        response_cli = subprocess.run(comand_cli, capture_output=True, text=True)

        if 'Operation not permitted' in response_cli.stdout:
            return {'erro': response_cli.stdout}
        else:
            response_in_json = json.loads(response_cli.stdout)
            print(response_in_json)
            return response_in_json
    except KeyError as err: 
        print(err)
        return {'erro': err}


@app.route('/scan_mock')
def scan_mock():
    time.sleep(3) # adicionar se quiser loading 
    with open('mock_responses/passive.json', 'r') as data_json:
        data_mock = json.load(data_json)

    # with open('auxiliares/code_description_map.json', 'r') as code_desc:
    #     description_dict = json.load(code_desc)
    
    return data_mock 

if __name__ == '__main__':
    app.run(debug=True) 
