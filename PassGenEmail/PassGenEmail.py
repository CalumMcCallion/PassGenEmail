#Author Calum McCallion
#Created 24/02/22 -- dd/mm/yy


import os 
import smtplib
import random


pass_chars = 'randomcharacters' #type characters that you want to be shuffled

genPass = ''.join(random.sample(pass_chars, len(pass_chars))) #takes entered characters and shuffles them randomly


#This code was done so that I didnt have to enter in confidential details into script
EMAIL_ADDRESS = os.environ.get('EMAIL_USER') #Pulls my enviromental variable which stores my email 
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS') #Pulls my enviromental variable which stores my password


#=====================CODE FOR SENDING EMAIL=====================#
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo() #identify with server
    smtp.starttls() #encrypts traffic
    smtp.ehlo()#identifies as encrypted

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Generated Password For GitHub '
    body = genPass 

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'mccallioncalum@gmail.com', msg)

