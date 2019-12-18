from firebase import firebase
from hashlib import sha256
firebase = firebase.FirebaseApplication('https://lolautoclient-b815d.firebaseio.com/', None)

pw_ = sha256(str('654321').encode('utf-8')).hexdigest()

data = {
    'Name':'Andrej',
    'pw':pw_,
    'Command': 'None'
}

#ADD DATA
#dataid = firebase.post('/lolautoclient-b815d/Users', data)
#print(dataid)

#GET DATA
getdata = firebase.get('/lolautoclient-b815d/Users','')
#print(getdata)

for accs in getdata:
    if getdata[accs]['Name'] == 'Diima':
        print(getdata[accs]['pw'])

#CHANGE DATA                                    (User ID)
#firebase.put('/lolautoclient-b815d/Users/-LwLQEj5rM5KmijQbWOr', 'Command', '(SG)(Lane1:TOP)(Lane2:MID)(Champ:QIYANA)(BANN:ZED)')
#print('ID Updated')

#DELETE DATA
#firebase.delete('/lolautoclient-b815d/Users', '-LwLM4e2bGFbDlW0WvPW')


#Dima -LwLQ2GiETX16EYX5Q5-
#Andrej -LwLQEj5rM5KmijQbWOr
