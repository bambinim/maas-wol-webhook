#!/usr/bin/env python
from flask import Flask, request, Response
import settings
from machine import Machine

settings.load_machines()

app = Flask(__name__)


def machine_from_token(token: str) -> Machine or None:
    for i in settings.MACHINES:
        if i.token() == token:
            return i
    return None


def machine_from_name(name: str) -> Machine or None:
    for i in settings.MACHINES:
        if i.name() == name:
            return i
    return None


@app.route('/startup', methods=['POST'])
def startup():
    if 'Authorization' not in request.headers:
        return Response({'status': 400, 'message': 'Token not found'}, status=400)
    token = request.headers['Authorization'].replace('Bearer ', '')
    machine = machine_from_token(token)
    if machine is None:
        return Response({'status': 400, 'message': 'Token not valid'}, status=400)
    machine.startup()
    return {'status': 200, 'message': 'WoL magic packed sent'}


@app.route('/shutdown', methods=['POST'])
def shutdown():
    try:
        if 'Authorization' not in request.headers:
            return Response({'status': 400, 'message': 'Token not found'}, status=400)
        token = request.headers['Authorization'].replace('Bearer ', '')
        machine = machine_from_token(token)
        if machine is None:
            return Response({'status': 400, 'message': 'Token not valid'}, status=400)
        machine.shutdown(ssh_key_file=settings.SSH_KEY_PATH)
        return {'status': 200, 'message': 'Shutdown command sent'}
    except Exception:
        pass


@app.route('/status', methods=['GET'])
def status():
    if 'name' not in request.args:
        return Response({'status': 400, 'message': 'Machine name not specified'}, status=400)
    machine = machine_from_name(request.args['name'])
    return {
        'status': 200,
        'power_status': 'running' if machine.status() else 'stopped'
    }


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT, debug=True)
