# Ping-Ponging with your Keyboard: English words that will drive you nuts

Have you ever heard of a "ping-pong word"? These are words that, when typed on a QWERTY keyboard, alternate between the left and right sides of the keyboard, just like playing ping-pong.

This repository contains a Python script that finds all the "ping-pong words" in the English language and some fun statistics related to these words. The script uses a list of English words that can be found at https://github.com/dwyl/english-words

This repository was inspired by a meme on twitter, which stated that typing the word "skepticism" is like playing ping-pong with your keyboard. I thought it would be fun to explore this concept further and find all the "ping-pong words" in the English language. Here's the meme that started it all:


![Meme](https://user-images.githubusercontent.com/83130443/213490822-b90d23f1-8831-4f63-a8ae-d17758da7622.png)

## Scripts
* **find_ping_pong_words.py**: This script takes a list of English words as an input and returns a list of "ping-pong words" that alternate between the left and right sides of the keyboard.
* **finger_travel.py**: This script takes a word as an input and calculates the distance traveled by the fingers to type that word on a QWERTY keyboard.
## Results
* The script found a total of 4,585 "ping-pong words" out of 370,105 total English words, which represents around 1.24% of all the words in the list. This means that out of every 100 words, only around 1 word is a "ping-pong word".

![results1](https://user-images.githubusercontent.com/83130443/213500848-84438a00-09cc-4874-a69b-a38aa9ce6cb8.png)

* Out of those 4,585 "ping-pong words", 115 words have 10 characters or more. This represents around 2.51% of all the "ping-pong words" found.

![results2](https://user-images.githubusercontent.com/83130443/213503847-54f34976-29d5-4ebe-af91-0abe682baaef.png)

* The longest "ping-pong words" is: 'antiskepticism' with 14 characters.

![results3](https://user-images.githubusercontent.com/83130443/213504558-c1207650-0845-417d-9626-0bf4faf09405.png)


* The most intense "ping-pong match" between you and your keyboard is held when typing the word "epanalepsis" with a distance of 67.5639695045162.
The "most intense ping-pong match" refers to the word that requires the most distance to be traveled by the fingers when typing it on a QWERTY keyboard. It's a way to compare the difficulty of typing different "ping-pong words". The distance is calculated based on the position of each letter on the QWERTY keyboard and the distance between them. For example, typing the word "epanalepsis" requires the fingers to travel a distance of 67.5639695045162 units (the unit is arbitrary, it depends on the implementation). To give you an idea of how this distance is calculated, the word "antiskepticism" has a distance of 64.46898119314358 units, this means that typing "epanalepsis" is considered more intense than typing "antiskepticism".

![results4](https://user-images.githubusercontent.com/83130443/213509993-dbb4fef6-1647-418b-92b2-bb2013964659.png)



* The top 5 most intense "ping-pong words" are:
1. The word "epanalepsis" with a distance of 67.5639695045162
2. The word "palapalai" with a distance of 66.23722322627773
3. The word "autotoxicosis" with a distance of 64.63374073984866
4. The word "antiskepticism" with a distance of 64.46898119314358
5. The word "suspensorial" with a distance of 64.13108930029671

## To-Do
* Create a script that allows the user to enter a word and animate the "ping-pong match" between the left and right side of the keyboard.
* Check if the entered word is a "ping-pong word" and if it's not, animate the corresponding side losing the match.
