import http.client, urllib.request, urllib.parse, json

# This function takes in an image file
# returns the emotions exhibited in this image
def getEmotion(imageFileName):
    params = urllib.parse.urlencode({
        })
    imageData = __getImageData(imageFileName)
    return __makeCognitiveApiRequest("/vision/v1.0/recognize?%s" % params, imageFileName)


# This function analyzes an image file and
# returns a list of tags for the image
def getImageTags(imageFileName):
    params = urllib.parse.urlencode({
        'visualFeatures': 'Tags',
        'language': 'en'
    })

    imageData = __getImageData(imageFileName)
    apiResponse = __makeCognitiveApiRequest("/vision/v1.0/analyze?%s" % params, imageData)
    jsonString = __parseJson(apiResponse)
    tagList = jsonString["tags"]
    tags = []
    for t in tagList:
        tags.append(t["name"])
    return tags 

# This function analyzes an image file and returns
# a sentence describing what it shows
def getDescription(imageFileName):
    imageData = __getImageData(imageFileName)
    apiResponse = __makeCognitiveApiRequest('/vision/v1.0/describe', imageData)
    jsonString = __parseJson(apiResponse)
    captions = jsonString["description"]["captions"]
    description = ""
    maxConfidence = 0
    for c in captions:
        if c["confidence"] > maxConfidence:
            description = c["text"]
            maxConfidence = c["confidence"]

    return description

def __parseJson(httpResponse):
    data = httpResponse.decode('utf8')
    return json.loads(data)

def __getImageData(imageFileName):
    f = open(imageFileName, "rb")
    body = f.read()
    f.close()
    return body

def __makeCognitiveApiRequest(relativeUri, body):
    headers = {
        'Content-Type':'application/octet-stream',
        'Ocp-Apim-Subscription-Key':'!!!TOBEREPLACED!!!',
    }
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", relativeUri, body, headers)
    response = conn.getresponse()
    if response.status >= 300:
        raise Exception(response.reason)
    data = response.read()
    conn.close()
    return data