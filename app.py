import os
import logging
from flask import Flask, render_template, request, jsonify
from language_detector import detect_language

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/')
def index():
    """Render the main page of the application"""
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    """API endpoint to detect the language of the provided text"""
    text = request.form.get('text', '')
    logger.debug(f"Received text for detection: {text[:50]}...")
    
    result = detect_language(text)
    
    return jsonify(result)



@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    logger.error(f"Server error: {str(e)}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
