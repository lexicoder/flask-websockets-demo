from flask import Flask, render_template
from flask_sockets import Sockets
import time

app = Flask(__name__)
sockets = Sockets(app)

@app.route('/echo_test', methods=['GET'])
def echo_test():
    return render_template('echo_test.html')

@app.route('/client_echo_test', methods=['GET'])
def client_echo_test():
    return render_template('client.html')

@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message + ' ' + str(time.time()))

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()