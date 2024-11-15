# OSU 361 Microservice A

This microservice generates upon request, a username and password using ZeroMQ.

## Prerequisites
- **pip**
- **requests**
- **zmq**


## Installation

Clone the repository to your local machine
```bash
git clone https://github.com/Mathew29/OSU361_MicroserviceA.git
cd OSU361_MicroserviceA/
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

## Example of Requesting and Receiving Code
To receive messages from this microservice, you must connect using ZeroMQ subscriber on tcp://123.0.0.1:5600. 

Example of JSON message to send to this microservice:
```json
{
'username': False,
'password': {
    'generatePassword': True,
    'special': True,
    'lowercase': True,
    'uppercase': True,
    'numbers': True,
    'length': 16
    }
}
```



