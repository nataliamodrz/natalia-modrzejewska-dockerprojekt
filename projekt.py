from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET', 'POST'])
def predict():
    # Pobieramy wartości z parametrów żądania (GET lub POST)
    number1 = request.args.get('number1', default=0, type=float)
    number2 = request.args.get('number2', default=0, type=float)

    # Prosta logika predykcji
    total = number1 + number2
    prediction = 1 if total > 5.8 else 0

    # Przygotowanie odpowiedzi
    response = {
        "prediction": prediction,
        "features": {
            "number1": number1,
            "number2": number2
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
