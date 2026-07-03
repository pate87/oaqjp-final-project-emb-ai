''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion detection_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotion and its 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion detection_analyzer function and store the response
    res = emotion_detector(text_to_analyze)

    # Extract the anger, disgust, fear, joy, sadness from the response
    # anger = res['anger']
    # disgust = res['disgust']
    # fear = res['fear']
    # joy = res['joy']
    # sadness = res['sadness']
    dominant_emotion = res['dominant_emotion']

     # Check if the emotions are None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # Return a formatted string with the emotion detection anger, disgust, fear, joy, sadness
    return (
        f"For the given statement, the system response is "
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, "
        f"'fear': {res['fear']}, 'joy': {res['joy']} and "
        f"'sadness': {res['sadness']}. The dominant emotion is {dominant_emotion}."
    )
    # return ("For the given statement, the system response is "
    #     "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} "
    #     "and 'sadness': {}. The dominant emotion is {}."
    #     .format(anger, disgust, fear, joy, sadness, dominant_emotion))

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
