
from flask import Flask,render_template,request
from helper.helper import passgen, shorten_url, omdb_search, get_info, spellcorrect

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

        add_sym = values['symbol'] if 'symbol' in values else False   #Get value of Symbol checkbox!
        add_num = values['number'] if 'number' in values else False  #Get value of number checkbox!

        add_sym = True if add_sym == 'on' else False
        add_num = True if add_num == 'on' else False

        password = passgen(length, add_sym, add_num)
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

        if short_link :
            return render_template('shortener.html', values = values, short_link=short_link)
        else :
            values.errors['error'] = 'Error Occured While Processing your request\nCheck your link!'
            return render_template('shortener.html', values = values, short_link = short_link)
    else :

        return render_template('shortener.html', values = values)

@app.route('/movie')
def search_movie():

    values = {}
    if request.method=='GET' :
        query = request.args.get('query')
        page = request.args.get('page')

        if not query :
            return render_template('movie_search.html', values = values)
        if page :
            page = int(page)
            results = omdb_search(query,page=page)
        else :
            results = omdb_search(query)
        
        values['query'] = query.replace('+',' ')
        if 'error' in results:
            values['error'] = results['error']
            return render_template('movie_search.html', values = values)

        elif results :
            return render_template('movie_search.html', values = values, results = results, page = page)
        else :
            values['error'] = 'Unknown Error Occured!'
            return render_template('movie_search.html', values = values)

@app.route('/movie/<id>')
def movie_info(id):

    values = {}
    values['id'] = id
    info = get_info(id)

    if 'error' in info :
        values['error'] = info['error']
        return render_template('movie_info.html', values = values )
    elif info :
        return render_template('movie_info.html', values = values, info = info )
    else :
        values['error'] = 'Unknown Error Occured!'
        return render_template('movie_info.html', values = values )
    return id


@app.route('/spellcorrect',methods=['GET','POST'])
def spell_correct() :

   values = request.form
   values.errors = {}
   
   if request.method == 'GET' :
       return render_template('spellcheck.html', values = values)

   if request.method == 'POST' :

       para = values['para']
       checked_para = spellcorrect(para)
       if len(checked_para) == 0:
           values.errors['error'] = 'Atleast Insert something in the input box!'
           return render_template('spellcheck.html',values = values)
       if checked_para :
           return render_template('spellcheck.html',values = values, checked_para = checked_para)
       else :
           values.errors['error'] = 'Some error Occured !'
           return render_template('spellcheck.html',values = values)
