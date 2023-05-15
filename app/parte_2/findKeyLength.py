from weakref import ref
from plotter import plotter
from utils import remove_combining_fluent, remove_caracteres_especiais_e_espacos

#1 - Find the length of the key
    
        # 1.1 - Print out cyphertext on a long single strip twice


def findKeyLength(cyphertext=None):
    
    if cyphertext is None:        
        with open('./app/parte_2/txts/ritaLee_ptbr.txt', 'r') as file:
            cyphertext = file.read().replace('\n', '')
    
    
    remove_combining_fluent(cyphertext)
    remove_caracteres_especiais_e_espacos(cyphertext).upper()
    print(cyphertext)
    
    shiftsList = [cyphertext]
    i=1
    for substr in range(len(cyphertext)):
        cyphertex = cyphertext[:-1]
        shiftsList.append(" "*i + cyphertex)
        cyphertext = cyphertex
        i+=1
        #print(f'{cyphertex}')
        # 1.2 - Slide the strip across itself until the last letter 
        #       of the cyphertext matches the first letter of the
        #       second copy of the cyphertext
        #
        #    'CYPHERTEXT'
        #      .    .  .  
        #    ' CYPHERTEX'      
        
        # 1.3 - Find and count caracters coincidences
    
    offsets = []
    hitsList = []
    
    #print(shiftsList)
    
    #for i in range(1,len(shiftsList)-1):
    #        print(shiftsList[0])
    #        print(shiftsList[i])
    #        print()
            
    # try another for loop to show the shifts side by side 
    # and then compare them
    #TODO: try to find a way to compare the shifts side by side
    
    
    
    
    Ngram = 1
    
    #C = int(len(shiftsList)*0.01)
    C = 100
    
    print(f"len(shiftsList): {len(shiftsList)}")
    for shift in range(1,C):
        coincidences=0
        for j in range(0,len(shiftsList)):
            #print(shiftsList[0][j],end=' -> ')
            #print(shiftsList[shift][j])
            
            if shiftsList[0][j:j+Ngram]==shiftsList[shift][j:j+Ngram]:
                coincidences+=1
    
        offsets+=[shift]
        hitsList+=[coincidences]
        print(f'offset: {shift}; coincidences: {coincidences}')

    #print(offsetsList)
    #print(hitsList)
    
                       
    plotter(offsets,hitsList, threshold=7)
    
        
        
        # 1.4 - Count the number of letters between the two matching letters
        
        
        # 1.5 - Repeat steps 1.2 and 1.3 for each letter in the cyphertext
        
            
        
        # 1.6 - The most common distance between matching letters is the length 
        #       of the key
    
    
    
    offsetHitsTuples = list(zip(offsets,hitsList))
    return offsetHitsTuples
        
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
    #findKeyLength()
    offsetHitsTuples=findKeyLength()
    #print(offsetHitsList)
    #for i in offsetHitsList:
    #    print(i)
    

    with open('./app/parte_2/output.txt', 'w') as file:
        file.write(str(offsetHitsTuples))
    
    
    
    