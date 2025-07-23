from flask import Flask, render_template, request
from logic import predict_next_bet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    confidence = None
    trend = ""

    if request.method == 'POST':
        trend = request.form['trend']
        result, confidence = predict_next_bet(trend)

    return render_template('index.html', result=result, confidence=confidence, trend=trend)

if __name__ == "__main__":
    app.run(debug=True)