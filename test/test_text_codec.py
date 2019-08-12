import unittest

from training.dataprep.codecs.text_codec import TextCodec

class TestTextCodec(unittest.TestCase):
    def test_padding(self):
        codec = TextCodec()

        assert codec.encode("<PAD>") == [0]
        assert codec.decode([0]) == "<PAD>"

    def test_initial_encoding(self):
        text = "this is the string the"
        output = [1, 2, 3, 4, 3]
        codec = TextCodec()
        assert codec.encode(text) == output

    def test_initial_decoding(self):
        text = "this is the string the"
        codec = TextCodec()
        encoded = codec.encode(text)
        assert codec.decode(encoded) == text

    def test_extra_encoding(self):
        initial_text = "this is the string the"
        extra_text = "more to the encoding"
        codec = TextCodec()

        codec.encode(initial_text)
        encoded = codec.encode(extra_text)

        assert encoded == [5, 6, 3,7]
    
    def test_extra_decoding(self):
        initial_text = "this is the string the"
        extra_text = "more to the encoding" 
        codec = TextCodec()

        codec.encode(initial_text)
        encoded = codec.encode(extra_text)

        assert codec.decode(encoded) == extra_text
