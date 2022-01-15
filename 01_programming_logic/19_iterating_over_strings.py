"""
Iterating over strings
"""
sentence = "o rato roeu a roupa do rei de roma"
sentence_size = len(sentence)
counting = 0
new_sentence = ""

while counting < sentence_size:
    # print(sentence[counting], counting)
    character = sentence[counting]
    if character == "r":
        new_sentence += "R"
    else:
        new_sentence += character
    counting += 1

print("new sentence:", new_sentence)
