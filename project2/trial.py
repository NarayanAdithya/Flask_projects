from flask import Flask, render_template,url_for,redirect,json

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/apifetch')
def apifetch():
    return render_template('apifetch.html')


if __name__ == '__main__':
    app.run(debug=True)
