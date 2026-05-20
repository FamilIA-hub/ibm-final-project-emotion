import requests, json
   
def emotion_detector(text_to_analyze):
    '''
    Uses Watson IBM emotion AI tool or detecting emtions in texts.
    Parameter: text_to_analyze being the text the user puts on the website.
    Output as text.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #url of the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #Headers required for the API request
    myobj = { "raw_document": { "text": text_to_analyze } }
    #Creates a dictionary with the text provided.
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    #Extract the scores for each emotion from the dictionary in the list
    emotions = {
        'anger' : anger_score,
        'disgust' : disgust_score,
        'fear' : fear_score,
        'joy' : joy_score,
        'sadness' : sadness_score
    }
    #create a dictionary with the emotions and the scores
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    #find the highest score and add the emotion as a new value in the dictionary
    return emotions

