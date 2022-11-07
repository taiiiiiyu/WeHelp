from flask import Flask,request,render_template,redirect,session,jsonify
import mysql.connector

app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="any string but secret"


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="website"
)


#首頁
@app.route("/")
def index():
    return render_template("index.html")

#成功頁面網址
@app.route("/member")
def member():
    if "username" in session:
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM member WHERE username =%s",(session["username"],))
        user=mycursor.fetchone()
        session["name"]=user[1]
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
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM member WHERE username =%s",(usernameData,))
    user=mycursor.fetchone()
    if "username" in session:
        return render_template("loggedIn.html")
    if user==None:
        return redirect("/error?message=沒有此帳號")
    userN=user[2]
    userP=user[3]
    if usernameData=="" or passwordData == "":
        return redirect("/error?message=請輸入帳號、密碼")
    elif userN==usernameData and userP==passwordData :
        session["username"]=usernameData
        return redirect("/member")
    return redirect("/error?message=帳號、或密碼輸入錯誤")

#驗證註冊網址
@app.route("/signup",methods=["POST"])
def signup():
    nameData=request.form["nameData"]
    usernameData=request.form["usernameData"]
    passwordData=request.form["passwordData"]
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM member WHERE username =%s",(usernameData,))
    user=mycursor.fetchone()
    if usernameData=="" or passwordData == "" or nameData=="":
        return redirect("/error?message=請輸入姓名、帳號、密碼")
    elif user != None:
        return redirect("/error?message=帳號已經被註冊")
    else:
        mycursor.execute("INSERT INTO member (name, username, password) VALUES (%s,%s,%s)",(nameData,usernameData,passwordData,))
        mydb.commit()
        session["name"]=request.form["nameData"]
        session["username"]=request.form["usernameData"]
        session["password"]=request.form["passwordData"]
        return redirect("/")


#登出成功網址
@app.route("/signout")
def signout():
    del session["username"]
    return redirect("/")


@app.route("/api/member",methods=["GET","PATCH"])
def api():
    username=request.args.get("")
    if request.method=="GET":
        if username!="":
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM member WHERE username =%s",(username,))
            user=mycursor.fetchone()
            null=None
            if "username" in session and user!=None:
                data={"id":user[0],"name":user[2],"username":user[1]}
                return jsonify({"data":data})
            return jsonify({"data":null})
        return jsonify({"data":False})
    else:
        updateName=request.get_json()
        updateName=updateName["name"]
        if "username" in session and updateName!="":
            memberUsername=session["username"]
            mycursor=mydb.cursor()
            mycursor.execute("UPDATE member SET name=%s WHERE username=%s",(updateName,memberUsername,))
            mydb.commit()
            return jsonify({"ok":True})
        return jsonify({"error":True})



if __name__=="__main__":
    app.run(debug=True,port=3000)