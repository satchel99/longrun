class Message:
    def __init__(self,name=None,num=None,body=None,date=None):
        self.name = name
        self.num = num
        self.body = body
        self.date = date
    def addDate(self, date=None):
        self.date = date
    def __str__(self):
        return "Name: " + self.name + " Number: " + self.num + " Date: " + self.date + "\n" + "Body: " + self.body