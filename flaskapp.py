
from flask import Flask,render_template,request
from helper.helper import passgen, shorten_url

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/passgen',methods=['GET','POST'])
def generate_password() :

    values = request.form
    values.errors = {}
    if request.method == 'POST' :
        length = request.form['length']     #Extract length of password from form!

        """
        add_sym = request.form['symbol']    #Get value of Symbol checkbox!
        add_num = request.form['number']    #Get value of number checkbox!
        """

        password = passgen(length)      #pass add_sym & add_num argument!
        if password :
            return render_template('passgen.html', values= values, password = password)
        else :
            values.errors['error'] = 'An Error Occured!'
            return render_template('passgen.html', values = values )

    else :

        return render_template('passgen.html', values = values)


@app.route('/shorten',methods=['GET','POST'])
def link_shortener():

    values = request.form
    values.errors = {}
    if request.method == 'POST' :
        url = values['fullurl']   #Get Url from form!
        short_link = shorten_url(url)   # TODO:Add support for multiline links & option for other API
        print(short_link)
        if short_link :
            return render_template('shortener.html', values = values, short_link=short_link)
        else :
            values.errors['error'] = 'Error Occured While Processing your request\nCheck your link!'
            return render_template('shortener.html', values = values, short_link = short_link)
    else :

        return render_template('shortener.html', values = values)

