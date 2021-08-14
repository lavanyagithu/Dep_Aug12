from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('landing.html')

@app.route('/contact')
def contactc():
    return render_template('contact.html')

@app.route('/feedback')
def contacfeedbackf():  
    return render_template('feedback.html')

@app.route('/gallary')
def gallary():
    return 'This is a gallary page'

@app.route('/data', methods = ['Post'])
def data():
    First_Name = request.form.get('First_Name')
    second_Name = request.form.get('second_Name')
    number  = request.form.get('Number')
    email = request.form.get('email')

    print(First_Name)
    print(second_Name)
    print(number)
    print(email)

    return 'form submitted'


if __name__=='__main__':
    app.run(debug=True)

