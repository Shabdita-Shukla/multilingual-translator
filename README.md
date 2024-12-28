# Multilingual Translator

This is a simple web application for translating text into multiple languages using the Google Translate API.

## Features
- Translate content dynamically on a webpage.
- Supports multiple languages.

## Install Software
1. Install Python.
2. Install a code editor, like Visual Studio Code.

## Enable Google Translate API
1. Create a Google Cloud Project
-  Go to the Google Cloud Console.
-  Click on Select a project > New Project.
-  Give your project a name and click Create.

2. Create a Google Cloud Project
-  In your project dashboard, go to APIs & Services > Library.
-  Search for Cloud Translation API.
-  Click on it and click Enable.

3. Create a Service Account and add Role
-  Go to IAM > Service Accounts then create a account.
-  Add Cloud Translation API Service Agent Role.
-  Generate Key.json file and download it.

4. Set an environment variable GOOGLE_APPLICATION_CREDENTIALS to point to the key file.
   On Windows--set GOOGLE_APPLICATION_CREDENTIALS=path\to\key.json

## Install Python Libraries
1. pip install flask google-cloud-translate.

## Code Setup Instructions
1. Clone the repository.
2. Run the Flask Backend in bash
   python app.py
   backend is now running at http://localhost:5000
3. Open index.html in browser.
4. Select a language from the dropdown and observe the content translation.

## Testing the API
   Test the /translate endpoint using tools like Postman or curl.
1. Example Request (Postman or JavaScript)

   URL: http://localhost:5000/translate
   Method: POST
   Headers 
   {
      "Content-Type": "application/json"
   }
   Body
   {
      "text": "Hello, world!",
      "targetLanguage": "es"
   }

2. Response
   {
    "translatedText": "¡Hola, mundo!"
   }

Made with ❤️ By Shabdita






