"""
Allows user to define convention for encoding string from one to another using a direct character -> character relationship
Function createDictionaries() must be called and succeed before encode() or decode() is called
"""


def createDictionaries(path):
    """
    Defines convention for encoding strings from a text file.
    Input:
        Path to File - Raw Text File, Each line will contain TWO characters separated by whitespace. 
                        First char is decoded char, second char is the char to encode the first char to
    Output:
        0 - Success
        1 - File path not valid
        2 - One or more lines contains a number of chars that != 2
        3 - A decoded character exists twice or more
        4 - An encoded character exists twice or more
    """
    encoding_temp, decoding_temp = {}, {}
    try:
        dict_file = open(path, "r")
    except FileNotFoundError:
        print("Error: Dictionary File not found")
        return 1 #file not found error code

    for line in dict_file.readlines():
       
        key, value = line.split()
        if len(key + value) != 2: #concatenates strings, must only be two chars 
            return 2 #if more or less than 2 chars return error code 2

        #prevents keys or values being added twice
        if key in encoding_temp: 
            return 3 #key already exists error code
        elif value in decoding_temp: 
            return 4 #key already exists error code

        encoding_temp[key], decoding_temp[value] = value, key
        #this could be done more efficiently, having two dicts to store the same values but reversed is inefficient use of memory, however will stick to instructions

    global encoding, decoding #here so it is not unnessecarily called - a better way to do this would be to use OOP, not sure if we're allowed to because it hasn't been covered though
    encoding, decoding = encoding_temp, decoding_temp #saves dictionaries if they pass all tests / are valid
    return 0 #success code

def encode(raw_string):
    """
    Encodes the string using convention defined by createDictionaries(). 
    createDictionaries() must have succeeded before attempting to encode a string
        Input: Raw String
        Output: Encoded String 
                or 
                ##### -  Error, one or more chars in string does not have a corresponding encoded character
    """
    encoded_string = ""
    for char in raw_string:
        try:
            encoded_string += encoding[char] #fetches and appends correct corresponding encoded character
        except KeyError:
            return "#####"

            
    return encoded_string

def decode(encoded_string):
    """
    Decodes the string using convention defined by createDictionaries(). 
    createDictionaries() must have succeeded before attempting to decode a string
        Input: Encoded String
        Output: Decoded String 
                or 
                ##### -  Error, one or more chars in string does not have a corresponding decoded character
    """
    raw_string = ""
    for char in encoded_string:
        try:
            raw_string += decoding[char] #fetches and appends correct corresponding decoded character
        except KeyError:
            return encoded_string
            
    return raw_string