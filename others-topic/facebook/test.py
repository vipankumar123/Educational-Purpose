from flask import Flask, request, redirect
import requests

app = Flask(__name__)

# Replace YOUR_APP_ID and REDIRECT_URI with your actual values
app_id = '404776325537704'
redirect_uri = 'http://localhost:5000/facebook/callback'
scope = 'user_profile,user_media'
app_secret = '44794c00a6587b03baa64b81e74236fc'

@app.route('/login')
def login():


    auth_url = f'https://api.instagram.com/oauth/authorize?client_id={app_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code'

    return redirect(auth_url)

if __name__ == '__main__':
    app.run()