from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    asset = {'name': 'DRAX'}
    transformer = [
        {
            'subnode1': {'name': 'TX1'},
            'subnode2': 'FIRST DESCRIPTION TYPE'
        },
        {
            'subnode1': {'name': 'TX2'},
            'subnode2': 'SECOND DESCRIPTION TYPE'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           asset=asset,
                           transformer=transformer)
