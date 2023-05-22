from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def create_csv():
    if request.method == 'POST':
        variables = request.form.getlist('variable')
        
        if not variables:
            return render_template('index.html', error='No variables entered.')

        filename = 'output.csv'

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(variables)

        return render_template('result.html', filename=filename)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
