from flask import Flask, render_template, request
from counting import counting
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write_csv1', methods=['POST'])
def write_csv1():
    filename = 'output1.csv'
    variables = request.form.get('variables')

    if not variables:
        return render_template('index.html', error='Missing variables.')

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(variables.split(','))

    return render_template('result.html', filename=filename)

@app.route('/write_csv2', methods=['POST'])
def write_csv2():
    filename = 'output2.csv'
    variables = request.form.get('variables')

    if not variables:
        return render_template('index.html', error='Missing variables.')

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(variables.split(','))

    return render_template('result.html', filename=filename)

@app.route('/start_program', methods=['POST'])
def start_program():
    # Perform any necessary actions or operations for your Python method/program
    # ...

    # Run a Python method/program using subprocess
    # subprocess.run(['python', 'counting.py'])
    counting()

    return render_template('result2.html', message='Python program started successfully.')

if __name__ == '__main__':
    app.run(debug=True)
