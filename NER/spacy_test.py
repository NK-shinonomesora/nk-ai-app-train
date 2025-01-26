# pip install -U spacy
# python -m spacy download ja_core_web_sm
import spacy
from spacy.tokens import Span

nlp = spacy.load("./output/model-last")

txt = "私の得意なプログラミング言語はC言語とJavaとPythonです。データベースはMySQLとOracle DatabaseとMicrosoft SQL Serverを使用しています。Javaが一番相性がいいです。"
txt2 = "友人も最近PythonやMySQLに興味を持っており、プログラミング言語ではC++が苦手と感じているそうです。WebサーバとしてNginxを使用しています。"

def pred(doc):
    result = {}
    for ent in doc.ents:
        newData = {}
        newData[ent.text] = ent.label_
        result = {**result, **newData}
    return result

doc = nlp(txt)
doc2 = nlp(txt2)

result1 = pred(doc)
result2 = pred(doc2)

lastResult = {**result1, **result2}

for key, value in lastResult.items():
    print(f"key = {key}, value = {value}")
