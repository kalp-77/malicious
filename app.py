from flask import Flask
from flask import Flask, request, jsonify
from flask import jsonify
from prediction import predictor


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_url():
    return jsonify({"status":"Success"})


@app.route('/detect', methods=['POST'])
def detect_url():
    data = request.json
    if data and 'url' in data:
        url = data['url']
        result = predictor(url)
        if result == 0:
            return jsonify({"result": "No", "message": "The URL is not detected as malicious."})
        else:
            return jsonify({"result": "Yes", "message": "The URL is detected as malicious."})




app.run(debug=False)
