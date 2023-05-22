from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file selected.')
        
        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No file selected.')

        if file:
            data = file.read().decode('utf-8').splitlines()
            reader = csv.reader(data)

            variables = []

            for row in reader:
                variables.append(row)

            return render_template('result.html', variables=variables)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
