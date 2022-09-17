from http import client
from os import access
import re
from flask import Flask, render_template, request, session, redirect
from zenora import APIClient
from creds import BOT_TOKEN, REDIRECT_URL, OAUTHURL, CLIENT_SECRET, APP_SECRET_KEY

app = Flask(' ')
app.config['SECRET_KEY'] = APP_SECRET_KEY
client = APIClient(token=BOT_TOKEN, client_secret=CLIENT_SECRET)


@app.route('/login')
def index():
    return render_template('login.html', oauth_url=OAUTHURL)


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


@app.route('/')
def home():
    try:
        bearer_client = APIClient(session['token'], bearer=True)
        current_user = bearer_client.users.get_current_user()
        edit_rights = False
        # if current_user.id in [686898495063719939,300503128170692620]:
        if current_user.id in [300503128170692620]:
            edit_rights = True
        return render_template('home.html', pfp=current_user.avatar_url, username=current_user.username, id=current_user.discriminator, rights=edit_rights)
    except KeyError:
        return redirect('/login')


@app.route('/edit')
def edit():
    try:
        bearer_client = APIClient(session['token'], bearer=True)
        current_user = bearer_client.users.get_current_user()
        # if current_user.id in [686898495063719939,300503128170692620]:
        if current_user.id in [300503128170692620]:
            return 'you can edit the dashboard items'
        return 'you currently dont have the permissions to edit '

    except KeyError:
        return redirect('/login')


app.run(debug=True)
