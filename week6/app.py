from flask import Flask,request,render_template,redirect,session
from flask_mysqldb import MySQL
# import MySQLdb.cursors


app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="any string but secret"
app.config['MYSOL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='12345678'
app.config['MYSQL_DB']='website'
app.config['MYSQL_PORT']='3306'
mysql=MySQL(app)

#首頁
@app.route("/")
def index():
    return render_template("index.html")

#成功頁面網址
@app.route("/member")
def member():
    if "username" in session:
        return render_template("member.html")
    return render_template("index.html")
#失敗頁面網址
@app.route("/error")
def error():
    message=request.args.get("message","發生錯誤")
    return render_template("error.html",message=message)

#驗證功能網址
@app.route("/signin",methods=["POST"])
def signin():
    usernameData=request.form["usernameData"]
    passwordData=request.form["passwordData"]
    if usernameData=="test" and passwordData=="test":
        session["username"]=usernameData
        return redirect("/member")
    if usernameData=="" or passwordData == "":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

#驗證註冊網址
@app.route("/signup",methods=["POST"])
def signup():
    # nameData=request.form["nameData"]
    # usernameData=request.form["usernameData"]
    # passwordData=request.form["passwordData"]
    cur=mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv=cur.fetchall()
    return str(rv)
    # cursor.execute("SELECT * FROM member WHERE username =%s",usernameData)
    # account=cursor.fetchone()
    # if account:
    #     return render_template("error.html")


#登出成功網址




















if __name__=="__main__":
    app.run(debug=True,port=3000)