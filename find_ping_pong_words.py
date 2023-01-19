def find_ping_pong_words(word_list: list) -> list:
    """
    Returns a list of words that are similar to "skepticism" in the way that the successive characters
    are each at a side of the keyboard, based on the QWERTY layout

    :param word_list: list of words to check
    :type word_list: list
    :return: list of words that match the criteria
    :rtype: list
    """
    left_side = set("qwertasdfgzxcv")
    right_side = set("yuiophjklbnm")
    ping_pong_words = []
    for word in word_list:
        on_left = word[0].lower() in left_side
        for letter in word[1:]:
            if letter.lower() in left_side:
                if not on_left:
                    on_left = True
                else:
                    break
            elif letter.lower() in right_side:
                if on_left:
                    on_left = False
                else:
                    break
            else:
                break
        else:
            ping_pong_words.append(word)
    return ping_pong_words
