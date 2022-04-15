from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    {
        'description':'salary', 'amount':5000
    }
]

@app.route("/")
def what_the_hell():
    return "what the hell!?"

@app.route("/incomes")

def hello_world():
    return "hello, world"



