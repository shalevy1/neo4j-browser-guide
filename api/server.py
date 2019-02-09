from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)


@app.route('/<file>')
def root(file):
    return render_template('html/' + file)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
