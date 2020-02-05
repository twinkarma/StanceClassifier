from flask import Flask
from flask import request
from flask import jsonify
from stanceclassifier import StanceClassifier

stance_classifier = None

app = Flask(__name__)

def init_server():
    global stance_classifier
    stance_classifier = StanceClassifier("lr")

@app.route('/', methods=['POST', 'GET'])
def index():
    try:

        if stance_classifier is None:
            return jsonify({"error": "Could not start classifier"})

        if request.method == 'POST':
            req_json = request.get_json()
            if "original" in req_json.keys() and "reply" in req_json.keys():
                print("Request received")
                print(req_json["original"])
                print(req_json["reply"])

                stance_class, stance_prob = stance_classifier.classify(req_json["original"], req_json["reply"])
                print("classified as {} {}".format(stance_class, stance_prob))
                return jsonify({"stance_class": stance_class, "stance_prob": stance_prob.tolist()}), 200

        return jsonify({"error": "Invalid input"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400



# run the server
if __name__ == '__main__':
    init_server()
    app.run(host='0.0.0.0', port='9125', debug=True)






