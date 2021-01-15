
from flask import Flask,render_template,request
from helper.helper import passgen, shorten_url

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/passgen',methods=['GET','POST'])
def generate_password() :

    errors = {}

    if request.method == 'POST' :
        length = request.form['length']     #Extract length of password from form!

        """
        add_sym = request.form['symbol']    #Get value of Symbol checkbox!
        add_num = request.form['number']    #Get value of number checkbox!
        """

        password = passgen(length)      #pass add_sym & add_num argument!

        return render_template('passgen.html', errors = errors, password = password)

    else :

        return render_template('passgen.html', errors = errors)


@app.route('/link/shorten')
def link_shortener():

    errors = {}

    if request.method == 'POST' :
        url = request.form['fullurl']   #Get Url from form!
        short_link = shorten_url(url)   # TODO:Add support for multiline links!

        return render_template('shortener.html', errors=errors, short_link=short_link)
    else :

        return render_template('shortener.html', errors=errors)

