from Message import Message
import DBUtils as ut
import SMSUtils as sms
from flask import Flask, render_template, request,redirect,url_for,session

app = Flask(__name__)
app.secret_key = 'password'

DEFAULT_MESSAGE = 'Hey this is the default rn, but we can change it later'

@app.route("/", methods = ['GET', 'POST'])
def mainpage():
    conversations = list(sms.get_messages().keys())
    return render_template("index.html", sent_to = conversations)

@app.route("/newnumber")
def newnumber():
    dic = ut.get_one_number()
    return render_template("form.html", name=dic["name"], age=dic["age"], gender = dic["gender"], phone=dic["phone"])

@app.route("/sendmessage",  methods = ['GET'])
def sendmessage():
    number = request.args.get('phone')
    body = request.args.get('body')
    print(number)
    print(body)
    if(number == None):
        dic = ut.get_one_number()
        if(dic != False):
            return render_template("form.html", name=dic["name"], age=dic["age"], gender = dic["gender"], phone=dic["phone"])
        else:
            return "error"
    if(body == None):
        dic = ut.get_one_number()
        if(dic != False):
            return render_template("form.html", name=dic["name"], age=dic["age"], gender = dic["gender"], phone=dic["phone"])
        else:
            return "error"
    number = sms.translatePhone(number)
    print(number)
    m = Message("name", number, body)
    result = sms.send_message(m)
    if(result == False):
        dic = ut.get_one_number()
        return render_template("form.html", name=dic["name"], age=dic["age"], gender = dic["gender"], phone=dic["phone"], status = "Message could not send")
    else:
        dic = ut.get_one_number()
        return render_template("form.html", name=dic["name"], age=dic["age"], gender = dic["gender"], phone=dic["phone"], status="Message sent sucessfully")
    

@app.route("/messages", methods = ['GET', 'POST'])
def viewmessages():
    phone = request.args.get('phone')
    if(phone == None):
        return "error"
    else:
        phone = "+" + phone.strip()
        print(phone)
        return render_template("viewmessages.html", table=sms.view_messages(phone), phone=phone)

@app.route("/reply", methods = ['GET', 'POST'])
def reply():
    phone = request.form.get('phone')
    body = request.form.get('body')
    print(phone)
    print(body)
    if(phone == None):
        return "error"
    if(body == None):
        return "error"
    else:
        phone = "+" + phone.strip()
        print(phone)
        m = Message("name", phone, body)
        result = sms.send_message(m)
        if(result == False):
            return "Message not sent"
        else:
            return "Message sent succesfully"
        
@app.route("/getTable", methods = ['GET', 'POST'])
def getTable():
    phone = request.form.get('phone')
    print(phone)
    if(phone == None):
        return "error"
    else:
        print(phone)
        return sms.getMessagesTable(phone)
    
@app.route("/newMessage", methods = ['GET', 'POST'])
def getNewMessage():
    return ""


if __name__=="__main__":
    app.run("localhost", 8080, debug = True)

