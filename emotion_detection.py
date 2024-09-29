import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    req_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = req_json, headers = headers)
    resp_json = json.loads(response.text)
    resp_body = resp_json['emotionPredictions'][0]['emotion']
    most_dominant = 0
    for emotion in list(resp_body.keys()):
        if resp_body[emotion] > most_dominant:
            most_dominant = resp_body[emotion]
            resp_body['dominant_emotion'] = emotion
    return resp_body
