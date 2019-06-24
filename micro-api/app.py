import os, re, base64
from flask import Flask, render_template, request, session, jsonify
app = Flask(__name__)

# set secrekey to use session
app.secret_key = os.urandom(24)

@app.route('/test',methods = ['POST', 'GET'])
def test():
   print('TEST method:\n', request.method)
   if request.method == 'POST':
      data = dict(zip(('code', 0), ('msg', 'ok')))
      return jsonify(data)
   else:
      return "Hello World"  


if __name__ == '__main__':
   # run app
   app.run(host='localhost', port=5000, debug = True)