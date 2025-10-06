from flask import Flask, render_template, request, jsonify
from chatbot import ChattyBot

app = Flask(__name__)
chatbot = ChattyBot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    # handle exit phrases
    if user_input.lower() in ['exit', 'bye', 'quit', 'nice to talk to you']:
        reply = "Always there for you , have a nice day and feel free to talk anytime !"
    else:
        reply = chatbot.get_response(user_input)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
