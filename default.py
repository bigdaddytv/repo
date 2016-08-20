import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin,base64
pipcan = base64.b64decode
PLUGIN=pipcan('cGx1Z2luLnZpZGVvLmJpZ2RhZGR5dHY=')
reason = xbmcaddon.Addon(id=PLUGIN)
singer = reason.getSetting(pipcan('dXNlcm5hbWU='))
lighter = reason.getSetting(pipcan('cGFzc3dvcmQ='))
active = reason.getSetting(pipcan('YWN0aXZl'))
view = reason.getSetting(pipcan('dmlldw=='))
dialog = xbmcgui.Dialog()
def noway():
            nosee('Live',pipcan('cmFuZG9t'),8,pipcan('aHR0cDovL3RhcmdldGJ1aWxkcy5uZXQvaWNvbnMvbGl2ZSUyMGhkLnBuZw=='),pipcan('aHR0cDovL3RhcmdldGJ1aWxkcy5uZXQvaWNvbnMvbGl2ZSUyMGhkLnBuZw=='),'')
            nosee('No Guide',pipcan('cmFuZG9t'),7,pipcan('aHR0cDovL3RhcmdldGJ1aWxkcy5uZXQvaWNvbnMvbGl2ZSUyMGhkLnBuZw=='),pipcan('aHR0cDovL3RhcmdldGJ1aWxkcy5uZXQvaWNvbnMvbGl2ZSUyMGhkLnBuZw=='),'')
            url = pipcan('aHR0cDovL3JlYm9vdC5uczAxLmJpei9hZGRvbi92aWV3X2NhdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM=')%(singer,lighter)
            r = requests.get(url)
            monster = re.compile(pipcan('bmFtZSI6IiguKz8pIiwidXJsIjoiKC4rPykiLCJ0aHVtYiI6IiguKz8pIiwiZmFuYXJ0IjoiKC4rPykiLCJkZXNjcmlwdGlvbiI6IiguKz8pIg==')).findall(r.content)
            for pillow,url,thumb,fanart,description in monster:
                if 'Blocks' in pillow:
                    nosee(pillow,pipcan('aHR0cDovL3JlYm9vdC5uczAxLmJpei9hZGRvbi92aWV3LnBocD9wPTU2JnVzZXJuYW1lPSVzJnBhc3N3b3JkPSVz')%(singer,lighter),2,thumb,fanart,description)
                else:
                    nosee(pillow,url,1,thumb,fanart,description)
            grays(pipcan('UmFuZG9t'),pipcan('cmFuZG9t'),6,pipcan('aHR0cDovL3d3dy5oZWhlbWVtZS5jb20vaW1nL3JlZnJlc2gucG5n'),pipcan('aHR0cDovL3d3dy5oZWhlbWVtZS5jb20vaW1nL3JlZnJlc2gucG5n'),'')
            xbmcplugin.setContent(int(sys.argv[1]), pipcan('bW92aWVz'))
def livestream():
    url = 'http://192.99.232.176/addon/streamtest3.php?id=1'
    r = requests.get(url)
    match = re.compile('name":"(.+?)"id":"(.+?)"cat":"1"epg":"(.+?)"').findall(r.content)
    for name,url,listid in set(match):
        if listid == 'null':
            bonding('%s'%(name),pipcan('aHR0cDovL3JlYm9vdC5uczAxLmJpejo4MDAwL2xpdmUvJXMvJXMvJXMubTN1OA==')%(singer,lighter,url),3,'','','')
        else:
            listid = listid.replace('null','')
            getGuide(name,url,listid)
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
def getGuide(name,url,listid):
    r = requests.get('http://tvschedule.zap2it.com/tvlistings/ZCSGrid.do?stnNum=%s'%(listid))
    match = re.compile("<li class=\"zc-ssl-pg\" id=\"row1-1\".+?<a id=\"rowTitle1\" class=\"zc-ssl-pg-title\" href='http://tvlistings.zap2it.com/tv/.+?/(.+?)\?.+?>(.+?)<",re.DOTALL).findall(r.content)
    for fanart,now in set(match):
        fanart2 = ('https://services.timewarnercable.com/imageserver/program/%s?default=true&hight=600&width=1200')%(fanart)
        bonding('%s[/COLOR] - [COLOR white][I]%s[/I][/COLOR]'%(name,now),pipcan('aHR0cDovL3JlYm9vdC5uczAxLmJpejo4MDAwL2xpdmUvJXMvJXMvJXMubTN1OA==')%(singer,lighter,url),3,'http://localhost:52307/getpvrthumb&title=%s&fallback=%s'%(now,fanart),'http://localhost:52307/getpvrthumb&title=%s&fallback=%s'%(now,fanart),'')
def noguide():
    r = requests.get('http://192.99.232.176/addon/streamtest3.php?id=1')
    match = re.compile('name":"(.+?)"id":"(.+?)"cat":"\d"epg":"\d:(.+?):(.+?)"').findall(r.content)
    for  name,url,icon,epg in match:
        bonding(name,pipcan('aHR0cDovL3JlYm9vdC5uczAxLmJpejo4MDAwL2xpdmUvJXMvJXMvJXMubTN1OA==')%(singer,lighter,url),1,'http://%s'%icon,'','')
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
def usaguide():
    import calendar,datetime
    from time import mktime
    start = datetime.datetime.now()
    timer = mktime(start.timetuple())
    tm = int(timer)
    timer2 = '%s'%(tm)
    cat = '0'
    usaoffset=reason.getSetting(pipcan("dXNhb2Zmc2V0"))
    hehe = int(timer2) - int(usaoffset)
    qual=reason.getSetting(pipcan("cXVhbA=="))
    r = requests.get('http://192.99.232.176/addon/streamtest3.php?id=1')
    match = re.compile('name":"(.+?)"id":"(.+?)"cat":"\d"epg":"\d:(.+?):(.+?)"').findall(r.content)
    url2 = ('http://tvschedule.zap2it.com/tvlistings/ZCGrid.do?method=decideFwdForLineup&zipcode=28390&setMyPreference=false&lineupId=NC32401:X&aid=tvschedule&isDescriptionOn=true&fromTimeInMillis=%s&aid=tvschedule#now'%(hehe))
    r2 = requests.get(url2)
    for name,url,icon,epg in set(match):
        try:
            epg = epg.replace('null','')
            match2=re.compile('</a></span><span class="zc-st-c"><a class="zc-st-a" href="http://tvschedule\.zap2it\.com/tvlistings/ZCSGrid\.do\?stnNum=.+?&channel=(.+?)&aid=tvschedule">(.+?)</a></span>.+?tvschedule">(.+?)<.+?this,\'(.+?)\'.+?tvschedule">(.+?)</a>',re.DOTALL).findall(r2.content)
            for ids,no,channel,image,prog in set(match2):
                channel = channel.decode("utf-8", "ignore")
                channel = urllib2.unquote(channel)
                channel = channel.replace('&amp;','And').replace('&#039;','\'').replace('"','')
                fanart = ('https://services.timewarnercable.com/imageserver/program/%s?default=true&hight=600&width=800')%(image)
                if ids == epg:
                    bonding('%s [/COLOR][COLOR white][I][ %s ][/I][/COLOR]'%(name,channel),pipcan('aHR0cDovL3JlYm9vdC5uczAxLmJpejo4MDAwL2xpdmUvJXMvJXMvJXMubTN1OA==')%(singer,lighter,url),1,'http://%s'%icon,fanart,'')
        except:
            pass
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
    xbmcplugin.setContent(int(sys.argv[1]), pipcan('ZXBpc29kZXM='))
    xbmc.executebuiltin("Container.SetViewMode(%s)"%view)

def getjiggywithit():
        if active == 'true':
                    keyboard = xbmc.Keyboard('',pipcan('UGxlYXNlIEVudGVyIFVzZXJuYW1l'))
                    keyboard.doModal()
                    tecleado = keyboard.getText()
                    if tecleado == '':
                        exit()
                    reason.setSetting(pipcan('dXNlcm5hbWU='),tecleado)
                    keyboard2 = xbmc.Keyboard('',pipcan('UGxlYXNlIEVudGVyIHBhc3N3b3Jk'))
                    keyboard2.doModal()
                    tecleado2 = keyboard2.getText()
                    if tecleado2 == '':
                        exit()
                    reason.setSetting(pipcan('cGFzc3dvcmQ='),tecleado2)
                    url = (pipcan(('aHR0cDovL3JlYm9vdC5uczAxLmJpejo4MDAwL3BhbmVsX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM='))%(tecleado,tecleado2))
                    r = requests.get(url)
                    monster = re.compile(pipcan('eyJhdXRoIjooLis/KX0=')).findall(r.content)
                    for a in monster:
                        if a == pipcan('MA=='):
                            dialog = xbmcgui.Dialog()
                            reason.setSetting('active', 'true')
                            dialog.ok(pipcan('RXJyb3IgV29ybmcgVXNlci9QYXNzJywnU2VlbXMgWW91ciBQYXNzd29yZCBJcyBXcm9uZyBHbyBCYWNrIEFuZCBUcnkgQWdhaW4='))
                            exit()
                        if a == '1':
                            continue
                        else:
                            redbull()
        noway()
def redbull():
                    if singer == '':
                        exit()
                    url = (pipcan(('aHR0cDovL3JlYm9vdC5uczAxLmJpejo4MDAwL3BhbmVsX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXM='))%(singer,lighter))
                    r = requests.get(url)
                    monster = re.compile(pipcan('eyJyZWRidWxsIjooLis/KX0=')).findall(r.content)
                    for a in monster:
                        if a == '0':
                            dialog = xbmcgui.Dialog()
                            reason.setSetting(pipcan('YWN0aXZl'), 'true')
                            dialog.ok(pipcan('RXJyb3IgV3JvbmcgVXNlci9QYXNzJywnU2VlbXMgWW91ciBQYXNzd29yZCBJcyBXcm9uZyBHbyBCYWNrIEFuZCBUcnkgQWdhaW4='))
                            exit()
                        if a == '1':
                            continue
                        else:
                            break


def CAT(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        r = requests.get(url)
        monster = re.compile(pipcan('bmFtZSI6IiguKz8pIiwidXJsIjoiKC4rPykiLCJ0aHVtYiI6IiguKz8pIiwiZmFuYXJ0IjoiKC4rPykiLCJkZXNjcmlwdGlvbiI6IiguKz8pIg==')).findall(r.content)
        for pillow,url,thumb,fanart,description in monster:
            nosee(pillow,url,2,thumb,fanart,description)
        xbmcplugin.setContent(int(sys.argv[1]), pipcan('bW92aWVz'))
def CAT2(url):
        r = requests.get(url)
        monster = re.compile(pipcan('bmFtZSI6IiguKz8pIiwidXJsIjoiKC4rPykiLCJ0aHVtYiI6IiguKz8pIiwiZmFuYXJ0IjoiKC4rPykiLCJkZXNjcmlwdGlvbiI6IiguKz8pIg==')).findall(r.content)
        for pillow,url,fanart,thumb,description in monster:
           bonding(pipcan('JXM=')%pillow,url,3,thumb,fanart,description)
        xbmcplugin.setContent(int(sys.argv[1]),pipcan('bW92aWVz'))
def CAT3():
        url = pipcan('aHR0cDovL3JlYm9vdC5uczAxLmJpei9hZGRvbi9zZGYucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVz')%(singer,lighter)
        r = requests.get(url)
        monster = re.compile(pipcan('bmFtZSI6IiguKz8pIiwidGh1bWIiOiIoLis/KSIsInVybCI6IiguKz8pIg==')).findall(r.content)
        for pillow,thumb,url in monster:
            try:
                bonding(pillow,url,1,thumb,'','')
            except:
                pass
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )

def bonding(pillow,url,mode,iconimage,fanart,description):
        ok=True
        liz=xbmcgui.ListItem(pillow, iconImage=pipcan("RGVmYXVsdEZvbGRlci5wbmc="), thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": pillow, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        liz.addContextMenuItems(items=[], replaceItems=False)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok
def randoms():
    import random
    dp = xbmcgui.DialogProgress()
    r = random.randrange(0,12237)
    req = requests.get(pipcan('aHR0cDovLzE5Mi45OS4yMzIuMTc2L3JhbmRvbS5waHA/aWQ9JXM=')%(r))
    monster = re.compile(pipcan("JyguKz8pJy4rPycoLis/KSc=")).findall(req.content)
    dp.create(pipcan('U3RhcnQgUmFuZG9taXphdGlvbg=='))
    for pillow,url in monster:
        dp.update(20,'%s'%(pillow))
        hello(pipcan('aHR0cDovLzE5Mi45OS4yMzIuMTc2OjgwMDAvbW92aWUvJXMvJXMvJXM=')%(singer,lighter,url))
        dp.close()
def hello(url):
        url2 = url
        play=xbmc.Player()
        try:
            play.play(url)  
        except: pass 
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]  
        return param
def nosee(pillow,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&pillow="+urllib.quote_plus(pillow)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(pillow, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": pillow, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def grays(pillow,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&pillow="+urllib.quote_plus(pillow)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(pillow, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": pillow, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok            
params=get_params()
url=None
pillow=None
mode=None
iconimage=None
fanart=None
description=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        pillow=urllib.unquote_plus(params["pillow"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "pillow: "+str(pillow)

if mode==None or url==None or len(url)<1:
        print ""
        if singer == '':
            getjiggywithit()
            reason.setSetting('active', '2')
            xbmc.executebuiltin(pipcan("Q29udGFpbmVyLlJlZnJlc2g="))
        else:
            noway()
       
elif mode==1:
        CAT(url)
elif mode==2:
        CAT2(url)
elif mode==3:
        hello(url)
elif mode==4:
        search()
elif mode==5:
        CAT3()
elif mode==6:
        randoms()
elif mode==7:
        noguide()
elif mode==8:
        usaguide()
xbmcplugin.endOfDirectory(int(sys.argv[1]))