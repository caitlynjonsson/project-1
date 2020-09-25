import tweepy

from authorization_tokens import *

import random
#
# import pronouncing

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

message1_list = ["Yesterday was a warm summer day", "It was a cold fall morning", "Yesterday was a rainy spring day",
                    "The other day was Christmas", "It was a stormy winter night"]
message2_list = ["And I was out buying some groceries", "I was eatting some cereal", "I was out with some friends",
                "And my family made me some tea", "I was enjoying my time"]
message3_list = ["When someone tapped me on the shoulder", "When I was watching the news", "When I heard a loud noise",
                    "And I decided to go on a walk with my friend", "And I was watching a movie with my family"]
message4_list = ["They told me I looked like their cousin", "They were talking about the dangers of global warming",
                "It seems like theres been a lightning strike", "When I slipped and fell and broke my ankle",
                "But then I heard something outside my window"]
message5_list = ["I was shocked, this has never happened before", "I was surprised, how is this possible",
                "I wasn't sure what to do", "I was disappointed to say the least", "I felt very scared"]

random_number = random.randrange( len(message1_list) )
message1 = message1_list[ random_number ]
random_number = random.randrange( len(message2_list) )
message2 = message2_list[ random_number ]
random_number = random.randrange( len(message3_list) )
message3 = message3_list[ random_number ]
random_number = random.randrange( len(message4_list) )
message4 = message4_list[ random_number ]
random_number = random.randrange( len(message5_list) )
message5 = message5_list[ random_number ]

status1 = api.update_status(message1)
status2 = api.update_status(message2,in_reply_to_status_id = status1.id,auto_populate_reply_metadata=True)
status3 = api.update_status(message3,in_reply_to_status_id=status2.id,auto_populate_reply_metadata=True)
status4 = api.update_status(message4,in_reply_to_status_id=status3.id,auto_populate_reply_metadata=True)
status5 = api.update_status(message5,in_reply_to_status_id=status4.id,auto_populate_reply_metadata=True)

api.update_status = status1
api.update_status = status2
api.update_status = status3
api.update_status = status4
api.update_status = status5

 # option 1:
 # pick a phrase randomly from a list of phrases
# phrase_list = [ "Hi my name is Caitlyn",
#                  "Caitlyn is my name",
#                  "I like dogs" ]
# random_number = random.randrange( len(phrase_list) )
# message = phrase_list[ random_number ]

# api.update_status(message)

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
# mentions = api.mentions_timeline(count=1)
# mention = mentions[0]
#
# mention_word_list = mention.text.split()
# random_number = random.randrange ( len(mention_word_list) )
# word = mention_word_list [random_number]
#
# rhyming_word_list = pronouncing.rhymes(word)
# random_number = random.randrange( len(rhyming_word_list) )
# rhyme = rhyming_word_list [random_number]
#
# template = "if you like {}, you'll love {}"
# message = message = "@" + mention.user.screen_name + " " + template.format(word, rhyme)
#
# api.update_status(message, in_reply_to_status_id = mention.id)

# option 3 practice for experiment:
# randomly pick a template from a list, then randomly pick words
# from a word list, and use the words to fill in the template
# word_list = ["I broke my arm", "I fell into the lake", "I ran away", "I lost my dog"]
# template_list = [ "Guess what, {}, and {}",
#                   "you might think {} but actually {} ",
#                   "youd never guess it but {} and then {}" ]
# random_number = random.randrange( len(template_list) )
# template = template_list [ random_number ]
#
# random_number = random.randrange( len(word_list) )
# word1 = word_list[ random_number ]
#
# random_number = random.randrange( len(word_list) )
# word2 = word_list[ random_number ]
#
# message = template.format(word1,word2)
#
# api.update_status(message)

print("Done.")
