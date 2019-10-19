# views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''

    title = 'Home -  best pitches'

    return render_template('index.html',title = title)