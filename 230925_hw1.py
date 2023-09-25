Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text=open("jwh.txt", 'r').readline()
>>> print(text)
Cloud computing is a term for delivering hosted services over the Internet. Over a network, it gives services control over such things as a user's data and software. It has many advantages compared to the traditional way of storing data. For one thing, it only requires users to have a computer and access to the Internet. With cloud computing, users can access software and data stored on servers at a remote location from a number of different devices.
>>> texts=[sentence.split() for sentence in text.split(". ")]
>>> print(texts)
[['Cloud', 'computing', 'is', 'a', 'term', 'for', 'delivering', 'hosted', 'services', 'over', 'the', 'Internet'], ['Over', 'a', 'network,', 'it', 'gives', 'services', 'control', 'over', 'such', 'things', 'as', 'a', "user's", 'data', 'and', 'software'], ['It', 'has', 'many', 'advantages', 'compared', 'to', 'the', 'traditional', 'way', 'of', 'storing', 'data'], ['For', 'one', 'thing,', 'it', 'only', 'requires', 'users', 'to', 'have', 'a', 'computer', 'and', 'access', 'to', 'the', 'Internet'], ['With', 'cloud', 'computing,', 'users', 'can', 'access', 'software', 'and', 'data', 'stored', 'on', 'servers', 'at', 'a', 'remote', 'location', 'from', 'a', 'number', 'of', 'different', 'devices.']]
>>> print("1. text size= {}".format(len(text)))
1. text size= 454
>>> print("2. # of sentences={}".format(len(texts)))
2. # of sentences=5
>>> new_text=text.replace('.',' ').replace(',',' ').replace('\'',' ')
>>> total_characters=len(''.join(new_text.split()))
>>> print("3. # of total characters={}".format(total_characters))
3. # of total characters=368
>>> unique_characters=len(set(''.join(new_text.split())))
>>> print("3. # of unique characters={}".format(unique_characters))
3. # of unique characters=28
>>> all_words=[word for sentence in texts for word in sentence]
>>> total_words = len(all_words)
>>> unique_words = len(set(all_words))
>>> average_word_count = total_words / len(texts)
>>> print("4. total # of words:", total_words)
4. total # of words: 78
>>> print("4. # of unique words:", unique_words)
4. # of unique words: 57
>>> print("5. Average # of words:", average_word_count)
5. Average # of words: 15.6
