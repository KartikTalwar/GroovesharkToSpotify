import json
import urllib
import grooveshark
from pprint import pprint as pp


def getTrack(query):
    url = "http://ws.spotify.com/search/1/track.json?q=" + urllib.quote(query)
    get = json.load(urllib.urlopen(url))
    res = []

    try:
        res.append(get['tracks'][0]['name'])
        res.append(get['tracks'][0]['artists'][0]['name'])
    except IndexError:
        return res

    return res



gs = grooveshark.init()
call  = grooveshark.api_call('getPlaylistSongs', {'playlistID': '80199741'})
songs = call['result']['songs']
slist = map(lambda x:  [x['SongName'], x['ArtistName']],songs)


for i in slist:
    q = ' '.join(i[::]).encode('ascii', 'ignore')
    print q
    if '(' in i[0] or '[' in i[0]:
        q = i[0].encode('ascii', 'ignore')
    gt = getTrack(q)
    if len(gt) > 0:
        a,b = gt
        print "%s  %s" % (a,b)
        print "\n"
    else:
        print '..'

