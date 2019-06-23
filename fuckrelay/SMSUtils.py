from twilio.rest import Client

account_sid = "AC5ab857de1d62b39b0f89b33f9131321b"
auth_token  = "3dd51b71379b851c2930de472f9e9b35"
HOME_NUMBER = "+18452475430"


client = Client(account_sid, auth_token)
def send_message(m):
    try:
        message = client.messages.create(
        to=m.num, 
        from_=HOME_NUMBER,
        body=m.body)
        #record_message(m)
        return True
    except:
        return False
    
def get_messages():
    try:
        print("retrieving messages...")
        dic = {}
        messages = client.messages.list()
        for message in messages:
            try:
                messagedic = {"to" : message.to, "from" : message.from_, "when": message.date_sent, "body" : message.body, "date_sent" : message.date_sent, "direction" : message.direction}
                if(dic.get(message.to) == None):
                    dic[message.to] = [messagedic]
                else:
                    dic[message.to].append(messagedic)
            except Exception as e:
                print(e)
        return dic
    except:
        return False
    
def get_from_message(dic):
    start_tr = "<tr style='background-color:lightblue;'>"
    end_tr = "</tr>"
    body_str="<td>" + dic["from"] + "</td><td>" + dic["body"] + "</td>"
    return start_tr + body_str + end_tr

def get_to_message(dic):
    start_tr = "<tr style='background-color:lightgreen;'>"
    end_tr = "</tr>"
    body_str="<td>" + dic["to"] + "</td><td>" + dic["body"] + "</td>"
    return start_tr + body_str + end_tr

def get_messeges_from_number(dic, phone):
    l = dic[HOME_NUMBER]
    messages_to = []
    for i in l:
        if(i["from"] == phone):
            messages_to.append(i)
    return messages_to

def sort_by_date(e):
    return e[0]["when"]
def view_messages(phone):
    dic = get_messages()
    message_history = dic.get(phone)
    if(message_history == None):
        return "<h3>No messages found with that person</h3>"
    else:
        open_table = "<table border='2%'>"
        end_table = "</table>"
        entire_convo = []
        for i in message_history:
            entire_convo.append((i, True))
        m_to = get_messeges_from_number(dic, phone)
        for i in m_to:
            entire_convo.append((i, False))
        entire_convo.sort(key=sort_by_date)
        body = ""
        for convo in entire_convo:
            if(convo[1]):
                body = body + get_from_message(convo[0])
            else:
                body = body + get_to_message(convo[0])
        return entire_convo
    
def getMessagesTable(phone):
    dic = get_messages()
    message_history = dic.get(phone)
    if(message_history == None):
        return "<h3>No messages found with that person</h3>"
    else:
        open_table = "<table border='2%'>"
        end_table = "</table>"
        entire_convo = []
        for i in message_history:
            entire_convo.append((i, True))
        m_to = get_messeges_from_number(dic, phone)
        for i in m_to:
            entire_convo.append((i, False))
        entire_convo.sort(key=sort_by_date)
        body = ""
        for convo in entire_convo:
            if(convo[1]):
                body = body + get_from_message(convo[0])
            else:
                body = body + get_to_message(convo[0])
        return open_table + body + end_table
    
def translatePhone(phone):
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace(" ", "")
    phone = phone.replace("%20", "")
    phone = phone.replace("-", "")
    return "+1" + phone