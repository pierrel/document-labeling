from training.dataprep.airbnb_example import AirbnbExample
import numpy
import itertools

example = AirbnbExample(file_path="/Users/pierrelarochelle/Desktop/Categories_csv.csv")

print([i for i in itertools.islice(example.texts(), 0, 3)])
print([i for i in itertools.islice(example.labels(), 0, 100)])