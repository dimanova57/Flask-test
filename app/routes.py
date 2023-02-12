from flask import render_template, request, flash, redirect
from app import app
from app.bd_communicate import add_question, get_all_tests


@app.route('/')
def index():
    return render_template("pass_test.html")


@app.route('/add_test', methods=['POST', 'GET'])
def add_test():
    if request.method == 'POST':
        question = request.form['question']
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        correct = request.form['correct']
        msg = add_question(question, ans1, ans2, correct)

        flash(msg)
        redirect('/add_test')
    return render_template("add_test.html")


@app.route('/pass_test', methods=["POST", "GET"])
def pass_test():
    all_tests = get_all_tests()
    return render_template('pass_test.html', all_tests=all_tests)
