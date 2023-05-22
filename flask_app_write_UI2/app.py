from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def create_csv():
    if request.method == 'POST':
        header = request.form.get('header')
        variable1 = request.form.get('variable1')
        variable2 = request.form.get('variable2')
        variable3 = request.form.get('variable3')
        variable4 = request.form.get('variable4')

        if not header or not variable1 or not variable2 or not variable3 or not variable4:
            return render_template('index.html', error='Missing header or variables.')

        filename = 'output.csv'

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header.split(','))  # Write the header line
            writer.writerow(variable1.split(','))  # Write the first variable line
            writer.writerow(variable2.split(','))  # Write the second variable line
            writer.writerow(variable3.split(','))  # Write the third variable line
            writer.writerow(variable4.split(','))  # Write the fourth variable line

        return render_template('result.html', filename=filename)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
