from flask import Flask, render_template, request

app = Flask(__name__)

def process_input(input_data):
    # Example processing logic
    return input_data.upper()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_data = request.form['input_data']
    result = process_input(input_data)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)