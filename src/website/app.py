from http import client
from os import access
import re
from flask import Flask, render_template, request, session, redirect
from zenora import APIClient
from creds import BOT_TOKEN, REDIRECT_URL, OAUTHURL, CLIENT_SECRET, APP_SECRET_KEY

app = Flask(' ')
app.config['SECRET_KEY'] = APP_SECRET_KEY
client = APIClient(token=BOT_TOKEN, client_secret=CLIENT_SECRET)


@app.route('/')
def index():
    return render_template('index.html', oauth_url=OAUTHURL)


@app.route('/oauth/callback')
def callback():
    code = request.args['code']
    access_token = client.oauth.get_access_token(
        code=code, redirect_uri=REDIRECT_URL).access_token
    session['token'] = access_token
    '''
    bearer_client = APIClient(access_token, bearer=True)
    current_user = bearer_client.users.get_current_user()
    return str(current_user)
    '''
    return redirect('/')


app.run(debug=True)
