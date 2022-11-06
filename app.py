from flask import Flask , render_template ,request
app = Flask(__name__)

@app.route('/<int:num1>')
def home(num1):
   return render_template('index.html',n1 = num1)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    return render_template('register.html', name=name, number=number, email=email)

@app.route('/about')
def about():
    return render_template('about.html')

app.add_url_rule('/home','home', home)

if __name__ == '__main__':
    app.run(debug=True)