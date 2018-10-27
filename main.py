from flask import Flask, render_template, request


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/AngerManagment")
def main():
    return render_template("main.html")


@app.route("/create", methods=["POST"])
def create():
    var1 = 0
    var2 = 0
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    verified = False
    #if email is entered
    if len(email) > 0:
        # verify if @ and . is in email
        if "@" in email and "." in email:
                verified = True
        else:
            verified = "False"
            email_error = "This is not a valid email."
    #else: 
        #email_error = "Did not enter email correctly, please try again."
    
    if len(password) >= 3 and len(password) <= 20:
        verified = True
    else:
        verified = "False"        
        password_error = " This password is invalid."
    
    if len(verify) >= 3 and len(verify) <= 20:
        verified = True
    else:
        verified = "False"        
        password_error = " This Verify password is invalid."


    if password == verify:
        verified = True
    else: 
        verified = False
        verify_error = "Please double check your password"  
    
    if verify_error == password_error:
        verified = True
    else:
        verified = "False"
        verify_error = "Please double check your password."
    if len(username) > 0 and len(username) < 20:
        verified = True
    else:
        verified = False
        username_error = "Must have to be between 3 and 20 characters."
    
    return render_template("main.html", username=username, password=password, verify=verify, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)
app.run()
