from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html', name='User')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email == 'wildan@admin.com' and password == '12345678':
        return render_template('welcome.html')
    else:
        return "Login gagal. Silakan coba lagi."
    
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/biodata')
def biodata():
    return render_template('biodata.html')

@app.route('/submit_biodata', methods=['POST'])
def submit_biodata():
    fullname = request.form.get('fullname')
    address = request.form.get('address')
    phone = request.form.get('phone')
    
  
    return render_template('displaydata.html', fullname=fullname, address=address, phone=phone)
if __name__ == '__main__':
    app.run(debug=True)
