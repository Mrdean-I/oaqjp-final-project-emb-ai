""" Emotion detection:
this module provides a function for analyzing emotion in text
using the Watson NLP EmotionPredict API header and json object provided """

import json
import requests

def emotion_detector(text_to_analyze):
    """ Detect emotions in the provided text.
    Args:
      text_to_analyze (str): the text to analyze
    Returns:
      dict: the emotion prediction results from the Watson API
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Required header that specifies which emotion model to use 
    # describes the model to use in watson's EmotionPredict (Headers)
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # JSON payload required by the API 
    myobj = { "raw_document": { "text": text_to_analyze } }
    # assign response from requests method 
    response = requests.post(url, json=myobj, headers=headers)
    return response.text
