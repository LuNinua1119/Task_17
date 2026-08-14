from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/multiply/<int:a>/<int:b>/<int:c>/<int:d>')
def multiply(a,b,c,d):
    result = a * b * c * d

    return f' შედეგი : {result}'

@app.route('/info')
def info():
    data = {
        "name" : "Luka",
        "last name" : "Ninua",
        "gender" : "Male",
    }

    return jsonify(data)

@app.route('/hello/<name>')
def hello(name):
    return f'გამარჯობა, {name}'

@app.errorhandler(404)
def page_not_found(error):
    return "თქვენ მოხვდით არარსებულ გვერდზე, გთხოვთ დაბრუნდეთ მთავარ გვერდზე", 404


if __name__ == '__main__':
    app.run(debug=True)