from Message import Message
import DBUtils as ut
import SMSUtils as sms



def translatePhone(phone):
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")
    phone = phone.replace(" ", "")
    phone = phone.replace("%20", "")
    phone = phone.replace("-", "")
    return "+1" + phone

s = "(845) 287-3462"
m = Message("name", translatePhone(s), "Hey! This is Andrea. I’m a volunteer with Logan for 2nd Ward Alderman. This Tuesday, June 25th, there’s going to be a Democratic Primary Election and Logan needs your help! Logan’s fighting for Middletown to have a clean environment and move to 100% renewable energy, internet access for all, to protect our undocumented families, improve local infrastructure, and build affordable housing. The election is going to be close and every vote counts. Can Logan count on your vote?")
result = ut.get_one_number()
print(result)
