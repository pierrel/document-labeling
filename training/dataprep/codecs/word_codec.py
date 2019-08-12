import codecs

class WordCodec(codecs.Codec):
    """
    Encodes a unique string to a unique number
    """
    def __init__(self):
        self.counter: int = 0
        self.encode_map: dict = {}
        self.decode_map: dict = {}
    
    def encode(self, input: str, errors='strict') -> int:
        self.addWord(input)
        return self.encode_map.get(input) 

    def decode(self, input: int, errors='strict') -> str:
        return self.decode_map.get(input)

    def addWord(self, word: str) -> None:
        if self.encode_map.get(word, None) == None:
            self.encode_map.update({word: self.counter})
            self.decode_map.update({self.counter: word})
            self.counter += 1

