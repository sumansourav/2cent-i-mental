#! /usr/bin/env/python

"""
Citing:
If you use the VADER sentiment analysis tools, please cite:
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""

__author__ = 'sumansourav'

import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = []
# Read a line of sentences
# TODO: Replace with a CSV reading logic. Hardcoding sentences now.

with open('cnn_posts.csv', 'r', newline='', encoding='utf-8') as csvf:
    reader = csv.reader(csvf)
    # TODO: Not sure at this point which data shall be needed.
    # Extract column containing messages
    row = 1
    for row in reader:
        # first row
        message_index = 9
        if row == 1:
            message_index = row.find('message')
        else:
            sentences.append(row[message_index])
#
#
#
# exit(0)
# sentences = ["VADER is smart, handsome, and funny.",  # positive sentence example
#              "VADER is not smart, handsome, nor funny.",  # negation sentence example
#              "VADER is smart, handsome, and funny!",
#              # punctuation emphasis handled correctly (sentiment intensity adjusted)
#              "VADER is very smart, handsome, and funny.",
#              # booster words handled correctly (sentiment intensity adjusted)
#              "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
#              "VADER is VERY SMART, handsome, and FUNNY!!!",
#              # combination of signals - VADER appropriately adjusts intensity
#              "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",
#              # booster words & punctuation make this close to ceiling for score
#              "The book was good.",  # positive sentence
#              "The book was kind of good.",  # qualified positive sentence is handled correctly (intensity adjusted)
#              "The plot was good, but the characters are uncompelling and the dialog is not great.",
#              # mixed negation sentence
#              "At least it isn't a horrible book.",  # negated negative sentence with contraction
#              "Make sure you :) or :D today!",  # emoticons handled
#              "Today SUX!",  # negative slang with capitalization emphasis
#              "Today only kinda sux! But I'll get by, lol",
#              # mixed sentiment example with slang and constrastive conjunction "but"
#              "Moving sucks!!",
#              "Game of Thrones is an awesome series!! :) ",
#              "Jon + Dany = Incest!"  # [WARN] Limitation - Not able to recognize the compound value
#              ]
# TODO: Find logic to find the sentiment if no valid compound score is received

analyzer = SentimentIntensityAnalyzer()

with open("output.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(("Message", "Positive", "Negative", "Neutral", "Compound"))
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        writer.writerow([sentence, vs["pos"], vs["neg"], vs["neu"], vs["compound"]])
        print(vs)
