import http.client, urllib.request, urllib.parse, json

headers = {
        'Content-Type':'application/octet-stream',
        'Ocp-Apim-Subscription-Key':'!!!TOBEREPLACED!!!',
}

def getEmotion(imageFileName):
    params = urllib.parse.urlencode({
        })
    f = open(imageFileName, "rb")
    body = f.read()
    f.close()
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print(e.args)


# This function takes in an image file and
# returns a list of tags for the image
def getImageTags(imageFileName):
    params = urllib.parse.urlencode({
        'visualFeatures': 'Tags',
        'language': 'en'
    })

    f = open(imageFileName, "rb")
    body = f.read()
    f.close()
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read().decode('utf8')
        conn.close()
        jsonString = json.loads(response)
        tagList = jsonString["tags"]
        tags = []
        for t in tagList:
            tags.append(t["name"])
        return tags 
    except Exception as e:
        print(e.args)
        return []
