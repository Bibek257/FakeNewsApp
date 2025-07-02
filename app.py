from flask import Flask, render_template, request
import joblib

# Load model
model = joblib.load('fake_news_model.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        user_input = request.form['news_text']
        if user_input.strip() != '':
            prediction = model.predict([user_input])[0]
            prediction = "Fake News" if prediction == 0 else "Real News"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
