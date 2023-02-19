from flask import render_template, request, flash, redirect
from app import app
from app.bd_communicate import *

last_test = ''


@app.route('/')
def index():
    return render_template("pass_test.html")


@app.route('/add_test', methods=['POST', 'GET'])
def add_test():
    if request.method == 'POST':
        selected_test = request.form['selected']
        question = request.form['question']
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        correct = request.form['correct']
        msg = add_question(selected_test, question, ans1, ans2, correct)

        flash(msg)
        redirect('/add_test')
    return render_template("add_test.html", tablenames=get_all_table_names())


@app.route('/delete_table', methods=["POST"])
def delete_table():
    selected_table = request.form['delete_selected']
    delete_new_table(selected_table)


@app.route('/add_table', methods=["POST"])
def new_table():
    name = request.form['tablename']
    res = create_new_table(name)
    print(res)
    return redirect('/add_test')


@app.route('/pass_test_result', methods=['POST'])
def pass_test_result():
    all_tests = get_all_tests(last_test)
    user_answers = request.form
    correct = 0
    for question in user_answers:
        user_answer = user_answers[question]
        print(user_answer)
        ans = all_tests[question][user_answer]
        if ans:
            correct += 1
    return f"correct -> {correct}"


@app.route('/pass_test/<test_name>')
def pass_test(test_name):
    global last_test
    last_test = test_name
    all_tests = get_all_tests(test_name)
    return render_template('pass_test.html', all_tests=all_tests)
