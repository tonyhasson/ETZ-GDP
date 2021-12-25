from imports import *

def load_dataset(file_name, label_column):
    df = pd.read_csv(file_name)

    TRAINING_FEATURES = df.columns[df.columns != label_column]
    TARGET_FEATURE = label_column

    X = df[TRAINING_FEATURES]
    y = df[TARGET_FEATURE]

    return X,y


