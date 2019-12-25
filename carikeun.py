# MENTOL 
# At:Wed Dec 25 02:37:22 2019 

import requests
from bs4 import BeautifulSoup
import re, sys, time
reload(sys)
sys.setdefaultencoding('utf-8')

def banner():
    print "\x1b[94m _                                 _                      _\n| | ____ _ _ __ ___  _   _ ___  __| | __ _  ___ _ __ __ _| |__\n| |/ / _` | '_ ` _ \\| | | / __|/ _` |/ _` |/ _ \\ '__/ _`  '_  \\\n|   < (_| | | | | | | |_| \\__ \\ (_| | (_| |  __/ | | (_| | | | |\n|_|\\_\\__,_|_| |_| |_|\\__,_|___/\\__,_|\\__,_|\\___|_|  \\__,_|_| |_|\x1b[97m\n     scraped by Hero, btw author na gans #anjaymabar :V\n"


class main(object):

    def __init__(self):

        def result(url, ag):
            print '\n    \x1b[97m~ tunggu bentar ini lagi dicariin :) jan ngambek ya :D'
            pars = requests.get(url, headers=ag).text
            try:
                print '\n(\x1b[92m+\x1b[97m) \x1b[93mnah ketemu artinya\x1b[97m : %s ' % re.findall('</div>(.*?)<div', pars)[1]
            except IndexError:
                print '\n(\x1b[91m!\x1b[97m) yahhh gada beb hasil nya coba deh periksa kosakatamu'

            print '-' * 26

        self.agent = {}
        print '(\x1b[92m1\x1b[97m) dari bahasa indonesia ke bahasa daerah\n(\x1b[93m2\x1b[97m) dari bahasa daerah ke bahasa indonesia\n(\x1b[94m3\x1b[97m) tampilkan kode daerah'
        while True:
            self.select = input('\n    - pilih apa mau dipilihin nih wkwk : \x1b[92m')
            if self.select == 1:
                self.query = raw_input('\n\x1b[97m(\x1b[96m-\x1b[97m) masukin kosakata dari bhs indonesia nya euy :\x1b[92m ')
                self.ke = raw_input('\x1b[97m(\x1b[93m-\x1b[97m) pen ditranslate kemana? masukin kode daerah na beb : \x1b[92m')
                self.url = 'https://www.kamusdaerah.com/?bhs=a&bhs2=%s&q=%s' % (self.ke, self.query)
                result(self.url, self.agent)
            elif self.select == 2:
                self.query = raw_input('\n(\x1b[96m-\x1b[97m) masukin kosakata dari daerah kamu beb :v > \x1b[92m')
                self.ke = raw_input('\x1b[97m(\x1b[93m-\x1b[97m) kode daerah kamu? masukin euy : \x1b[92m')
                self.url = 'https://www.kamusdaerah.com/?bhs=%s&bhs2=a&q=%s' % (self.ke, self.query)
                result(self.url, self.agent)
            elif self.select == 3:
                print '\x1b[97m\n              indonesia = a\n              aceh = o\n              batak_angkola = p #mandailing\n              batak_karo = c\n              batak_toba = b\n              batak_simalungun = d\n              bali =\n              banjar = h\n              sunda = m\n              betawi = f\n              bugis = r\n              gayo = gy\n              jawa = i\n              lampung = s\n              lembak = lb    #bengkulu\n              makassar = j\n              minang = k    #padang\n              palembang = l\n              pontiakan = n'
            else:
                print '\x1b[97m(-) engga ada beb pilih 1/2 !1!1!1'


if __name__ == '__main__':
    banner()
    main()
