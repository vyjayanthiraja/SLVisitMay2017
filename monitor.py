import http.client, urllib.request, urllib.parse, json

def getTags(response):
    response = response.decode('utf8')
    jsonString = json.loads(response)
    tagList = jsonString["tags"]
    tags = []
    for t in tagList:
        tags.append(t["name"])
    return tags

def analyzeImage(imageFileName):
    headers = {
        'Content-Type':'application/octet-stream',
        'Ocp-Apim-Subscription-Key':'!!!TOBEREPLACED!!!',
    }

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
        data = response.read()
        conn.close()
        return getTags(data)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

image = 'Koala_climbing_tree.jpg'
print(analyzeImage(image))


