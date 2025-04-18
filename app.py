from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def my_page():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get("name", "")
    if name:
        return f"Hello {name}!"
    return "Hello!"

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get("num1", default=0))
        num2 = float(request.args.get("num2", default=0))
        if (num1 + num2) > 5.8:
            prediction = 1
        else: prediction = 0
        return jsonify({"prediction": prediction, "features": {"num1": num1, "num2": num2}})
    
    except ValueError:
        return jsonify({"error": "Niepoprawne wartości liczbowe"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8000)
