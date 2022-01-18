import requests
import json
import os
import platform

print('Welcome to requesting in python. Do you want to continue or not? (y/n)')

op = input('Option: ')

if op == 'y':
    pass
elif op == 'n':
    exit()

#Have to work on this
def generate_report(url):
    websitefuncone = requests.get(url)
    print('Report\n=======\nStatus Code: ', websitefuncone.status_code, '\nURL: ', url)
    

while True:
    #The input
    cmd = input('$ ')

    #If - Elif parts
    if cmd == '':
        pass
    elif cmd == 'website report':
        url = input('Website: ')
        generate_report(url)
    elif cmd == 'status website':
        url2 = input('URL: ')
        urlstatus = requests.get(url2)
        print(url2, 'Status code received as: <', urlstatus.status_code, '>')
    elif cmd == 'get encoding website':
        urlencode = input('URL: ')
        urlreget = requests.get(urlencode)
        print('Encoding:' , urlreget.encoding)
    elif cmd == 'website html content':
        urlrete = input('URL: ')
        urlretex = requests.get(urlrete)
        with open('website-content.txt', 'w') as f:
            f.write(urlretex.text)
        print('Successfully inserted code into website-content.txt!!')
    elif cmd == 'clear website-content.txt':
        with open('website-content.txt', 'w') as f:
            f.write('')
    elif cmd == 'post website data':
        urldatapore = input('URL: ')
        datatopost = input('The JSON: ')
        timeoutpost = float(input('Timeout: '))
        urldataporeq = requests.get(urldatapore, data=datatopost, timeout=timeoutpost)
    elif cmd == 'delete website request':
        delreurl = input('URL: ')
        delereurl = requests.delete(delreurl)
        print('Deleted ', delreurl)
    elif cmd == 'operating system info':
        print('Platform: ', platform.system(), '\nLatest release: ', platform.release(), '\nDetailed Info On Operating System: ', platform.platform(), '\nVersion: ', platform.system() + ' ' + platform.release())
    elif cmd == 'exit':
        exit()
    else:
        print('Error found at: \n', cmd, '\nNo such command found.')
