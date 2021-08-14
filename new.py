from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/data', methods = ['Post'])
def data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')


    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)
   
    return "Form Submitted"




if __name__=='__main__':
    app.run(debug=True)