from flask import Flask, render_template, request
import csv
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def create_csv():
    if request.method == 'POST':
        # keyword = request.form.get('keyword')
        # location = request.form.get('location')
        keyword = "keyword"
        location = "location"
        variables = [
            request.form.get('variable1'),
            request.form.get('variable2'),
            request.form.get('variable3'),
            request.form.get('variable4')
        ]

        if not keyword or not location or not any(variables):
            return render_template('index.html', error='Missing keyword, location, or variables.')

        filename = 'output.csv'

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(['keyword', 'location'])  # Write the fixed header line
            writer.writerow([keyword, location])  # Write the keyword and location
            for variable in variables:
                if variable:
                    writer.writerow(variable.split(','))  # Write each variable line

        return render_template('result.html', filename=filename)
    
    return render_template('index.html')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)