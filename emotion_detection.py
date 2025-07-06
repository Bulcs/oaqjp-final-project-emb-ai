import requests
import json

def get_dominant_emotion(emotion_dict):
    """
    Determina a emoção dominante baseada nos scores das emoções
    """
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    max_score = 0
    dominant_emotion = ''
    
    for emotion in emotions:
        if emotion in emotion_dict and emotion_dict[emotion] > max_score:
            max_score = emotion_dict[emotion]
            dominant_emotion = emotion
    
    return dominant_emotion

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) 
    dict_response = response.json()
    
    if response.status_code == 400:
        all_emotions_resp = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    } 
    else:
        emotion_data = dict_response['emotionPredictions'][0]['emotion']
        
        all_emotions_resp = {
            'anger': emotion_data['anger'],
            'disgust': emotion_data['disgust'],
            'fear': emotion_data['fear'],
            'joy': emotion_data['joy'],
            'sadness': emotion_data['sadness'],
            'dominant_emotion': get_dominant_emotion(emotion_data)
        }    
    
    return all_emotions_resp