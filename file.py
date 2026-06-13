from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Hello! Your Flask API is running on port 5000. I'm Your updated API!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)