upadted app.py
 
from flask import Flask
import socket
import requests
 
app = Flask(__name__)
 
@app.route('/')
def hello_cloud():
    return 'Welcome to manchikanti Final Test API Serve'
 
@app.route('/host')
def host_name():
    return socket.gethostname()
 
@app.route('/ip')
def host_ip():
    # Return public IP (works in ECS Fargate)
    return requests.get('https://checkip.amazonaws.com').text.strip()
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
