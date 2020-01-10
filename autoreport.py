# At:Sat Jan 11 01:36:46 2020
import sys, os, time, mechanize, cookielib
N = '\x1b[0m'
W = '\x1b[1;37m'
B = '\x1b[1;34m'
M = '\x1b[1;35m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
if len(sys.argv) == 4:
    pass
else:
    print '%sPenggunaan:\n%spython2 fb-autoreport.py <username> <sandi> <ID Target>' % (G, C)
    sys.exit()
print '%s[%sDEV%s] %s|| HeroBrinePE ||' % (G, W, G, W)

def report_init(minecraft):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_equiv(True)
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    browser.open('https://mbasic.facebook.com')
    browser.select_form(nr=0)
    browser.form['email'] = sys.argv[1]
    browser.form['pass'] = sys.argv[2]
    checking = browser.submit()
    if 'free.facebook.com' in checking.read():
        print '%s[%sINFO%s] %sLogin Berhasil Next...' % (G, W, G, W)
    else:
        print '%s[%sERR%s] %sLogin Gagal Exiting..' % (G, W, G, W)
        sys.exit()
    browser.open('https://free.facebook.com/mbasic/more/?owner_id=' + sys.argv[3])
    browser.follow_link(text='Beri masukan atau laporkan profil ini')
    browser.select_form(nr=0)
    browser.form['tag'] = [minecraft]
    print '%s[%sINFO%s] %sSukses Melaporkan %s Dengan Alasan Postingan Pelecehan' % (G, W, G, W, sys.argv[3])
    browser.submit()
    browser.follow_link(text='Selesai')
    print '%s[%sURL%s] %s%s' % (G, W, G, Y, browser.geturl())
    browser.close()
    print '%s\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94\xe2\x80\x94' % R


while True:
    report_init('profile_posting_inappropriate_things')

