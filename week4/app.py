from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="any string but secret"

#首頁
@app.route("/")
def index():
    return render_template("index.html")

#成功頁面網址
@app.route("/member")
def member():
    if "nameData" in session:
        return render_template("member.html")
    return render_template("index.html")

#失敗頁面網址
@app.route("/error")
def error():
    message=request.args.get("message","發生錯誤")
    return  render_template("error.html",message=message)

#驗證功能網址
@app.route("/signin",methods=["POST"])
def signin():
    nameData=request.form["nameData"]
    passwordData=request.form["passwordData"]
    nameData=str(nameData)
    passwordData=str(passwordData)
    if nameData=="test" and passwordData=="test":
        session["nameData"]=nameData
        return redirect("/member")
    if nameData=="" or passwordData == "":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

#登出功能網址
@app.route("/signout")
def signout():
    del session["nameData"]
    return redirect("/")

# @app.route("/square/<number>",methods=["POST"])
# def square(number):
#     num=request.form["numberData"]
#     number=num
#     # number=str(num)
#     return number

# @app.route("/square/<number>")
# def square(number):
#     return number

@app.route("/square",methods=["POST"])
def square():
    num=request.form["numberData"]
    print(type(num))
    return 

app.run(port=3000)