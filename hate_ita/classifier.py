from transformers import Trainer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
from datasets import Dataset
import numpy as np
from typing import List
from hate_ita.dataset import prepare_dataset

class HateSpeechClassifier:

        def __init__(self, model="twitter-base"):
            if model == "twitter-base":
                self.tokenizer = AutoTokenizer.from_pretrained("MilaNLProc/hate-ita")
                self.model = AutoModelForSequenceClassification.from_pretrained("MilaNLProc/hate-ita")
            elif model == "base":
                    self.tokenizer = AutoTokenizer.from_pretrained("MilaNLProc/xlm-emo-t")
                    self.model = AutoModelForSequenceClassification.from_pretrained("MilaNLProc/hate-ita-xlm-r-base")
            elif model == "large":
                    self.tokenizer = AutoTokenizer.from_pretrained("MilaNLProc/xlm-emo-t")
                    self.model = AutoModelForSequenceClassification.from_pretrained("MilaNLProc/hate-ita-xlm-r-large")
            else:
                raise Exception("Not Yet Implemented")

        def predict(self, text: List):

            df = pd.DataFrame({"texts": text})

            train_dataset = Dataset.from_pandas(df)
            train_dataset = prepare_dataset(train_dataset, self.tokenizer)

            trainer = Trainer(model=self.model)

            local_results = np.argmax(trainer.predict(train_dataset)[0], axis=1)

            mapper = {0: "not-hate", 1: "hate"}

            return [mapper[k] for k in local_results]


