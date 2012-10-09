import json, dbus, urllib, sys, os

def get_spotify_dbus():
    try:
        spotify = dbus.SessionBus().get_object('com.spotify.qt', '/')
    except:
        print>>sys.stderr, "Spotify is not running."
        sys.exit(1)
    return spotify

def lookup_spotify(query):
    url = "http://ws.spotify.com/search/1/track.json?q=" + urllib.quote(query)
    response = json.load(urllib.urlopen(url))

    try:
        track = response['tracks'][0]
    except IndexError:
        return

    return track

def play():
    query = ' '.join(sys.argv[1:])
    if not query:
        print>>sys.stderr, "Usage: %s [song - artist]" % os.path.basename(sys.argv[0])

    else:
        if query.startswith("spotify:"):
            get_spotify_dbus().OpenUri(query)
            return

        track = lookup_spotify(query)
        if track:
            href = track['href']
            print "Playing %s - %s (%s)" % (', '.join(a['name'] for a in track['artists']), track['name'], href)
            get_spotify_dbus().OpenUri(href)

        else:
            print >>sys.stderr, "Could not find %s" % query
            sys.exit(1)

def pause():
    if '-h' in sys.argv:
        print >>sys.stderr, "%s: issues play/pause to spotify." % (os.path.basename(sys.argv[0]))
    else:
        get_spotify_dbus().PlayPause()

def info():
    if '-h' in sys.argv:
        print >>sys.stderr, "%s: shows what's currently playing on spotify." % (os.path.basename(sys.argv[0]))
    else:
        meta = get_spotify_dbus().GetMetadata()
        print "Now playing: %s - %s (%s)" % (
            ' ,'.join(meta['xesam:artist']), meta['xesam:title'], meta['xesam:url']
        )

