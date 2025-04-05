from flask import Flask
app = Flask(__name__)  # ✅ Use double underscores

@app.route("/")
def home():
    return "Hello from Flask App!"

if __name__ == "__main__":  # ✅ Correct comparison
    app.run(host="0.0.0.0", port=5000)
