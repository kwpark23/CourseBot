# 2019 Summer CS Research Project: Chatbot

This is an independent reasearch project for Summer 2019. 

## Navigation
<a name="top"></a> 
1. [Research Description](#intro)  
2. [Background Information](#background)
    - [Introduction to Chatbot](#intro2)
    - [How chatbots work](#work)
    - [How chatbots apply machine learning](#apply)
3. [Building a chatbot using Python](#python)
4. [Building a chatbot using Dialogflow](#dialog)
5. [Research Materials](#material)
6. [License Information](#license)

## <a name="intro"></a>Research Description 

This summer, I attended the study group for students who were interested in machine learning, led by Lisa Zhang, who is a CS professor at UTM. I decided to work on a research project to learn a how machine learning can be used to solve real world problems. After choosing **chatbot** as my research topic, I read up various articles to learn about it in detail, built a simple chatbot to understand how it works, wrote up instructions for other students to build their own chatbot, and presented about my research in front of other students and Lisa.  

[Back to top](#top)

## <a name="background"></a>Background Information
I want to start with basic introduction to chatbots, then talk about how they work, and finally talk about how chatbots apply machine learning.

### <a name="intro2"></a>Introduction to Chatbot
Here is the simple definition of chatbot: It is a software system or program designed to interact with humans through chats.

You have probably seen chatbot in its various iterations: As AI speakers, message boxes, and humanoid robots. Any software that understands human language and responds appropriately can be identified as chatbots. 

The first chatbot was created quite some time ago. It was named Eliza and it simulated conversation with humans using regular expressions. Now chatbots uses regular expressions as well machine learning to do NLP.  

Chatbots are being used more and more by companies because unlike human operators, they are available 24 hours at fraction of cost, they have access to large amount of data, and their performance is quantifiable.

### <a name="work"></a>How chatbots work
Building a chatbot requires identifying the following four things: 
  -Understand target audience: college students, consumer of the product, businessmen/women, or some other category of users.
  -Understand the natural language of communication: Is the user asking question in English, French, Chinese, Spanish, and so on?
  -Understand the intent or desire of the user: Is the user asking about book recommendation, restaurant search, booking hotel, how to use software?
  -Lastly, you want your chatbot to provide appropriate response to user’s question.

Chatbot is also about simulating conversation between humans, so there are fun aspect of making a chatbot, like adding personalities. 

Now, let’s discuss how a chatbot process human language. When you type some text into your chatbot, generally it looks for two things: intents and entities of the sentence. **Intent** is the broad description of what a user is trying to say and **Entity** is data classification from information the user provided. For example, if a user entered, "I want  to book a flight from Toronto to Seoul.", intents could be 'Flight_booking' and 'Flight_search'. As for entities, phrase, "book a flight" could be categorized as Booking ,and "Toronto" and "Seoul" could be categorized as Location.

Problem with identifying intents and entities is that human language has a lot of ambiguity. There are many ways to say the same thing. And classifying sentences by hand will take really long time. This is where machine learning comes to the rescue!

### <a name="apply"></a>How chatbots apply machine learning
I mentioned that in the old days, chatbots were built using regular expression and pattern matching. Now, chatbots are trained using word vector models. 

Simply put, word vector model transforms English words into n-dimensional vectors in space. The model uses angles between vectors to identify similarity between them. This is called cosine similarity, uses number between 0 and 1, with 1 having similar orientation and 0 having different orientation. For example, cat-dog will have higher cosine similarity than cat-can, because cat-dog are both animals. You train the model using training data set. Next, you improve the accuracy of the model by tweaking parameters to the model. Lastly, you feed new dataset that the model have never been exposed to before and train it further. Doing this from scratch takes a lot of data, time and computer power. Better idea is to use existing libraries with trained word vectors.

Here are a few popular machine learning libraries available for Python. You can use spacy for NLP, Scikitlearn for ML implementation and data analysis. The third library called Rasa_NLU is developed by company specializing in chatbots. It combines functionality of both spacy and scikitlearn. Below are links to each of the libraries:

  -  spaCy [installation](https://spacy.io/usage)
  -  Scikit-learn [installation](https://scikit-learn.org/stable/install.html)
  -  rasa_nlu [installation](http://rasa.com/docs/rasa/user-guide/installation/)
  
[Back to top](#top)

## <a name="material"></a>Research Materials
1. Build your first chatbot using Python NLTK [link](https://towardsdatascience.com/build-your-first-chatbot-using-python-nltk-5d07b027e727)
2. How to Build an Intelligent Chatbot with Python and Dialogflow [link](https://cloudacademy.com/blog/how-to-build-an-intelligent-chatbot-with-python-and-dialogflow/)
3. How I developed my own ‘learning’ chatbot in Python from scratch and deployed it on Facebook Messenger! [link](https://chatbotslife.com/how-i-developed-my-own-learning-chatbot-in-python-from-scratch-and-deployed-it-on-facebook-88bc828be0a8)
4. Developing a Chatbot using Python Language: Tutorial [link](https://www.probytes.net/blog/how-to-make-a-chatbot-in-python/)
5. ChatterBot is a machine learning, conversational dialog engine for creating chat bots [link](https://github.com/gunthercox/ChatterBot)
6. Deep Learning for Chatbots, Part 1 – Introduction [link](http://www.wildml.com/2016/04/deep-learning-for-chatbots-part-1-introduction/)
7. Building Facebook Messenger Bots with Python in less than 60 minutes [link](https://www.twilio.com/blog/2017/12/facebook-messenger-bot-python.html)
8. How to Build Your First Chatbot [link](https://tutorials.botsfloor.com/how-to-build-your-first-chatbot-c84495d4622d)
9. A New Approach to Conversational Software [link](https://medium.com/rasa-blog/a-new-approach-to-conversational-software-2e64a5d05f2a)
10. nltk.chat package [link](https://www.nltk.org/api/nltk.chat.html)
11. Datacamp course on building a chatbot [link](https://www.datacamp.com/courses/building-chatbots-in-python)
12. How to make a Chatbot with Dialogflow - API.ai [link](https://www.youtube.com/watch?v=gWNUg_v25dw)
13. DialogFlow (API.AI) Chatbot Tutorial - integration with Facebook messenger in 3 minutes [link](https://www.youtube.com/watch?v=-2hE3YHsuBQ)

[Back to top](#top)

## <a name="license></a>License Information
The MIT License (MIT)

Copyright © 2019 Zeros_Matter

You can find a copy of the License at https://mit-license.org/

License for them is in `Public Domain`

[Back to top](#top)


