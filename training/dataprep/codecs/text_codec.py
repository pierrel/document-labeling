import codecs
import types

from training.dataprep.codecs.word_codec import WordCodec

class TextCodec(codecs.Codec):
    """
    Encodes a string of distinct words

    Encodes a string by splitting by word into an array
    """
    PADDING = "<PAD>"

    def __init__(self):
        self.word_codec = WordCodec()
        self.word_codec.encode(self.PADDING) # 0 reserved is for padding
    
    def encode(self, input, errors='strict') -> str:
        words = input.split(' ')
        return [self.word_codec.encode(word) for word in words]

    def decode(self, input, errors='strict') -> str:
        return ' '.join([self.word_codec.decode(number) for number in input])
