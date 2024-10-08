''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotiondetector():
    ''' This function calculates emotion scores for text '''
    response = emotion_detector(request.args.get('textToAnalyze'))
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
    'anger': {response['anger']}, 'disgust': {response['disgust']}, 
    'fear': {response['fear']}, 'joy': {response['joy']} 
    and 'sadness': {response['sadness']}. 
    The dominant emotion is <b>{dominant_emotion}</b>"""

@app.route("/")
def render_index_page():
    ''' This function render index.html '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
