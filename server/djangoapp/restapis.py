# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv


load_dotenv()


backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception:
        # If any error occurs
        print("Network exception occurred")


def analyze_review_sentiments(text):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text}}
    
    try:
        # Make the API request
        response = requests.post(url, json=myobj, headers=headers)
        
        # Ensure the response is successful
        response.raise_for_status()
        
        # Parse the response as JSON
        response_data = response.json()
        
        # Extract the emotion dictionary
        emotion_data = response_data['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion
        dominant_emotion = max(emotion_data, key=emotion_data.get)
        dominant_value = emotion_data[dominant_emotion]
        
        # Add the dominant emotion to the response
        return {
            "dominant_emotion": dominant_emotion,
            "dominant_value": dominant_value,
            "raw_response": response_data
        }
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as err:
        print(f"Unexpected error: {err}")
    
    # Return a default response in case of an error
    return {"dominant_emotion": None, "dominant_value": None, "raw_response": None}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception:
        print("Network exception occurred")
