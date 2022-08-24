#// Don't forget to hit SUBSCRIBE, COMMENT, LIKE, SHARE! and LEARN... :)
# But srsly, hit that sub button so you don't miss out on more content! 

'''imports'''
import requests
import time
import threading

''' INPUT USERNMAE TO DOX '''
username = input('\033[92m{+} Enter username to DOX: ')


# INSTAGRAM
instagram = f'https://www.instagram.com/{username}'

# FACEBOOK
facebook = f'https://www.facebook.com/{username}'

#TWITTER
twitter = f'https://www.twitter.com/{username}'

# YOUTUBE
youtube = f'https://www.youtube.com/{username}'

# BLOGGER
blogger = f'https://{username}.blogspot.com'

# GOOGLE+
google_plus = f'https://plus.google.com/s/{username}/top'

# REDDIT
reddit = f'https://www.reddit.com/user/{username}'

# WORDPRESS
wordpress = f'https://{username}.wordpress.com'

# PINTEREST
pinterest = f'https://www.pinterest.com/{username}'

# GITHUB
github = f'https://www.github.com/{username}'

# TUMBLR
tumblr = f'https://{username}.tumblr.com'

# FLICKR
flickr = f'https://www.flickr.com/people/{username}'

# STEAM
steam = f'https://steamcommunity.com/id/{username}'

# VIMEO
vimeo = f'https://vimeo.com/{username}'

# SOUNDCLOUD
soundcloud = f'https://soundcloud.com/{username}'

# DISQUS
disqus = f'https://disqus.com/by/{username}'

# MEDIUM
medium = f'https://medium.com/@{username}'

# DEVIANTART
deviantart = f'https://{username}.deviantart.com'

# VK
vk = f'https://vk.com/{username}'

# ABOUT.ME
aboutme = f'https://about.me/{username}'

# IMGUR
imgur = f'https://imgur.com/user/{username}'

# FLIPBOARD
flipboard = f'https://flipboard.com/@{username}'

# SLIDESHARE
slideshare = f'https://slideshare.net/{username}'

# FOTOLOG
fotolog = f'https://fotolog.com/{username}'

# SPOTIFY
spotify = f'https://open.spotify.com/user/{username}'

# MIXCLOUD
mixcloud = f'https://www.mixcloud.com/{username}'

# SCRIBD
scribd = f'https://www.scribd.com/{username}'

# BADOO
badoo = f'https://www.badoo.com/en/{username}'

# PATREON
patreon = f'https://www.patreon.com/{username}'

# BITBUCKET
bitbucket = f'https://bitbucket.org/{username}'

# DAILYMOTION
dailymotion = f'https://www.dailymotion.com/{username}'

# ETSY
etsy = f'https://www.etsy.com/shop/{username}'

# CASHME
cashme = f'https://cash.me/{username}'

# BEHANCE
behance = f'https://www.behance.net/{username}'

# GOODREADS
goodreads = f'https://www.goodreads.com/{username}'

# INSTRUCTABLES
instructables = f'https://www.instructables.com/member/{username}'

# KEYBASE
keybase = f'https://keybase.io/{username}'

# KONGREGATE
kongregate = f'https://kongregate.com/accounts/{username}'

# LIVEJOURNAL
livejournal = f'https://{username}.livejournal.com'

# ANGELLIST
angellist = f'https://angel.co/{username}'

# LAST.FM
last_fm = f'https://last.fm/user/{username}'

# DRIBBBLE
dribbble = f'https://dribbble.com/{username}'

# CODECADEMY
codecademy = f'https://www.codecademy.com/{username}'

# GRAVATAR
gravatar = f'https://en.gravatar.com/{username}'

# PASTEBIN
pastebin = f'https://pastebin.com/u/{username}'

# FOURSQUARE
foursquare = f'https://foursquare.com/{username}'

# ROBLOX
roblox = f'https://www.roblox.com/user.aspx?username={username}'

# GUMROAD
gumroad = f'https://www.gumroad.com/{username}'

# NEWSGROUND
newsground = f'https://{username}.newgrounds.com'

# WATTPAD
wattpad = f'https://www.wattpad.com/user/{username}'

# CANVA
canva = f'https://www.canva.com/{username}'

# CREATIVEMARKET
creative_market = f'https://creativemarket.com/{username}'

# TRAKT
trakt = f'https://www.trakt.tv/users/{username}'

# 500PX
five_hundred_px = f'https://500px.com/{username}'

# BUZZFEED
buzzfeed = f'https://buzzfeed.com/{username}'

# TRIPADVISOR
tripadvisor = f'https://tripadvisor.com/members/{username}'

# HUBPAGES
hubpages = f'https://{username}.hubpages.com'

# CONTENTLY
contently = f'https://{username}.contently.com'

# HOUZZ
houzz = f'https://houzz.com/user/{username}'

#BLIP.FM
blipfm = f'https://blip.fm/{username}'

# WIKIPEDIA
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

# HACKERNEWS
hackernews = f'https://news.ycombinator.com/user?id={username}'

# CODEMENTOR
codementor = f'https://www.codementor.io/{username}'

# REVERBNATION
reverb_nation = f'https://www.reverbnation.com/{username}'

# DESIGNSPIRATION
designspiration = f'https://www.designspiration.net/{username}'

# BANDCAMP
bandcamp = f'https://www.bandcamp.com/{username}'

# COLOURLOVERS
colourlovers = f'https://www.colourlovers.com/love/{username}'

# IFTTT
ifttt = f'https://www.ifttt.com/p/{username}'

# EBAY
ebay = f'https://www.ebay.com/usr/{username}'

# SLACK
slack = f'https://{username}.slack.com'

# OKCUPID
okcupid = f'https://www.okcupid.com/profile/{username}'

# TRIP
trip = f'https://www.trip.skyscanner.com/user/{username}'

# ELLO
ello = f'https://ello.co/{username}'

# TRACKY
tracky = f'https://tracky.com/user/~{username}'

# BASECAMP
basecamp = f'https://{username}.basecamphq.com/login'


''' WEBSITE LIST - USE FOR SEARCHING OF USERNAME '''
WEBSITES = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
]


''' COLOUR PRINTING FUNCTION '''
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function


''' COLOUR PRINTS '''
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')


''' BANNER '''
def banner():
    YELLOW(r'''
  _                 _    _                      
 | |               | |  (_)                     
 | |     ___   ___ | | ___ _ __   __ _   ______ 
 | |    / _ \ / _ \| |/ / | '_ \ / _` | |______|
 | |___| (_) | (_) |   <| | | | | (_| |         
 |______\___/ \___/|_|\_\_|_| |_|\__, |         
                                  __/ |         
                                 |___/          
   _____ _                      __   ___   ___  
  / ____| |                    /_ | / _ \ / _ \ 
 | |  __| | __ _ ___ ___  __   _| || | | | | | |
 | | |_ | |/ _` / __/ __| \ \ / / || | | | | | |
 | |__| | | (_| \__ \__ \  \ V /| || |_| | |_| |
  \_____|_|\__,_|___/___/   \_/ |_(_)___/ \___/ 
  ''')


def search():
    GREEN(f'[+] Searching for username:{username}')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(0.5)

    GREEN(f'[+] Looking-Glass v1.00 is working\n')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(0.5)

    time.sleep(1)

    count = 0
    threads = []
    results = [False for i in range(len(WEBSITES))]
    for i in range(len(WEBSITES)):
        url = WEBSITES[i]
        def thread(results, index, url):
            try:
                r = requests.get(url, timeout=10)

                if r.status_code == 200:
                    YELLOW(f'\n{url} - {r.status_code} - OK')
                    if username.lower() in r.text.lower():
                        GREEN(f'POSITIVE MATCH: Username:{username} - text has been detected in url.')
                    else:
                        GREEN(f'POSITIVE MATCH: Username:{username} - \033[91mtext has NOT been detected in url, could be a FALSE POSITIVE.')#
                    results[index] = True
            except requests.exceptions.ConnectTimeout:
                RED(f'{url} - Connection Timeout')
            except Exception as e:
                RED(f'ERROR checking {url} - {e}')
            
        t = threading.Thread(target=thread, args=(results, i, url))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    
    for i in range(len(results)):
        if results[i]:
            count += 1
    

    total = len(WEBSITES)
    GREEN(f'FINISHED: A total of {count} MATCHES found out of {total} websites.')



if __name__=='__main__':
    banner()
    search()
