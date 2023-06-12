import smtplib
import datetime
import time, schedule
from fastapi import FastAPI

from email.mime.multipart import MIMEMultipart  # for creating email template part to from etc
from email.mime.text import MIMEText  # for creating body text, and

app = FastAPI()

birthday_dict = {
    "Linga@fangtechnologies.com":"2002-06-11",
    "sai.thatiguntla@fangtechnologies.com": "2002-06-13",
    "saireddy2k2@gmail.com": "2001-02-24",
    "saikumarreddythatiguntla@gmail.com": "2001-03-24",
    "thatiguntlasaikumarreddy@gmail.com": "2001-03-24",
}
"""
birthday_dic = {
"sai.thatiguntla@fangtechnologies.com": "2002-05-15",
"bhavana.nagella@fangtechnologies.com" : "2002-07-28", 
"narasimhulu.chinta@fangtechnologies.com" : "2001-02-24",
"aswini.malli@fangtechnologies.com" : "2002-07-15",
"sumanth.yaddanapudi@fangtechnologies.com":"2002-08-28",
"priyanka.nersupalli@fangtechnologies.com":"2003-03-16",
"gunasekhar.neeluri@fangtechnologies.com": "2003-11-30",
"naveen.dasari@fangtechnologies.com": "2002-01-06",
"ganesh.nallabapineni@fangtechnologies.com" : "2002-07-09",
"mounika.kattubadi@fangtechnologies.com": "2002-10-20",
"sravani.g@fangtechnologies.com":"2003-05-25",
"Linga@fangtechnologies.com":"1994-07-15",
"Hemanth.Surimani@fangtechnologies.com":"1997-07-05",
"PraveenSai.Kallepalli@fangtechnologies.com":"1997-10-02",
"jayaprakash.d@fangtechnologies.com":"1995-08-11",
"BhavyaBindu.Metla@fangtechnologies.com":"1998-06-11",
"Yamini.Sannapaneni@fangtechnologies.com":"1997-11-30",
"Amulya.Manukonda@fangtechnologies.com" :"1997-07-02",
"tirupathaiah.galla@fangtechnologies.com": "1995-03-06"
}
"""

gmail_user = 'sai.thatiguntla@fangtechnologies.com'  # enter your mail
gmail_password = 'uyofygjfqmclyqnu'  # here use google app pasword

sent_from = gmail_user
to = []
birthdays = []

tommorow = str(datetime.date.today() + datetime.timedelta(days=1))
print(tommorow)
for key in birthday_dict:
    if birthday_dict[key][6:] == tommorow[6:]:
        birthdays.append(key)
    else:
        to.append(key)

birthdayPersons = [item[:-21] for item in birthdays]

birthdaystring = ','.join(birthdayPersons)
Body = f"Hey Fangie, \n \t  Just a reminder that {birthdaystring}'s birthday is tomorrow!\n Don't forget to wish them a happy birthday!\n\nBest regards,\n Fang Technologies "
print(Body)


@app.get("/birthday-function")
async def checkBdays():
    if len(birthdays) != 0:
        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()

            smtp_server.login(gmail_user, gmail_password)
            msg = MIMEMultipart()  # msg object that stores to, from and other data
            msg['From'] = sent_from
            msg['To'] = ",".join(to)

            msg['Subject'] = "Birthday Remainder !!!"
            Body = f"Hi all, \n \t  Just a friendly reminder that {birthdaystring}'s birthday is tomorrow! Don't forget to wish them a happy birthday!\n\nBest regards,\n Fang Technologies "
            msg.attach(MIMEText(Body, 'plain'))

            smtp_server.send_message(msg)
            smtp_server.close()
            return {"message": "Email sent successfully!"}


        except Exception as ex:
            return {ex: "Something went wrong…."}
        schedule.every().day.at("19:13").do(checkBdays)

        while True:
            schedule.run_pending()
            time.sleep(1)




# print("sending mail")
# send_email()


"""
import smtplib
from email.mime.multipart import MIMEMultipart  #for creating email template part to from etc
from email.mime.text import MIMEText  #for creating body text, and
from fastapi import FastAPI

//gmail_user = 'saikumarreddyt2k2@gmail.com'  #enter your mail
gmail_password = 'pmbsyuelmfezitcu' # here use google app password(under 2 step verfication)

sent_from = gmail_user
to = 'lgm.cse94@gmail.com'
# subject = 'subject of the mail'
# body = 'hi  good mrng , i need a leave..!'

# email_text =Subject: %s %s  % ( subject, body))
# print(email_text)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
   
    smtp_server.login(gmail_user, gmail_password)
    msg = MIMEMultipart()     #msg object that stores to, from and other data
    msg['From']=sent_from
    msg['To']=to
    msg['Subject']="requesting leave reg."
    Body = "i need a leave for 2 days !"
    msg.attach(MIMEText(Body, 'plain'))
    
    smtp_server.send_message(msg)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
"""
