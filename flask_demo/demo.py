from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print("Classifier is ready")
print(time.time() - start_time, "seconds")

@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        df = []
        df.append(text)
        print(text)
        with open("logs.txt", "a") as f:
            f.write("<response>\n")
            f.write(text + '\n')
            prediction_message = classifier.get_prediction_message(df)
            print(prediction_message)
            f.write(prediction_message + '\n')
            f.write("</response>\n\n")

    return render_template('hello.html', text=text, prediction_message=prediction_message)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
