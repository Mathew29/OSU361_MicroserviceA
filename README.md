# OSU 361 Microservice A

This microservice generates upon request, a username and password using ZeroMQ.

## Prerequisites
- **pip**
- **requests**
- **zmq**
- **typing**


## Installation

Clone the repository to your local machine
```bash
git clone https://github.com/Mathew29/OSU361_MicroserviceA.git
cd OSU361_MicroserviceA/src
```

## How to run

Set up Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

Install Dependencies
```bash
pip install -r requirements.txt
```

Run the application
```bash
python generator.py
```

## Example of JSON messages to send to this microservice below:
```json
{
"username": false,
"password": {
    "generatePassword": true,
    "special": true,
    "lowercase": true,
    "uppercase": true,
    "numbers": true,
    "length": 16
    }
}
```
```json
{
"username": true,
}
```
```json
{
"password": {
    "generatePassword": true,
    "special": true,
    "lowercase": true,
    "uppercase": true,
    "number": true,
    "length": 16
    }
}
```

## Example of Requesting and Receiving Code
To receive messages from this microservice, you must connect using ZeroMQ on tcp://123.0.0.1:5600. 

Example call to Request and Receive username and password
```python
import json
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5600")

# create a JSON object formatted similar to the above examples

msg = json.dumps(jsonObject)
socket.send(packet_json.encode('utf-8'))

response = socket.recv().decode('utf-8)
```

## UML Diagram
![image](https://github.com/user-attachments/assets/f8f43bb5-8ee0-4787-b8f0-a7e41f5b23ed)





