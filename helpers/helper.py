import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

##### Define button style
button_style = {'background-color': 'darkblue',
                    'color': 'white',
                    'textAlign': 'center',
                }

########### Define your variables ######

myheading1='Vader Sentiment Analysis'
initial_value='You have controlled your fear. Now, release your anger. Only your hatred can destroy me.'
tabtitle = 'Vader'
sourceurl = 'https://pypi.org/project/vaderSentiment/'
githublink = 'https://github.com/plotly-dash-apps/620-vader-sentiment-analysis'

####### Write your primary function here
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        final="Positive"
    elif sentiment_dict['compound'] <= - 0.05 :
        final="Negative"
    else :
        final="Neutral"
    # responses
    response1=f"Overall sentiment dictionary is : {sentiment_dict}"
    response2=f"Sentence rated as {round(sentiment_dict['neg']*100, 2)}% Negative"
    response3=f"Sentence rated as {round(sentiment_dict['neu']*100, 2)}% Neutral"
    response4=f"Sentence rated as {round(sentiment_dict['pos']*100,2 )}% Positive"
    response5=f"Sentence Overall Rated As {final}"
    return response1, response2, response3, response4, response5
