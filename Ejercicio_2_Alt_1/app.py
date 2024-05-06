from flask import Flask, request, json, render_template, Response, jsonify
from similarity import Similarity

app = Flask(__name__)

@app.route('/')

def index():

    return render_template('form.html')

@app.route('/process', methods=['GET', 'POST'])

def process():
    if request.method == 'POST':

        text = request.form['text']
        number = request.form['number']
        try:
            number = float(number)
        except (TypeError, ValueError):
            return jsonify({'Error': 'Invalid number'}), 400

        instance = Similarity(text, number)
        result = instance.similarity_percentage()
        result_json=json.dumps(result, indent=4, ensure_ascii=False, sort_keys=False)
        response=Response(result_json, content_type='/process; charset=utf-8')
        return  response
    
    return 'Not allowed method', 405

if __name__ == '__main__':
    app.run(debug=True)