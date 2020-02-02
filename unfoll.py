# At:Sun Feb  2 17:08:34 2020
import os, sys, urllib, json
if len(sys.argv) != 2:
    print 'Usage: python2 %s <access_token>' % sys.argv[0]
    quit()
os.system('clear')
putih = '\x1b[97m'
print putih + '\n           ,;:;;,\n          ;;;;;\n  .=\',    ;:;;:   \x1b[92m UNFOLLOW FACEBOOK\x1b[97m\n /_\', "=. \';:;:;\n @=:__,  \\,;:;:\' \x1b[92mCoded By \x1b[96m@IkbalCode\x1b[97m\n   _(\\.=  ;:;;\'  \x1b[96mhttps://t.me/ikbalcode\x1b[97m\n  `"_(  _/="`\n    `"\'``\n'
url = 'https://graph.facebook.com/v2.0/fql'
q = "SELECT target_id FROM connection WHERE source_id=me() AND is_following='true' AND target_type='user'"
access_token = sys.argv[1]
param = urllib.urlencode({})
response = urllib.urlopen(url + '?' + param)
data = json.load(response)
response.close()
if 'error' in data:
    print 'Error: ', data['error']['message']
    quit()
url = 'https://graph.facebook.com/v2.3'
count = 0
for ids in data['data']:
    for key, value in ids.iteritems():
        count += 1
        response = urllib.urlopen(url + '/' + value + '?fields=name&access_token=' + access_token)
        temp = json.load(response)
        response.close()
        for k, v in temp.iteritems():
            if k == 'error':
                print 'Account disabled'
                print 'id : ', value
                continue
            print k, ':', v

        print ''

print 'Total count: ', count
