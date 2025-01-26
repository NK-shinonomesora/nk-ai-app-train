from datasets import load_dataset
from pprint import pprint
from collections import Counter
import pandas as pd
from datasets import Dataset

dataset = load_dataset("llm-book/ner-wikipedia-dataset", trust_remote_code=True)

def count_label_occurrences(dataset: Dataset) -> dict[str, int]:
    """固有表現タイプの出現回数をカウント"""
    # 各事例から固有表現タイプを抽出したlistを作成する
    entities = [
        e["type"] for data in dataset for e in data["entities"]
    ]

    # ラベルの出現回数が多い順に並び替える
    label_counts = dict(Counter(entities).most_common())
    return label_counts

label_counts_dict = {}
for split in dataset:
    label_counts_dict[split] = count_label_occurrences(dataset[split])

# DataFrame形式で表示する
df = pd.DataFrame(label_counts_dict)
df.loc("合計") = df.sum()
display(df)