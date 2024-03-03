from flask import Flask, redirect, url_for, render_template, request, session
import requests

app = Flask(__name__)
app.secret_key = "vipan kumar"

# facebook credentials
Fb_APP_ID = "334870495569330"
Fb_APP_SECRET = "32424e1509204734227b117e7b0b2346"
FB_REDIRECT_URI = "http://localhost:5000/facebook/callback"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/facebook/login')
def facebook_login():
    return redirect(f"https://www.facebook.com/v12.0/dialog/oauth?client_id={Fb_APP_ID}&redirect_uri={FB_REDIRECT_URI}&scope=email")

@app.route('/facebook/callback')
def facebook_callback():
    code = request.args.get('code')
    if code:
        resposne = requests.get(
            f"https://graph.facebook.com/v12.0/oauth/access_token?client_id={Fb_APP_ID}&redirect_uri={FB_REDIRECT_URI}&client_secret={Fb_APP_SECRET}&code={code}"
        )
        data = resposne.json()
        if "access_token" in data:
            session['access_token'] = data['access_token']

            # fetch urer data
            user_response = requests.get(
                f"https://graph.facebook.com/v12.0/me?fields=id,name,email&access_token={data['access_token']}"
            )

            print("user -resposne", user_response)
            for i in user_response:
                print(i)
            return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)