# hugotbot.py
from nltk.chat.util import Chat, reflections
import nltk



pairs = [
  [
    r'(Hi|Hello|Hey)',
    ['Hey Friend! What is your name?'],
  ],
  [
    r'Im hungry',
    ['Would you like me to call uber eats?'],

  ],
  [
    r'(.*):name',
    ["""Nice to meet you, %1. I wish I had a name like that. I actually don't have a name yet...#awkward. Would you like to set up an Archethtect account? Type yes or no."""],
  ],
	[
		r'yes:account',
		["""Gnarly! Please take a picture of your QR code. Send it to me and I'll do the rest! """],
	],
  [
    r'no:account',
    ["Why text me when you know you don't want me? Quit wasting my time, bye."],
  ],
  [
    r'yes:qrcode',
    ["""Account created. Would you like to see a list of current proposals or learn more about Archethtect? Type proposals or arch."""],
  ],
  [
    r'no:qrcode',
    ["I'm sorry. For some reason that QR code could not be read. Please try focusing the camera and take it again."],
  ],
  [
    r'yes:proposals',
    ["""Here are a list of proposals on queue for voting. [Stronger Wifi @ EthDenver 2019, Shorter Opening Ceremonies, More Food Truck Options and more.] Which would you like to see? Type wifi or ceremonies or food or more. If you'd like to search by proposal category, type category."""],
  ],
  [
    r'yes:arch',
    ["""Wow! 😳 Thanks for being interested in me. Here's a link to learn more. https://github.com/Meeshbhoombah/architect"""],
  ],
  [
    r'yes:wifi',
    ["""It's no secret that despite the valient efforts of the EthDenver organizers that the wifi\nthis year was just short of disastrous. Therefore, in preparation for next year's event,\nI propose that in addition to forging partnerships with A1 blockchain and cryptocurrency\ncompanies, that EthDenver collaborate with Comcast/AT&T to ensure that the bandwith of\nthe wifi modems can accomodate the # of hackers in the space. This is especially imperative\nbecause EthDenver will only grow in interest and demand in the upcoming years."""],
  ],
  [
    r'yes:ceremonies',
    ["""Opening Ceremonies are a crucial part of every hackathon as they set the mood for the rest\nof the event. It's also an important time to talk about the community and the type of community\nwe as hackers want to build in this space. However, a 2-hour ceremony is abhorrently long. Hackathons\nare for hacking and time is precious. I propose that in the future, opening ceremonies are no longer than 1 hour long."""],
  ],
  [
    r'yes:food',
    ["""I'll be the first to say that the food truck line-up at EthDenver this year was phenomenal and exceeded my expectations.\nThere were a variety of cuisines to choose from and the wait times were short. However, a lot of the food was really heavy.\nAs hackers we are sitting down for long periods of time with not much opportunity to walk around, it causes the body and mind\nto be sluggish when hackathons require its' participants to keep a clear, sharp mind. I propose that for EthDenver 2019, the\norganizers offer more healthy/vegan/vegetarian options."""],
  ],
  [
    r'yes:more',
    ["link."],
  ],
  [
    r'yes:category',
    ["Here is a list of the available categories. [Sponsors, Venue, Location, Prizes.] From which category would you like to see proposals on queue for voting?"],
  ],
  [
    r'yes:different category',
    ["Sure thing. Here are the other available categories."],
  ],
  [
    r'yes:specific proposal',
    ["link."],
  ],
  [
    r'soon',
    ['Coming soon! Checkout https://github.com/Meeshbhoombah/architect to keep updated.']
  ]
]

reflections = {
  'my name is' :'your name is',
  'i was'      : 'you were',
  'i'          : 'you',
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

chat = Chat(pairs, reflections)

def get_response(user_message):
    # Parse user message and return appropriate response
    bot_response = chat.respond(user_message) 
    return bot_response

def ethdenver_bot():
    print("Welcome to the EthDenver Bot! What is your name?")
    chat.converse()


if __name__ == "__main__":
    ethdenver_bot()