from flask import Flask

app = Flask(__name__)

# extremely simple flask app
@app.route('/', methods=['GET'])
def home():
    return 'Go TPT!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)