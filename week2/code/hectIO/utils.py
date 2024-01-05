import random
import string

def getRandomStr(length):
    numLetters = random.randint(0, length/2)
    numDigits = random.randint(0, length/2)
    numPunctuation = length - numLetters - numDigits
    letters = ''.join((random.choice(string.ascii_letters) for i in range(numLetters)))
    digits = ''.join((random.choice(string.digits) for i in range(numDigits)))
    punctuation = ''.join((random.choice(string.punctuation) for i in range(numPunctuation)))
    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits + punctuation)
    random.shuffle(sample_list)
    # convert list to string
    final_string = ''.join(sample_list)
    return final_string