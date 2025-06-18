from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print to the console
    return param  # Display in browser

@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(n) for n in range(param))
    return numbers + "\n"  # match test expectation: ends with newline

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Cannot divide by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)
