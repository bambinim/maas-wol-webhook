import os
from pathlib import Path
import yaml
from machine import Machine
from dotenv import load_dotenv

BASE_DIR = Path(os.path.dirname(__file__))

CONFIG_FILE = BASE_DIR / 'config.yaml'

if os.path.exists(BASE_DIR / '.env.local'):
    load_dotenv(BASE_DIR / '.env.local')
elif os.path.exists(BASE_DIR / '.env'):
    load_dotenv(BASE_DIR / '.env')


HOST = os.environ.get('HOST') or '127.0.0.1'
PORT = os.environ.get('PORT') or 8000
SSH_KEY_PATH = os.environ.get('SSH_KEY_PATH') or Path('~/.ssh/id_rsa')


MACHINES = []


def load_machines():
    with open(CONFIG_FILE, 'r') as fstream:
        machines = yaml.safe_load(fstream)
    for k, v in machines['hosts'].items():
        MACHINES.append(Machine(name=k, mac=v['mac'], ip=v['ip'], token=v['token'], ssh_user=v['ssh_user']))
