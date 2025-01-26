import spacy
from spacy.tokens import DocBin
import json

nlp = spacy.blank("ja")
with open("./annotations/project-5-at-2025-01-26-03-15-8ab6fbd3.json", encoding="utf-8") as f:
    training_data = json.loads(f.read())

db = DocBin()
for annotation in training_data:
    doc = nlp(annotation["text"])
    ents = []
    for label in annotation["label"]:
        span = doc.char_span(label["start"], label["end"], label["labels"][0])
        if span is not None:
            ents.append(span)
    doc.ents = ents
    db.add(doc)

db.to_disk("./train.spacy")
db.to_disk("./dev.spacy")
