import unittest

from training.fileprep.codecs.word_codec import WordCodec

class TestWordCodec(unittest.TestCase):
    def test_initial_encoding(self):
        text = "this is the string the"
        output = 0
        codec = WordCodec()
        assert codec.encode(text) == output

    def test_initial_decoding(self):
        text = "this is the string the"
        codec = WordCodec()
        encoded = codec.encode(text)
        assert codec.decode(encoded) == text

    def test_extra_encoding(self):
        initial_text = "this is the string the"
        extra_text = "more to the encoding"
        codec = WordCodec()

        codec.encode(initial_text)
        encoded = codec.encode(extra_text)

        assert encoded == 1
    
    def test_extra_decoding(self):
        initial_text = "this is the string the"
        extra_text = "more to the encoding" 
        codec = WordCodec()

        codec.encode(initial_text)
        encoded = codec.encode(extra_text)

        assert codec.decode(encoded) == extra_text
