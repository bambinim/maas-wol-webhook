from pathlib import Path
import wakeonlan as wol
import subprocess


class Machine:

    def __init__(self, name: str,  mac: str, ip: str, token: str, ssh_user: str):
        self.__name = name
        self.__mac = mac
        self.__ip = ip
        self.__token = token
        self.__ssh_user = ssh_user

    def startup(self):
        wol.send_magic_packet(self.__mac)

    def shutdown(self, key_file: str or Path = None):
        pass

    def status(self) -> bool:
        proc = subprocess.Popen(['/usr/bin/ping', '-c', '1', self.__ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.wait()
        return proc.returncode == 0

    def __iter__(self):
        yield 'name', self.__name
        yield 'mac', self.__mac
        yield 'ip', self.__ip
        yield 'token', self.__token
        yield 'ssh_user', self.__ssh_user
