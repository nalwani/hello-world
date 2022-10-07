import spacy

nlp = spacy.load("en_core_web_sm")


class Reader:

    def __init__(self):
        self.phrase = ""

    def read(self, phrase):
        self.phrase = phrase
        doc = nlp(self.phrase)
        # for token in doc:
        #     # read input
        #     print(token.text, token.pos_, token.dep_)
        print("Reading...")
