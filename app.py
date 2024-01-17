from flask import Flask, request, jsonify
from utils.text_to_summary import text_to_summary
from utils.translate_to_english import translate_to_english
from utils.categorizer import categorizer
from utils.classify_review import classify_review
from utils.text_to_speech import text_to_speech
from utils.text_to_sentiment import text_to_sentiment
from utils.best_answer import best_answer

# from utils.text_to_sentiment import text_to_sentiment

app = Flask(__name__)  # Corrected from _name_ to __name__

@app.route('/')
def test():
    return 'Welcome to mail assistant API'

@app.route('/predict', methods=['POST'])  # Added the method

def predict():
    data = request.get_json()
    variable_input = data['input1']  # Corrected the spelling of 'variable_input'

    response = {
        'email_summary': '',
        'sentiment': '',
        'category': '',
        'email_audio': ''
    }

    email_summary_var = text_to_summary(translate_to_english(variable_input))
    sentiment_var = text_to_sentiment(email_summary_var)
    category_var = categorizer(email_summary_var)
    # email_audio_var = text_to_speech(email_summary_var)
    email_audio_var = 'audio'
    best_answer_var = best_answer(email_summary_var)
    # best_answer_var = 'this best answer'
    best_answer_audio_var = 'best answer audio'
    # best_answer_audio_var = text_to_speech(best_answer_var)
    importance_var = 'really importante'

    response['email_summary'] = email_summary_var
    response['sentiment'] = sentiment_var
    response['category'] = category_var
    response['email_audio'] = email_audio_var
    response['best_answer'] = best_answer_var
    response['best_answer_audio'] = best_answer_audio_var
    response['importance'] = importance_var


    return jsonify(response)  # Wrapped the response in jsonify for proper JSON formatting

if __name__ == '__main__':  # Corrected from _name_ and _main_ to __name__ and __main__
    app.run(host='0.0.0.0', port=6969, debug=True)