from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!<br>  How are you toaday?"
    
if __name__ == "__main__":
    app.run()
