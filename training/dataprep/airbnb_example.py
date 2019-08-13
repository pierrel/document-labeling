import codecs
import csv
import numpy
from training.dataprep.data_source import DataSource
from training.dataprep.codecs.word_codec import WordCodec
from training.dataprep.codecs.text_codec import TextCodec


class AirbnbExample(DataSource):
    MAX_LEN = 128
    def __init__(self, file_path: str = None):
        self.file_path = file_path
        self.textCodec = TextCodec()
        self.labelCodec = WordCodec()

        # build the word space by encoding everything
        for (text, label) in self.text_label_from_file(file_path):
            self.textCodec.encode(text)
            self.labelCodec.encode(label)

        self.matrix_iden = numpy.identity(len(self.labelCodec.encode_map))

    def labels(self):
        for (_, label) in self.text_label_from_file(self.file_path):
            yield self.label_representation(label)
    
    def texts(self):
        for (text, _) in self.text_label_from_file(self.file_path):
            yield self.text_representation(text)
    
    def label_representation(self, label: str) -> numpy.ndarray:
        encoded = self.labelCodec.encode(label)
        return self.matrix_iden[encoded]

    def text_representation(self, text: str) -> numpy.ndarray:
        pre_pad = self.textCodec.encode(text)
        if len(pre_pad) >= self.MAX_LEN:
            return pre_pad[:self.MAX_LEN]
        else:
            return numpy.pad(pre_pad, (0,self.MAX_LEN-len(pre_pad)))
    
    def text_label_from_file(self, file_path):
        with open(self.file_path) as csv_file:
            reader = csv.reader(csv_file)
            for (text, label) in reader:
                yield (text, label)

    def read_prediction(self, single_prediction: numpy.ndarray):
        max_val = single_prediction.max()
        max_index = numpy.argmax(single_prediction)

        return (self.labelCodec.decode(max_index), max_val)