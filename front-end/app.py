from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/home')
def home():
  return render_template('index.html')

app.run(host="0.0.0.0", port=5000, debug=True)
