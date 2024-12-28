from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import translate_v2 as translate
import os

# Set the environment variable to point to your Google Cloud service account key JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/translateKey/spring-bonfire-446010-f9-09caeb427782.json"

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Initialize the Google Translate client
translate_client = translate.Client()

@app.route('/translate', methods=['POST'])
def translate_text():
    # Parse the incoming JSON request
    data = request.json
    text = data.get('text')  # Text to translate
    target_language = data.get('targetLanguage')  # Target language code

    # Validate inputs
    if not text or not target_language:
        return jsonify({"error": "Both 'text' and 'targetLanguage' are required fields"}), 400

    try:
        # Perform the translation
        result = translate_client.translate(text, target_language=target_language)
        return jsonify({"translatedText": result['translatedText']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)


