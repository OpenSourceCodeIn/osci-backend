import email
import smtplib
urlfmt = 'http://localhost:5000/student/{NAME}/verify?code={CODE}'
subject = 'Your ReCodeIn Account'
fromaddr = 'rci@chausie'
def send(name, code, toaddr):
    msg = email.message.EmailMessage()
    msg.set_content(urlfmt.replace('{NAME}', name).replace('{CODE}', code))
    msg['Subject'] = subject
    msg['To'] = toaddr
    msg['From'] = fromaddr
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
