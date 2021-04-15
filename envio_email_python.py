import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#criacao de um objeto mensagem
msg = MIMEMultipart()
login_email = str(input('Digite seu email: ')) #email_exemple: emailtesteempreendedor@gmail.com
senha_email = str(input('Digite sua senha: ')) #senha_exemple: empreendedor1234 
destinatario = 'emailtesteempreendedor@gmail.com'
assunto = 'Envio de email com python!'
texto = str(input(f'Digite um texto aleatorio que deseje enviar para {destinatario}'))

# parametros
msg['From'] = login_email
msg['To'] = destinatario
msg['Subject'] = assunto

#criacao do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criacao do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#login na conta para efetuar o envio
server.login(login_email, senha_email)
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')