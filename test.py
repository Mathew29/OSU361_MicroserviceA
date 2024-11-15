import json
import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5600")

packet = {
    'username': True,
    'password': {
        "generatePassword": True,
        "special": True,
        "lowercase": True,
        "uppercase": True,
        "numbers": True,
        "length": 16
    }
}

print(f"sending packet: {packet}")
packet_json = json.dumps(packet)
socket.send(packet_json.encode('utf-8'))

msg = socket.recv().decode('utf-8')
print(f"Received msg: {msg}")
