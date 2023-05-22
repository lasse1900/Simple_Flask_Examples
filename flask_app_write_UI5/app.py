from flask import Flask, render_template, request
import csv
import subprocess
from counting import counting

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write_csv', methods=['POST'])
def write_csv():
    filename = 'output.csv'
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

    return render_template('result.html', message='Python method/program started successfully.')

if __name__ == '__main__':
    app.run(debug=True)
