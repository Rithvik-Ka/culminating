def letter_frequency(text: str) -> dict[str, int]:
    """Return a dictionary mapping each letter A–Z to its count in text."""
    ls = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = {}
    print(text)

    for char in text.upper():#counting
        try:
            letters[char] += 1
        except:
            letters[char] = 1


    #finding highest frequency
    """record = 0
    record_letter = ""
    for count in letters:
        if letters[count] > record:
            record = letters[count]
            record_letter = count

    return [record_letter, record]"""
    return letters

def double_letter_counts(text: str) -> dict[str, int]:
    """Return a dict mapping a letter to how many times its double appears."""
    doubles = {"AA": 0, "BB": 0, "CC": 0, "DD": 0, "EE": 0, "FF": 0, "GG": 0,
               "HH": 0, "II": 0, "JJ": 0, "KK": 0, "LL": 0, "MM": 0, "NN": 0, "OO": 0, "PP": 0,
               "QQ": 0, "RR": 0, "SS": 0, "TT": 0, "UU": 0, "VV": 0, "WW": 0, "XX": 0,
               "YY": 0, "ZZ": 0}
    
    iter = 0
    text = text.upper()

    for i in text:
        try: 
            char2 = text[iter+1] 
            char1 = text[iter]
        except: break

        if text[iter] == text[iter+1]:#checkign for doubles
            doubles[char1+char2] += 1
            iter += 1  
        
        iter += 1
    print(doubles)
    return doubles

def most_common_double_letter(text: str) -> tuple[str, int] | None:
    """Return (letter, count) for the most common double letter, or None if none."""
    doubles = {"AA": 0, "BB": 0, "CC": 0, "DD": 0, "EE": 0, "FF": 0, "GG": 0,
               "HH": 0, "II": 0, "JJ": 0, "KK": 0, "LL": 0, "MM": 0, "NN": 0, "OO": 0, "PP": 0,
               "QQ": 0, "RR": 0, "SS": 0, "TT": 0, "UU": 0, "VV": 0, "WW": 0, "XX": 0,
               "YY": 0, "ZZ": 0}
    
    iter = 0
    text = text.upper()
    highest_double = 0
    highest_double_letter = ""

    for i in text:
        try: 
            char2 = text[iter+1] 
            char1 = text[iter]
        except: break

        if text[iter] == text[iter+1]:#checkign for doubles
            doubles[char1+char2] += 1
            iter += 1
            if doubles[char1+char2] > highest_double:#checking if this is the highest double
                highest_double = doubles[char1+char2]
                highest_double_letter = char1+char2    
        iter += 1
    

    tied_double_letters_inorder = []
    for double in doubles: #finding all ties
        if doubles[double] == highest_double:
            tied_double_letters_inorder.append(double)    

    for i in range(len(text) + 1): #finding first occuring tied double letter
        try:db = text[i]+text[i+1]
        except: break
        if db in tied_double_letters_inorder:
            highest_double_letter = db
            break
    
    if highest_double == 0:
        return None
    else:
        return(highest_double_letter, highest_double)

if __name__ == "__main__":
    text = input("Enter a line of text: ")
    print("letter frequency:\n" + str(letter_frequency(text)))
    
    m = most_common_double_letter(text)
    if m == None:
        print("No double letters found.")
    else:
        print("Most common double letter: " + m[0] + " (appears " + str(m[1]) + " times)")