import pandas as pd
import Levenshtein as lev
from unidecode import unidecode

class Similarity:

    def __init__(self, name, threshold):

        self.name=unidecode(''.join(char for char in name if char.isalnum())).lower()
        self.threshold=threshold

        dataframe=pd.read_csv(r'names_dataset.csv', sep=",")
        dataframe["full_name_cleansed"]=dataframe["Full Name"].map(lambda x: ''.join(char for char in x if (char.isalnum() or char in [" ", "."])))
        dataframe["full_name_transformed"]=dataframe["Full Name"].map(lambda x: unidecode(''.join(char for char in x if char.isalnum())).lower())
        
        self.dataset=dataframe[["ID", "full_name_cleansed", "full_name_transformed"]]

    def similarity_percentage(self):

        results={}
        for i in range(0,len(self.dataset)):
            names={}
            distance = lev.distance(self.name, self.dataset["full_name_transformed"][i])
            max_length = max(len(self.name), len(self.dataset["full_name_transformed"][i]))
            if max_length == 0:
                return 100.0
            similarity = (1 - distance / max_length) * 100
            if similarity>=self.threshold:
                names["name"]=self.dataset["full_name_cleansed"][i]
                names["similarity"]=similarity
                results[int(self.dataset["ID"][i])]=names

        return dict(sorted(results.items(), key=lambda item: item[1]['similarity'], reverse=True))

