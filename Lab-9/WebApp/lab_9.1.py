from flask import Flask,render_template

app = Flask(__name__)

@app .route('/<opt>/<float:a>/<float:b>')
def calculate(a, b, opt):
    if opt == "add":
        operator = '+'
        result = a + b
        return f'<h3>{a} {operator} {b} = {result}</h3>'
    elif opt == "sub":
        operator = '-'
        result = a - b
        return f'<h3>{a} {operator} {b} = {result}</h3>'
    elif opt == "mul":
        operator = 'x'
        result = a * b
        return f'<h3>{a} {operator} {b} = {result}</h3>'
    elif opt == "div":
        operator = '/'
        result = a / b
        return f'<h3>{a} {operator} {b} = {result}</h3>'
    else:
        return "Invalid operation"



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)