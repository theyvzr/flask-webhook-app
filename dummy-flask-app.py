from flask import Flask, request, jsonify, render_template
from configparser import ConfigParser
import requests
import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser()
config.read(f'{dir_path}/dummy-flask-app.cfg')
logging.basicConfig(filename=config['LOGGING']['log_file'], level=config['LOGGING']['log_level'])

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthchecker():
    status = 200
    return jsonify(Status=status)

# http://0.0.0.0:port/whoami
@app.route('/whoami', methods=['GET'])
def who_am_i():
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    return  jsonify(FirstName=firstname, LastName=lastname)

# https://webhook.site/example123

# http://0.0.0.0:port/alert
@app.route('/alert', methods=['POST'])
def alert():
    json_obj = request.get_json(force=True)
    try:
        requests.post(config['WEBHOOK']['webhook_url'], json=json_obj)
    except Exception as e:
        logging.error(e)
        return jsonify(Success=False, Error=str(e))
    return jsonify(Success=True)

# http://0.0.0.0:port
if __name__=="__main__":
    app.run(host=config['APISERVER']['api_host'], port=config['APISERVER']['api_port'], debug=True)