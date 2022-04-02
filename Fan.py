from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def Faning():
    return render_template('Fan.html')

@app.route('/Fan', methods=['get', 'post'])
def Fan():
    Fan = request.form['Fan']
    from ayushi import fire
    Fan = fire.run(Fan)
    return render_template('Fan.html',
                            Fan=int(Fan),
                            )

if __name__ == "__main__":
    app.run(debug=True)