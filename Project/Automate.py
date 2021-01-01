#import pywhatkit as pk
import time
from datetime import datetime, date, timedelta
import requests
import urllib
def Reminders():
    file_url='https://drive.google.com/uc?export=download&id=16H7gT0fdbbIk1N_StEH1UZ1WMdimSc9X'
    todo_list=[]
    file = urllib.request.urlopen(file_url)
    for line in file:
        decoded_line = line.decode("utf-8")
        todo_list.append(decoded_line.rstrip('\r\n').split(': '))

    today_message="=>Important Deadlines/Reminders for today\n\n"
    tomorrow_message="=>Important Deadlines/Reminders for tomorrow\n\n"
    today=datetime.now()
    tomorrow=datetime.now()+timedelta(days=1)#timedelta(days=1)
   
    today=today.strftime('%d-%m-%Y')
    tomorrow=tomorrow.strftime('%d-%m-%Y')
    print(today)
    print(tomorrow)
    exp_date=""
    for item in todo_list:
        exp_date=datetime.strptime(item[1],'%d-%m-%Y').strftime('%d-%m-%Y')
        if(exp_date==today):
            today_message+=' '.join(item)+"\n"
        elif(exp_date==tomorrow):
            tomorrow_message+=' '.join(item)+"\n"
            
   
    if(today_message!="=>Important Deadlines/Reminders for today\n\n"):
        today_message+="_________________________________________\n"
        url1 = f"https://api.callmebot.com/whatsapp.php?phone=+923065492015&text={today_message}&apikey=698276"
        r1 = requests.get(url1)
        print(r1)

    time.sleep(20)

    if(tomorrow_message!="=>Important Deadlines/Reminders for tomorrow\n\n"):
        tomorrow_message+="_________________________________________\n"
        url2 = f"https://api.callmebot.com/whatsapp.php?phone=+923065492015&text={tomorrow_message}&apikey=698276"
        r2 = requests.get(url2)
        print(r2)
    #pk.sendwhatmsg('+923005154602','hello created a bot',dt.datetime.now().hour,(dt.datetime.now().minute)+1)
    file.close()

Reminders()