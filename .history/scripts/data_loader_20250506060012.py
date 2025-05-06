import pandas as pd
import arff

def load_data(filepath):
    with open(filepath, 'r') as f:
        dataset = arff.load(f)
    df = pd.DataFrame(dataset['data'], columns=[attr[0] for attr in dataset['attributes']])
    return df