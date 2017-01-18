import sys,os
import datetime

time = os.path.getmtime('file.txt')
while True:
    if (time != os.path.getmtime('file.txt')):
        with open('file.txt', 'r') as f:
            info = f.read()
            print ("Update: " + info)
            with open ('file.txt', 'w') as f:
                f.write('')
            with open('log.txt','a') as l:
                l.write(info+'  '+datetime.datetime.today().strftime("%Y-%m-%d %H:%M"+'\n'))
        time = os.path.getmtime('file.txt')
