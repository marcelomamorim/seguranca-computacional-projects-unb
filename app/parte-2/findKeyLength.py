

#1 - Find the length of the key
    
        # 1.1 - Print out cyphertext on a long single strip twice
def findKeyLength():
        
    with open('desafio1.txt', 'r') as file:
        cyphertext = file.read().replace('\n', '') 
    
    return cyphertext

    #print(cyphertext)
    #print(cyphertext)
        
        
        
        # 1.2 - Slide the strip across itself until the last letter 
        #       of the cyphertext matches the first letter of the
        #       second copy of the cyphertext
        
        
        # 1.3 - Find and count caracters coincidences
        
        
        # 1.4 - Count the number of letters between the two matching letters
        
        
        # 1.5 - Repeat steps 1.2 and 1.3 for each letter in the cyphertext
        
        
        # 1.6 - The most common distance between matching letters is the length 
        #       of the key
        
        
        # 1.7 - If the key is longer than 10 characters, it is unlikely that the key 
        #       is longer than 10 characters
        # 1.8 - If the key is shorter than 3 characters, it is unlikely that the key 
        #       is shorter than 3 characters

    # 1.9 - If the key is 3 characters long, it is likely that the key is "the"

    # 1.10 - If the key is 2 characters long, it is likely that the key is "of", "to", "in", "it", "is", "be", "as", "at",
    # "so", "we", "he", "by", "or", "on", "do", "if", "me", "my", "up", "an", "go", "no", "us", "am"

    # 1.11 - If the key is 1 character long, it is likely that the key is "a", "i"

    # 1.12 - If the key is 4 characters long, it is likely that the key is "that", "have", "with", "this", "will", "your",
    # "from", "they", "know", "want", "been", "good", "much", "some", "time"

    # 1.13 - If the key is 5 characters long, it is likely that the key is "their", "there", "would", "could", "about",
    # "which", "these", "other", "words", "after", "first", "thing", "those", "where", "sound", "water", "place",
    # "right", "think", "three", "years", "world", "still", "small", "never", "under", "while", "along", "might",
    # "house", "found", "light", "large", "every", "since", "between", "under", "being", "leave", "heart", "story",
    # "today", "great", "paper", "often", "until", "night", "always", "money", "music", "point", "until", "night",
    # "always", "money", "music", "point", "until", "night", "always", "money", "music", "point", "until", "night",

    # 1.14 - If the key is 6 characters long, it is likely that the key is "people", "really", "family", "school",
    # "second", "around", "friend", "father", "mother", "before", "though"

    # 1.15 - If the key is 7 characters long, it is likely that the key is "because", "through", "thought", "without",
    # "nothing", "another", "against", "without", "nothing", "another", "against", "without", "nothing", "another",
    # "against", "without", "nothing", "another", "against", "without", "nothing", "another", "against", "without",



if __name__ == "__main__":
    findKeyLength()