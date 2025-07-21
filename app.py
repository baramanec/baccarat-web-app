from flask import Flask, render_template, request
from logic import calculate_win_rate
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        history = request.form.get('history')  # 例如 "B,P,B,T,P"
        result = calculate_win_rate(history)
        return render_template('index.html', result=result, history=history)
    return render_template('index.html', result=None, history="")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
