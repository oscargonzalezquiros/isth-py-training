
from flask import Flask, escape, request

app= Flask(__name__)

@app.route('/') 
 
def suma():
  numero1 = int(request.args.get("number1", "number1"))
  numero2 = int(request.args.get("number2", "number2"))
  total  =  numero1  +  numero2
    
  return f'Sumatoria=, {escape(total)}  !'


