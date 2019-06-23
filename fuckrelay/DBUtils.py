import sqlite3
import pandas as pd
from Message import Message

DBNAME = 'data/convos.db'
VOTERS_CSV = 'data/voters.csv'
VOTERS_CSV_KEYS = {"name" : "first", "age" : "code", "gender" : "gender", "phone" : "phone"}
def load_convos():
    try:
        conn = sqlite3.connect(DBNAME)
        cursor = conn.execute("SELECT * from convos")
        dic = {}
        for row in cursor:
            m = Message(row[0], row[1], row[2], row[3])
            if(dic.get(row[1]) != None):
                dic[row[1]].append(m)
            else:
                dic[row[1]] = [m]
        conn.close()
        return dic
    except Exception as e:
        print(e)
        return False
    
def create_insert_statement(m):
    if(m.num == None):
        return False
    if(m.body == None):
        return False
    else:
        if(m.date == None):
            s = "INSERT INTO convos (name, phone, message) VALUES ('" + m.name + "','" + m.num + "','" + m.body + "');"
            return s
        else:
            s = "INSERT INTO convos (name, phone, message, date) VALUES ('" + m.name + "','" + m.num + "','" + m.body + "','" + m.date + "');"
            return s
    
def record_message(m):
    try:
        stmt = create_insert_statement(m)
        if(stmt == False):
            return False
        if(stmt == None):
            return False
        conn = sqlite3.connect(DBNAME)
        conn.execute(stmt)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("here")
        return False
    
def insert_voter_stmt(name,age,gender,phone):
    s = "INSERT INTO voters (name, age, gender, phone, status) VALUES ('" + name + "','" + str(age) + "','" + gender + "','" + phone + "', 'y');"
    return s

def record_message(m):
    try:
        stmt = create_insert_statement(m)
        if(stmt == False):
            return False
        if(stmt == None):
            return False
        conn = sqlite3.connect(DBNAME)
        conn.execute(stmt)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        print("here")
        return False
    
def add_voters(voters):
    try:
        conn = sqlite3.connect(DBNAME)
        for voter in voters:
            try:
                conn.execute(voter)
            except:
                continue
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False
    
def isolate_age(dob):
    try:
        birthyear = int(str(dob)[0:4])
        age = 2019 - birthyear
        return age
    except Exception as e:
        return -1
    
def clear_voters_table():
    try:
        stmt = "DELETE from voters WHERE 1;"
        conn = sqlite3.connect(DBNAME)
        conn.execute(stmt)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False

def load_numbers():
    df = pd.read_csv(VOTERS_CSV)
    phone = VOTERS_CSV_KEYS['phone']
    name = VOTERS_CSV_KEYS['name']
    gender = VOTERS_CSV_KEYS['gender']
    dob = VOTERS_CSV_KEYS['age']
    df.dropna(subset=[phone], inplace=True)
    stmts = []
    for index, row in df.iterrows():
        age = isolate_age(row[dob])
        s = insert_voter_stmt(row[name], age, row[gender], row[phone])
        stmts.append(s)
    return add_voters(stmts)

def get_one_number():
    try:
        conn = sqlite3.connect(DBNAME)
        stmt = "select * from voters WHERE status = 'y' LIMIT 1;"
        cursor = conn.execute(stmt)
        dic = {}
        for row in cursor:
            dic["name"] = row[0]
            dic["age"] = row[1]
            dic["gender"] = row[2]
            dic["phone"] = row[3]
        #stmt = "UPDATE voters SET status = 'n' WHERE status = 'y' and phone = '" + dic["phone"] + "';"
        #conn.execute(stmt)
        #conn.commit()
        conn.close()
        return dic
    except Exception as e:
        return False
    
        

    