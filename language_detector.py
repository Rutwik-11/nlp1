import logging
from langdetect import detect, LangDetectException
from language_codes import LANGUAGE_CODES
from deep_translator import GoogleTranslator

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def translate_to_english(text, source_lang):
    """
    Translates text from the source language to English
    
    Args:
        text (str): The text to translate
        source_lang (str): The source language code
        
    Returns:
        str: The translated text in English, or None if translation failed
    """
    try:
        # Skip translation if already in English
        if source_lang == 'en':
            return text
            
        translator = GoogleTranslator(source=source_lang, target='en')
        translated_text = translator.translate(text)
        logger.debug(f"Translated text from {source_lang} to English")
        return translated_text
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        return None

def detect_language(text):
    """
    Detects the language of the given text using the langdetect library.
    
    Args:
        text (str): The text to detect the language of
        
    Returns:
        dict: A dictionary containing:
            - 'language_code': The detected language code
            - 'language_name': The full name of the detected language
            - 'success': Boolean indicating if detection was successful
            - 'error': Error message if detection failed
            - 'translated_text': The text translated to English (if successful)
    """
    result = {
        'language_code': None,
        'language_name': None,
        'success': False,
        'error': None,
        'translated_text': None
    }
    
    # Validate input
    if not text or not text.strip():
        result['error'] = "Please provide some text to analyze"
        return result
    
    # Text is too short for reliable detection
    if len(text.strip()) < 5:
        result['error'] = "Text is too short for reliable language detection"
        return result
    
    try:
        # Detect language
        lang_code = detect(text)
        
        # Map language code to full name
        lang_name = LANGUAGE_CODES.get(lang_code, "Unknown language")
        
        result['language_code'] = lang_code
        result['language_name'] = lang_name
        result['success'] = True
        
        logger.debug(f"Detected language: {lang_code} ({lang_name})")
        
        # Translate text to English if not already in English
        if lang_code != 'en':
            translated_text = translate_to_english(text, lang_code)
            result['translated_text'] = translated_text
        else:
            # Text is already in English
            result['translated_text'] = text
        
    except LangDetectException as e:
        logger.error(f"Language detection error: {str(e)}")
        result['error'] = f"Language detection error: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        result['error'] = f"An unexpected error occurred: {str(e)}"
        
    return result

def cli_interface():
    """Command-line interface for the language detector"""
    print("\n===== Language Detector =====")
    print("Enter text to detect its language (or 'q' to quit)")
    
    while True:
        user_input = input("\nEnter text: ")
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
            
        result = detect_language(user_input)
        
        if result['success']:
            print(f"\nDetected Language: {result['language_name']} ({result['language_code']})")
            if result['translated_text'] and result['language_code'] != 'en':
                print(f"\nEnglish Translation: {result['translated_text']}")
        else:
            print(f"\nError: {result['error']}")


if __name__ == "__main__":
    cli_interface()
