''' Executing this function initiates the application of emotion
    detection to be executed with Flask  and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotionapp():
    ''' From the text the user inputs in the HTML interface this code
        runs emotion detection. The output returned shows the scores for each
        of the five emotions and the dominant one.
    '''
    text_to_process = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_process)
    if result['dominant_emotion'] != None:
        return (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    
    else:
        return ('Invalid text! Please try again!.')
 
@app.route("/")
def render_index_page():
    ''' This function renders the main application index page
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000, debug = True)