import tweepy

from authorization_tokens import *

import random

import pronouncing

# option 1:
# pick a phrase randomly from a list of phrases
# phrase_list = [ "Hi my name is Caitlyn",
#                  "Caitlyn is my name",
#                  "I like dogs" ]
# random_number = random.randrang( len(phrase_list) )
# message = phrase_list

# option 2:
# create a sentance template with some blanks and
# randomly pick a word from a list to fill in each blank
# word_list = ["apples", "bananas", "carrots", "grapes"]
#
# string_template = "some people think {} are good, but I like {}"
#
# random_number = random.randrange( len(word_list) )
# word1 = word_list[ random_number ]
# random_number = random.randrange( len(word_list) )
# word2 = word_list[ random_number ]
#
# message = string_template.format(word1,word2)

# option 3:
# randomly pick a template from a list, then randomly pick words
# from a word list, and use the words to fill in the template
# word_list = ["coffee", "books", "dogs", "humans"]
# template_list = [ "if you like {}, you'll love {}",
#                   "you might think im a {} person but actually im a {} person",
#                   "youd never guess it but I like {} even more than {}" ]
# random_number = random.randrange( len(template_list) )
# template = template_list [ random_number ]

# random_number = random.randrange( len(word_list) )
# word1 = word_list[ random_number ]

# random_number = random.randrange( len(word_list) )
# word2 = word_list[ random_number ]

# message = template.format(word1,word2)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# option 4
# basic search
# search_results = api.search( q="hate filter:safe", lang="en" )
# random_number = random.randrange ( len(search_results) )
# random_tweet = search_results[random_number]
# message = random_tweet.text.replace ("hate","love")
# api.update_status(message)

# option 5
# reply to a randomly selected mention
# mentions = api.mentions_timeline()
# random_number = random.randrange( len(mentions) )
# random_mention = mentions[random_number]
#
# message = "@" + random_mention.user.screen_name + " i am robot :) "
#
# api.update_status(message, in_reply_to_status_id = random_mention.id)

 # option 5b
 # reply to the most recent mentions, with rhyme
mentions = api.mentions_timeline(count=1)
mention = mentions[0]

mention_word_list = mention.text.split()
random_number = random.randrange ( len(mention_word_list) )
word = mention_word_list [random_number]

rhyming_word_list = pronouncing.rhymes(word)
random_number = random.randrange( len(rhyming_word_list) )
rhyme = rhyming_word_list [random_number]

template = "if you like {}, you'll love {}"
message = message = "@" + mention.user.screen_name + " " + template.format(word, rhyme)

api.update_status(message, in_reply_to_status_id = mention.id)

print("Done.")
