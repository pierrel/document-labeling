import numpy
import itertools

from training.dataprep.airbnb_example import AirbnbExample
from training.trainer import Trainer
from training.model import DocLabelingModel

example = AirbnbExample(file_path="/path/to/file.csv")
texts = numpy.array([i for i in example.texts()])
labels = numpy.array([i for i in example.labels()])

eval_train_index = len(texts)-50

train_texts = texts[:eval_train_index]
eval_texts = texts[eval_train_index:]
train_labels = labels[:eval_train_index]
eval_labels = labels[eval_train_index:]

model = DocLabelingModel(len(labels[0]))
trainer = Trainer(model.model)

model = trainer.train(train_texts, train_labels)
print(trainer.evaluate(eval_texts, eval_labels))

# simple experiment
predictions = model.predict(eval_texts)
results = [(example.read_prediction(i), example.read_prediction(j)) for (i, j) in zip(predictions, eval_labels)]
for result in results:
    print(result, "\n")


