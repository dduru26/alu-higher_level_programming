#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:  # Check if the sentence is not empty
        return (len(sentence), sentence[0])  # Return length and first character
    else:
        return (0, None)  # Return 0 and None if the sentence is empty
