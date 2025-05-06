from sklearn.model_selection import train_test_split

def split_data(df, target_column='Result', test_size=0.3, random_state=42):
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)