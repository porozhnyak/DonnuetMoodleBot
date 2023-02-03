from scriptshedule import CreatSheduleTimes
import datetime




# CreatSheduleTimes.monday()

def article():
    id = int(str(datetime.datetime.today().isoweekday())+str(datetime.datetime.today().strftime('%H%M')))
    print(id)

id = article() 

