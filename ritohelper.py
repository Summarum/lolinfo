import sys
import json
from urllib2 import urlopen
riotKey = 'RGAPI-EAFA68C5-28DC-4BCB-835A-66DEAFE6427E'
apiURL = urlopen('https://'+sys.argv[1]+'.api.pvp.net/api/lol/'+sys.argv[1]+'/v1.4/summoner/by-name/'+sys.argv[2]+'?api_key='+riotKey)
rawJSON = apiURL.read()
convertedJSON=json.loads(rawJSON)
value = convertedJSON['summarum']['id']


print value
