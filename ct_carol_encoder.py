"""
- I will directly use the clean_text function to clean the input text for any characters other than letters
- I will also directly use the get_key function to get a valid key between 1-25 from the user
- I will directly use the encode and decode functions the encode the carol to be saved in the encoded file
   and also decode so that I can see that it works.
- The encoded and decoded functions use the chunk5 function to format the output in chunks of 5 letters in them
   so I wouldnt DIRECTLY be using it.
1. First I will filter the text using clean_text
2. Then I will encode the filtered text using encode and a key from get_key
3. I will save the encoded text to carol_encoded.txt
4. Then I will decode the encoded text using decode and a key from get_key so that I can verify it works
"""

def clean_text(f):
    for i in f:
        if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            f = f.replace(i, "")
        else:
            f = f.replace(i, i.upper())
    return f



def chunk5(f):
    s = ""
    iter = 0
    words = 0
    for i in f:
        s = s + i
        iter += 1
        if iter % 5 == 0:
            words += 1
            s = s + " "
            if words == 8:
                s = s + "\n"
                words = 0
    return s.strip()


def get_key() -> int:
    var = 0
    try:
        while var < 1 or var > 25:
            var = int(input("Enter a key (integer) from 1-25: "))
        return var
    except ValueError:
        print("Invalid input. Please enter an integer. Rerun the program.")
        quit()
        return 99

def encode(value, key):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = value.upper()
    encoded = ""
    #print("Value to encode:", value)
    for char in value:
        if char in chars:
            encoded += chars[(chars.index(char) + key) % 26]
    print("\nEncoded value:", chunk5(encoded))
    return chunk5(encoded).strip()

def decode(value, key):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = value.upper()
    decoded = ""
    #print("Value to decode:", value)
    for char in value:
        if char in chars:
            decoded += chars[(chars.index(char) - key) % 26]
    print("\nDecoded value:", chunk5(decoded))
    return chunk5(decoded).strip()


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

#opening file
f = open("carol_original.txt", "r").read()
print("uncleaned text:", f)
input("Uncleaned text letter freqencies:" + str(letter_frequency(f)) + "\nPress Enter to continue...")

filtered = clean_text(f)
print("\nFiltered text:", filtered)

encoded = encode(filtered, get_key())    
with open("carol_encoded.txt", "w") as c:
    c.write(encoded)


decoded = decode(encoded, get_key())
with open("decoded.txt", "w") as c:
    c.write(decoded)
