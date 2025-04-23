# Language Detector

A Python-based language detection tool using NLP techniques to identify the language of user-provided text and translate it to English.

## Features

- Fast and accurate language detection
- Support for 55+ languages
- Works with short phrases and longer texts
- Automatic translation to English
- Built-in error handling for edge cases

## Requirements

- Python 3.x
- See package_requirements.txt for all dependencies

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r package_requirements.txt
   ```

## Usage

To start the web application:

```
python main.py
```

Or use Gunicorn:

```
gunicorn --bind 0.0.0.0:5000 main:app
```

Then open a browser and navigate to `http://localhost:5000`

## Implementation Details

- The language detection is powered by the `langdetect` Python library, which implements a Naive Bayes classifier to identify languages.
- Translation functionality is provided by the `deep-translator` library.
- The web interface is built with Flask and uses Bootstrap for styling.

## License

MIT License

## For trying this site use this link

(https://d4652527-7883-4233-bcdc-4225b28f713b-00-2cg1bjd1wowdf.spock.replit.dev/)

## Acknowledgements

- [langdetect](https://github.com/Mimino666/langdetect)
- [deep-translator](https://github.com/nidhaloff/deep-translator)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
