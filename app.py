from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


from basiccal import calculator


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculation',methods=['POST'])
def calculation():

    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = calculator(a,b,operation)

    return render_template('index.html', box=str(result))

if __name__ == "__main__":
    app.run(debug=True)