import os

class Translator:
    def __init__(self):
        self.alphabet = {
            "A": "ᔑ",
            "B": "ʖ",
            "C": "ᓵ",
            "D": "↸",
            "E": "ᒷ",
            "F": "⎓",
            "G": "⊣",
            "H": "⍑",
            "I": "╎",
            "J": "⋮",
            "K": "ꖌ",
            "L": "ꖎ",
            "M": "ᒲ",
            "N": "リ",
            "O": "𝙹",
            "P": "!¡",
            "Q": "ᑑ",
            "R": "∷",
            "S": "ᓭ",
            "T": "ℸ",
            "U": "⚍",
            "V": "⍊",
            "W": "∴",
            "X": "̇/",
            "Y": "||",
            "Z": "⨅"
        }
        self.type: str  # "FILE" or "STR"
        self.input: str # the STR or the filename
    
    def get_text(self):
        return self.input if self.type == "STR" else open(self.input, 'r', encoding="utf8").read()

    def translate(self, input: str, type="STR", to="mc"):
        """
        to mc (minecraft) or rw (real world)
        """
        self.type = type
        self.input = input
        text = self.get_text()
        for char in self.alphabet:
            if to == "mc":
                text = text.replace(char, self.alphabet[char])
                text = text.replace(char.lower(), self.alphabet[char])
            else:
                text = text.replace(self.alphabet[char], char.lower())
        self.handle_output(text)
        print("\n$ Done")

    def handle_output(self, text):
        if self.type == "STR":
            print(text)
        else:
            f =  open('output.txt', 'w', encoding="utf8")
            for line in text.split('\n'):
                f.write(line + "\n")
            f.close()

translator = Translator()
what = input("$ What do you want to translate ((F)ile / (T)yped text)?: ")
direction = input("$ Do you want to translate to or from minecraft? ((T)o / (F)rom)?: ")

to = "rw"
if direction.lower().startswith("t"):
    to = "mc"

if what.lower().startswith('f'):
    file_name = input("$ File name: ")
    translator.translate(file_name, "FILE", to=to)
else:
    os.system('cls')
    print("$ INPUT TEXT:\t\t(type ':q' to submit)")
    text = ""
    while True:
        inpt = input(">")
        if inpt.startswith(':q'):
            break
        text += inpt.replace("\\:q", ":q") + "\n"

    translator.translate(text, to=to)