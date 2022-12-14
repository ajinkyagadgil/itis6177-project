# ITIS 6177 Final Project - Text to Speech

## Introduction
- I have implemented Text to Speech conversion in this project using Microsoft Azure Cognitive Services Text-to-Speech API. Here when we pass the text to the API it returns the audio output which is the speech output of the input text.

## Project Architecture and Explanation 
<img width="516" alt="image" src="https://user-images.githubusercontent.com/60301110/207738920-83422561-210a-4250-ab07-ec7732144257.png">

## Main Components
- Postman/UI: This is used to call the digital ocean-hosted API to get the response. Here called maybe postman or a UI element to get the speech audio data.
- API hosted on Digital Ocean: This is SI project API that in turn calls the Text to Speech API Azure APIs
- Text to Speech API: These are cognitive service APIs for Text to Speech related operations provided by Azure.

### Explanation
- Here postman calls the API hosted on digital ocean with the required parameters and then using those parameters the digital ocean hosted API calls the Text to Speech APIs provided by Azure which returns the response to APIs hosted on the digital ocean which processes the response and returns it to the caller i.e., Postman or any UI which may choose how to use or modify the data.

## Tech Stack
- I have used Python Flask for creating the APIs. Consumed Microsoft Cognitive Services Text to Speech APIs for converting text to speech.
- Azure Text to Speech API
- Digital Ocean for hosting the API
- Git for version control

## Scope
- I have implemented majorly 3 APIs that complete text to speech process and have some flexibility as well.
  - API that converts given text to speech and the speech audio is the default voice which is not configurable.
  - The GET request returns the voice samples which can be used for output audio
  - API that converts given text to speech audio using configurable voice samples that we get from the above API (b)
  
## Instructions to run API from POSTMAN

### Text to Speech using default voice <br>
Endpoint URL: http://159.65.229.252:3000/texttospeech <br>
Request Type: POST <br>
Body: text to convert into speech as form-data <br>
<img width="470" alt="image" src="https://user-images.githubusercontent.com/60301110/207739717-9d917d5b-9143-4d3c-962f-25738fd3ef92.png"> <br>

In the above screenshot, you can see that postman sends a post request to API hosted on digital ocean with text to be converted into the body(form-data) of the request. It returns status 200 i.e., OK with an audio file that can be played/saved which is the converted speech audio output of the text. Here we are not giving any particular voice sample and hence it uses default voice sample i.e. ‘en-US-ChristopherNeural’. 

### Voice API <br>
Endpoint URL: http://159.65.229.252:3000/voice <br>
Request Type: GET <br>
<img width="470" alt="image" src="https://user-images.githubusercontent.com/60301110/207739829-71c6a452-441f-4c36-85c4-1abf97cbc932.png"> <br>
In the above screenshot, we call the voice API which returns an array of the object of all the voices that are supported by the Azure Text to Speech API and use one of these voice samples for our speech output. Example of one object is below
```
{
        "DisplayName": "Ameha",
        "Gender": "Male",
        "LocalName": "አምሀ",
        "Locale": "am-ET",
        "LocaleName": "Amharic (Ethiopia)",
        "Name": "Microsoft Server Speech Text to Speech Voice (am-ET, AmehaNeural)",
        "SampleRateHertz": "48000",
        "ShortName": "am-ET-AmehaNeural",
        "Status": "GA",
        "VoiceType": "Neural",
        "WordsPerMinute": "112"
    }

```
<br>
In the object, we can use the short name to send it to azure API and it returns the speech output in that voice sample.

### Text to Speech using custom voice <br>
Endpoint URL: http://159.65.229.252:3000/textToSpeechCustom  <br>
Request Type: POST <br>
Body: Text to convert to Speech and voice sample to be used for speech output <br>

<img width="470" alt="image" src="https://user-images.githubusercontent.com/60301110/207740325-00d515bc-ea31-4f03-b76c-ec1d23c72b5e.png"> <br>

In the above screenshot, we send a post request with 2 parameters. First is a text which is to be converted into speech and second is a voice which is the short name of any object that is returned from voice API. This returns a status 200 with an audio file that can be played or saved. Here it converts the given text <br>

## Error Handling
Following are the status codes and its meaning which may be returned from the API <br>
- 200: Success - Request is successful.
- 400: Bad Request - This is the most common error, and it occurs when some of the parameters are missing, empty or null.
- 401: Unauthorized – The request is not authorized to make sure that the token/auth key is correct.
- 503: Service Unavailable - When the server is down or unable to process a request.

## Subscription Key Security
- As shown in the architecture we use the Azure Text to Speech APIs. To use Azure Text to Speech APIs we need the Subscription key or token which then verifies the identity of the caller. This subscription key or token cannot be made public or written in the code so I created a .env file that stores the key-value pair and we can get that securely using the os module in Python Flask.

## Steps to Run the code
- Clone the repository https://github.com/ajinkyagadgil/itis6177-project.git 
- Go to the project folder where there is requirements.txt file and run the command ‘pip install -r requirements.txt’ which would install all the dependencies. (Make sure to have python and pip installed on your system)
- Create a .env file and add key as SUBSCRIPTION_KEY=<azure text to speech key>
- Run the code with command python app.py and use the endpoints to convert text to speech
- Create a resource group and service of Azure Text to Speech API to get the endpoint and subscription key

## Video Link of the demonstration
https://drive.google.com/file/d/1RQei84oCatTYb9ShgBmUrsCvvVJhhebK/view?usp=sharing 














