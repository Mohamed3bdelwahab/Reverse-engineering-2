# Decompiled from: Python 2.7.17 (default, Oct 23 2019, 08:28:22) 
import os, sys, time, requests, base64, json, re
from bs4 import BeautifulSoup

def banner():
    print '\x1b[92m\n       _                                _\n      | |            _                 (_)\n _ _ _| |__  _   _ _| |_    _____ ____  _ ____  _____\n| | | |  _ \\| | | (_   _)  (____ |  _ \\| |    \\| ___ |\n| | | | | | | |_| | | |_   / ___ | | | | | | | | ____|\n \\___/|_| |_|____/   \\__)  \\_____|_| |_|_|_|_|_|_____)\x1b[97m\n     \x1b[1;97msearch for all anime info using anime images\n                coded by @muh4k3mos\x1b[97m\n'


class main(object):

    def __init__(self, path):
        notif = '[\x1b[93m+\x1b[97m]'
        try:
            self.path = path
            self.image = open(path, 'rb').read()
            self.encode = base64.b64encode(self.image)
            url = 'https://trace.moe/api/search'
            self.data = {}
            self.post = json.loads(requests.post(url, data=self.data).text)
        except ValueError:
            sys.exit('info: no results from this photo were found or an error was unknown')
        except IOError:
            print 'info: no such file or directory: %s' % self.path
            sys.exit()
        else:
            print ''
            for result in self.post['docs']:
                print '[\x1b[92m*\x1b[97m] \x1b[94minformation about this photo\x1b[97m'
                print '    %s anime   : %s ' % (notif, str(result['title_romaji']) + ' (%s)' % result['title'])
                print '    %s episode : %s ' % (notif, result['episode'])
                print '    %s date season  : %s \n' % (notif, result['season'])
                break

            url = ('https://anilist.co/anime/{}').format(result['anilist_id'])
            self.anilist = requests.get(url).text
            soup = BeautifulSoup(self.anilist, 'html.parser')
            for anilist in soup.find_all('script'):
                self.json = json.loads(anilist.string)
                raw_result = self.json['mainEntity']
                break

            class info:
                synopsis = raw_result['description']
                startdate = raw_result['startDate']
                endate = raw_result['endDate']
                reviewCount = raw_result['aggregateRating']['reviewCount']
                bestRating = raw_result['aggregateRating']['bestRating']
                worstRating = raw_result['aggregateRating']['worstRating']
                ratingValue = raw_result['aggregateRating']['ratingValue']
                ratingCount = raw_result['aggregateRating']['ratingValue']
                countryOrigin = raw_result['countryOfOrigin']
                company = raw_result['productionCompany']
                actor = raw_result['actor']
                creator = raw_result['creator']
                director = raw_result['director']
                numEps = raw_result['numberOfEpisodes']
                genrenime = raw_result['genre']
                tag = raw_result['keywords']

            print '[\x1b[92m*\x1b[97m] \x1b[94minformation about this anime\x1b[97m'
            print '    %s genre : %s ' % (notif, (' ').join(info.genrenime))
            print '    %s tag keywords : %s ' % (notif, (' ').join(info.tag))
            print '    %s number of episode : %s ' % (notif, info.numEps)
            try:
                listname = []
                for name in info.actor:
                    listname.append(name['name'] + ',')

                print '    %s actor : %s ' % (notif, (' ').join(listname))
            except TypeError:
                print '    %s actor : %s ' % (notif, info.actor)
            else:
                try:
                    for name in info.director:
                        print '    %s director : %s ' % (notif, name['name'])
                        break

                except TypeError:
                    print '    %s director : %s ' % (notif, info.director)

            print '    %s country of origin : %s ' % (notif, info.countryOrigin)
            print '    %s start date production : %s' % (notif, info.startdate)
            print '    %s end of production date : %s' % (notif, info.endate)
            try:
                for name in info.company:
                    print '    %s production company : %s ' % (notif, name['name'])

            except TypeError:
                print '    %s production company : %s ' % (notif, info.company)

        print '    %s synopsis : %s \n' % (notif, info.synopsis)
        print '[\x1b[92m*\x1b[97m] \x1b[94mabout rating\x1b[97m'
        print '    %s riview count : %s ' % (notif, info.reviewCount)
        print '    %s best rating  : %s ' % (notif, info.bestRating)
        print '    %s worst rating : %s ' % (notif, info.worstRating)
        print '    %s rating value : %s ' % (notif, info.ratingValue)
        print '    %s rating count : %s \n' % (notif, info.ratingCount)


if __name__ == '__main__':
    os.system('clear')
    banner()
    path = raw_input('[*] enter the image path : ')
    if path == '':
        sys.exit('info: enter the anime image path you want to search')
    main(path)
