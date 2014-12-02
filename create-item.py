import time, csv, sys, os, urllib, urllib2, json, httplib, ssl

def main():
    #token = doAppLogin()
    addItem('HecFWeGHaZm28PKPU_eLIWbcsdFiNhHwXNgk0Ltnc3WHeZ-Zh69c7Dqx9T4lMt4rlsW554yuNm5RMGJHZczPrUi4Wr7Uve0bhwkbh1F9gskCG5XM445Y5YsPETF46hO24gOFr_RGJFm7fZRExxjsaneaJS7fsFu7UJxX2nXdnyb6G7Vl_hNn5109JNsGudZ2')
    print "....done...."

def registerApplication(item,token):
    params = {}
    params['itemId'] = item
    params['appType'] = 'multiple'
    params['redirect_uris'] = []
    params['f'] = 'json'
    params['token'] = token
    params = urllib.urlencode(params)  
    try:
        request = urllib2.Request('https://www.arcgis.com/sharing/oauth2/registerApp',params)
        response = urllib2.urlopen(request)
        response = response.read()
        print response
        response = json.loads(response)  
        client_id = response["client_id"]
        client_secret = response["client_secret"]
        print "client id: " + client_id
        print "client secret: " + client_secret
    except Exception:
        print "register app request failed"
        pass

def addItem(token):
    params = {}
    params['title'] = "Power Biking Application"
    params['tags'] = "Health,Productivity,Music"
    params['type'] = "Application"
    params['description'] = "My Cool Power Biking App"
    params['access'] = "public"
    params['f'] = "json"
    params['token'] = token
    params = urllib.urlencode(params)  
    try:
        request = urllib2.Request('https://www.arcgis.com/sharing/rest/content/users/doogle_startups/addItem',params)
        response = urllib2.urlopen(request)
        response = response.read()
        print response
        response = json.loads(response)  
        item_id = response["id"]
        print "item id: " + item_id
        registerApplication(item_id, token)
    except Exception:
        print "addItem request failed"
        pass
           
def doAppLogin():
    params = {}
    params['client_id'] = "FQDSnKQxxjVG7c4o"
    params['client_secret'] = "bdf7fffa88f84d2abbc343a7097daf58"
    params['grant_type'] = "client_credentials"
    params = urllib.urlencode(params)  
    try:
        request = urllib2.Request('https://www.arcgis.com/sharing/oauth2/token/',params)
        response = urllib2.urlopen(request)
        response = response.read()
        response = json.loads(response)  
        token = response["access_token"]
        print token
    except Exception:
        pass        
        
if __name__ == "__main__":
    main()