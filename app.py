from xml.etree import ElementTree
from flask import Flask, Response, request, render_template
import requests
import json
from dotenv import load_dotenv
import os
SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")

load_dotenv()
app = Flask(__name__)

@app.route('/voice', methods=['GET', 'POST'])
def get_voices():
    voices_url = 'https://eastus.tts.speech.microsoft.com/cognitiveservices/voices/list'
    headers = {
        'Ocp-Apim-Subscription-Key':SUBSCRIPTION_KEY
    }
    voices = requests.get(voices_url, headers=headers)
    if voices.ok:
        return json.loads(voices.text)
    else:
        return Response(voices.reason, voices.status_code)

@app.route('/texttospeech', methods=['GET', 'POST'])
def cognitive_service():
    if 'text' in request.form:
        text = request.form['text']
        return call_azure_cognitive_api(text)
    else:
       return Response("Text field is missing", 400)

@app.route('/textToSpeechCustom', methods=['GET', 'POST'])
def cognitive_service_custom_voice():
    if 'text' in request.form and 'voice' in request.form:
        text = request.form['text']
        voice = request.form['voice']
        return call_azure_cognitive_api(text, voice)
    else:
        return Response("Text or voice field is missing", 400)
    
def call_azure_cognitive_api(text, voice_short_name = "en-US-ChristopherNeural"):
    token = get_token()
    cognitive_service_url = 'https://eastus.tts.speech.microsoft.com/cognitiveservices/v1'
    headers = {
        'Ocp-Apim-Subscription-Key':SUBSCRIPTION_KEY,
        # 'Authorization': 'Bearer %s' %token,
        'X-Microsoft-OutputFormat': 'audio-16khz-32kbitrate-mono-mp3',
        'Content-Type':'application/ssml+xml'
    }
    
   
    xml_body = ElementTree.Element('speak', version='1.0')
    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
    voice = ElementTree.SubElement(xml_body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
    voice.set('name', voice_short_name) # Short name for 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)'
    voice.text = text
    body = ElementTree.tostring(xml_body)
    
    response = requests.post(cognitive_service_url,data=body,headers=headers)
    if response.ok:
        return Response(response.iter_content(chunk_size=10*1024),
                    content_type=response.headers['Content-Type'])
    else:
        return Response(response.reason, response.status_code)

def get_token():
    fetch_token_url = 'https://eastus.api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
    }
    response = requests.post(fetch_token_url, headers=headers)
    access_token = str(response.text)
    return access_token

if __name__ == '__main__':
    app.run(port=8000, debug=True)
