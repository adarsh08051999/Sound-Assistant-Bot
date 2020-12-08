import smtplib

def SendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587) #587 is port
    server.ehlo()
    server.starttls()

    file1 = open("pass.txt", "r")
    password=file1.readline() # save your email ids password in a txt file named pass.txt
    id='adarshagrawal4@gmail.com' # my email id change accordingly
    server.login(id,password)
    server.sendmail(id,to,content)
    server.close()
    file1.close()
