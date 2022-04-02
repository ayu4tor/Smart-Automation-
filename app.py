
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def automation():
    return render_template('automation.html')

@app.route('/bulb', methods=['get', 'post'])
def bulb():
    led = request.form['led']
    from ayushi import fire
    led = fire.run(led)
    return render_template('automation.html',
                            led=int(led),
                            )

if __name__ == "__main__":
    app.run(debug=True)