import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAACwrNebricBAJri8eZC9xPml5hhkEm9906cJUroZAVavyhaaPX0q1cnYoGLdnBhyKizShIyDBeQRjZAXrbdQoSZBnqk6ffBWcL0oCNMUTkG6NxpkAI7GZAIQTueLy76ObiIzyknkYcjJEkobkFpKPmKe2xoZCkcByLXelRTSqlAZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    response_img = {"recipient": {"id": id}, 
    "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": img_url
                }
            }
        }
    }
    response = requests.post(url, headers={"Content-Type": "application/json"},json=response_img)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response
    
"""
def send_button_message(id, text, buttons):
    pass
"""
