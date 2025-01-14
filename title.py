import spacy
from collections import Counter
import sys

# Load spacy model
nlp = spacy.load("en_core_web_lg")

# Example text
# text = """What is Deep Learning? Deep learning is a branch of machine learning which is completely based on artificial neural networks, as neural network is going to mimic the human brain so deep learning is also a kind of mimic of human brain. In deep learning, we don’t need to explicitly program everything. The concept of deep learning is not new. It has been around for a couple of years now. It’s on hype nowadays because earlier we did not have that much processing power and a lot of data. As in the last 20 years, the processing power increases exponentially, deep learning and machine learning came in the picture. A formal definition of deep learning is- neurons.

# Virat Kohli is the best cricketer in the world. Even greats like Sachin and Ricky admire him. He has a record of 73 centuries.

# Humans have been, are, and will forever be thirsty to invent things that would make their lives easier and better by a thousandfold. The capacity of what a human mind can do has always baffled me. One such major invention would be what is called as AI- Artificial Intelligence. Wouldn’t it be great if machines could think? That’s precisely what AI is. We humans have natural intelligence. But if machines can think, it’d be artificial. So, AI is just a collective term for machines that can think. 

# What-is-AI-Artificial-Intelligence

# Now here are some examples of AI in real life. Robots are what come to mind first. They are machine replicas of human beings. They can think for themselves, take important decisions on their own without human help. Not all artificially intelligent machines need to look like human beings though. Some of the other examples include self-driving cars or Amazon Alexa or even Siri. One other important application can be speech recognition. Remember how you ask google by speaking instead of typing what you have to search for, into the search bar? That’s one of the applications right there. There are so many more applications but let me get on to other topics. 


# Artificial Intelligence (AI) is a branch of computer science that deals with the creation of intelligent machines that can perform tasks that typically require human intelligence. The goal of AI is to create algorithms and systems that can learn from data, reason, make predictions, and take actions.

# AI systems can be classified into two categories: narrow or weak AI, and general or strong AI. Narrow AI is designed to perform specific tasks, such as image recognition, speech recognition, or playing a game. On the other hand, general AI is capable of performing any intellectual task that a human can, including learning and problem-solving.

# Machine learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention.

# Do you get automatic recommendations on Netflix and Amazon Prime about the movies you should watch next? Or maybe you get options for People You may know on Facebook or LinkedIn? You might also use Siri, Alexa, etc. on your phones. That’s all Machine Learning! This is a technology that is becoming more and more popular. Chances are that Machine Learning is used in almost every technology around you!

# What-is-Machine-Learning?

# And it is hardly a new concept. Researchers have always been fascinated by the capacity of machines to learn on their own without being programmed in detail by humans. However, this has become much easier to do with the emergence of big data in modern times. Large amounts of data can be used to create much more accurate Machine Learning algorithms that are actually viable in the technical industry. And so, Machine Learning is now a buzz word in the industry despite having existed for a long time.


# But are you wondering what is Machine Learning after all? What are its various types and what are the different Machine Learning algorithms? Read on to find the answers to all your questions!

# What is Machine Learning?
# Machine Learning, as the name says, is all about machines learning automatically without being explicitly programmed or learning without any direct human intervention. This machine learning process starts with feeding them good quality data and then training the machines by building various machine learning models using the data and different algorithms. The choice of algorithms depends on what type of data we have and what kind of task we are trying to automate.

# As for the formal definition of Machine Learning, we can say that a Machine Learning algorithm learns from experience E with respect to some type of task T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.

# For example, If a Machine Learning algorithm is used to play chess. Then the experience E is playing many games of chess, the task T is playing chess with many players, and the performance measure P is the probability that the algorithm will win in the game of chess.

# What is the difference between Artificial Intelligence and Machine Learning?
# Artificial Intelligence and Machine Learning are correlated with each other, and yet they have some differences. Artificial Intelligence is an overarching concept that aims to create intelligence that mimics human-level intelligence. Artificial Intelligence is a general concept that deals with creating human-like critical thinking capability and reasoning skills for machines. On the other hand, Machine Learning is a subset or specific application of Artificial intelligence that aims to create machines that can learn autonomously from data. Machine Learning is specific, not general, which means it allows a machine to make predictions or take some decisions on a specific problem using data.

# Narendra Damodardas Modi (Gujarati: [ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː] (listen); born 17 September 1950)[b] is an Indian politician serving as the 14th and current Prime Minister of India since 2014. Modi was the Chief Minister of Gujarat from 2001 to 2014 and is the Member of Parliament from Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right-wing Hindu nationalist paramilitary volunteer organisation. He is the longest serving prime minister from outside the Indian National Congress.

# Modi was born and raised in Vadnagar in northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at age eight. He has reminisced about helping out after school at his father's tea stall at the Vadnagar railway station. At age 18, Modi was married to Jashodaben Chimanlal Modi, whom he abandoned soon after. He first publicly acknowledged her as his wife more than four decades later when required to do so by Indian law, but has made no contact with her since. Modi has asserted he had travelled in northern India for two years after leaving his parental home, visiting a number of religious centres, but few details of his travels have emerged. Upon his return to Gujarat in 1971, he became a full-time worker for the RSS. After the state of emergency was declared by prime minister Indira Gandhi in 1975, Modi went into hiding. The RSS assigned him to the BJP in 1985 and he held several positions within the party hierarchy until 2001, rising to the rank of general secretary.[c]

# Modi was appointed Chief Minister of Gujarat in 2001 due to Keshubhai Patel's failing health and poor public image following the earthquake in Bhuj. Modi was elected to the legislative assembly soon after. His administration has been considered complicit in the 2002 Gujarat riots in which 1044 people were killed, three-quarters of whom were Muslim,[d] or otherwise criticised for its management of the crisis. A Special Investigation Team appointed by the Supreme Court of India found no evidence to initiate prosecution proceedings against Modi personally.[e] While his policies as chief minister—credited with encouraging economic growth—have received praise, his administration was criticised for failing to significantly improve health, poverty and education indices in the state.[f]

# Modi led the BJP in the 2014 general election which gave the party a majority in the lower house of Indian parliament, the Lok Sabha, the first time for any single party since 1984. Modi's administration has tried to raise foreign direct investment in the Indian economy and reduced spending on healthcare, education, and social welfare programmes. Modi centralised power by abolishing the Planning Commission and replacing it with the NITI Aayog. He began a high-profile sanitation campaign, controversially initiated a demonetisation of high-denomination banknotes and a transformation of the taxation regime, and weakened or abolished environmental and labour laws. He oversaw the country's response to the COVID-19 pandemic. As Prime Minister, Modi has received consistently high approval ratings.

# Narendra Damodardas Modi (Gujarati: [ˈnəɾendɾə dɑmodəɾˈdɑs ˈmodiː] (listen); born 17 September 1950)[b] is an Indian politician serving as the 14th and current Prime Minister of India since 2014. Modi was the Chief Minister of Gujarat from 2001 to 2014 and is the Member of Parliament from Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right-wing Hindu nationalist paramilitary volunteer organisation. He is the longest serving prime minister from outside the Indian National Congress.

# Modi was born and raised in Vadnagar in northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at age eight. He has reminisced about helping out after school at his father's tea stall at the Vadnagar railway station. At age 18, Modi was married to Jashodaben Chimanlal Modi, whom he abandoned soon after. He first publicly acknowledged her as his wife more than four decades later when required to do so by Indian law, but has made no contact with her since. Modi has asserted he had travelled in northern India for two years after leaving his parental home, visiting a number of religious centres, but few details of his travels have emerged. Upon his return to Gujarat in 1971, he became a full-time worker for the RSS. After the state of emergency was declared by prime minister Indira Gandhi in 1975, Modi went into hiding. The RSS assigned him to the BJP in 1985 and he held several positions within the party hierarchy until 2001, rising to the rank of general secretary.[c]

# Modi was appointed Chief Minister of Gujarat in 2001 due to Keshubhai Patel's failing health and poor public image following the earthquake in Bhuj. Modi was elected to the legislative assembly soon after. His administration has been considered complicit in the 2002 Gujarat riots in which 1044 people were killed, three-quarters of whom were Muslim,[d] or otherwise criticised for its management of the crisis. A Special Investigation Team appointed by the Supreme Court of India found no evidence to initiate prosecution proceedings against Modi personally.[e] While his policies as chief minister—credited with encouraging economic growth—have received praise, his administration was criticised for failing to significantly improve health, poverty and education indices in the state.[f]

# Modi led the BJP in the 2014 general election which gave the party a majority in the lower house of Indian parliament, the Lok Sabha, the first time for any single party since 1984. Modi's administration has tried to raise foreign direct investment in the Indian economy and reduced spending on healthcare, education, and social welfare programmes. Modi centralised power by abolishing the Planning Commission and replacing it with the NITI Aayog. He began a high-profile sanitation campaign, controversially initiated a demonetisation of high-denomination banknotes and a transformation of the taxation regime, and weakened or abolished environmental and labour laws. He oversaw the country's response to the COVID-19 pandemic. As Prime Minister, Modi has received consistently high approval ratings."""
# Tokenize the text using spacy

text = str(sys.argv[1])

doc = nlp(text)

# Extract named entities and filter out non-relevant entities
entities = [entity.text.lower() for entity in doc.ents if entity.label_ ==
            "PERSON" and entity.text.lower() not in ["the", "a", "an"]]

# Calculate the frequency of the named entities
freq = Counter(entities)

# Choose the named entity with the highest frequency as the title
if freq:
    title = freq.most_common(1)[0][0]
    print(title)
else:
    print("No relevant entities found.")
