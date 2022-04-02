
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/parking')
def parking():
    return render_template('parking.html')

if __name__ == "__main__":
    app.run(debug=True)