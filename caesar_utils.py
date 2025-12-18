

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
    print("Value to encode:", value)
    for char in value:
        if char in chars:
            encoded += chars[(chars.index(char) + key) % 26]
    print("\nEncoded value:", chunk5(encoded))
    return chunk5(encoded).strip()

def decode(value, key):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = value.upper()
    decoded = ""
    print("Value to decode:", value)
    for char in value:
        if char in chars:
            decoded += chars[(chars.index(char) - key) % 26]
    print("\nDecoded value:", chunk5(decoded))
    return chunk5(decoded).strip()

if __name__ == "__main__":
    #opening file
    f = open(input("What is the file you want to read?\n-> "), "r").read()
    print("uncleaned text:", f)

    filtered = clean_text(f)
    print("\nFiltered text:", filtered)
    
    encoded = encode(filtered, get_key())    
    with open("encoded.txt", "w") as c:
        c.write(encoded)
    

    decoded = decode(encoded, get_key())
    with open("decoded.txt", "w") as c:
        c.write(decoded)
