import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load the data from a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def normalize_features(train_df: pd.DataFrame, test_df: pd.DataFrame, feature_type: int) -> pd.DataFrame:
    """Normalize the test features based on the mean and std of the train features."""
    train_features = train_df.filter(regex=f'feature_type_{feature_type}_\d+')
    test_features = test_df.filter(regex=f'feature_type_{feature_type}_\d+')
    
    mean_train, std_train = train_features.mean(), train_features.std()
    test_df[test_features.columns + "_stand"] = (test_features - mean_train) / std_train
    
    return test_df

def compute_max_index(test_df: pd.DataFrame, feature_type: int) -> pd.DataFrame:
    """Compute the maximum value and index of each row in the feature_type_{i} columns of the test DataFrame."""
    features = test_df.filter(regex=f'feature_type_{feature_type}_\d+_stand')
    test_df[f"max_feature_type_{feature_type}_index"] = features.idxmax(axis=1).str.extract('(\d+)').astype(int)
    return test_df

def save_data(test_df: pd.DataFrame, feature_type: int) -> None:
    """Save the transformed test DataFrame into a new file test_transformed.csv."""
    output_file = f"test_transformed_feature_type_{feature_type}.csv"
    columns_to_save = ["id_job"] + list(test_df.filter(regex=f'feature_type_{feature_type}_\d+_stand')) + [f"max_feature_type_{feature_type}_index"]
    test_df[columns_to_save].to_csv(output_file, index=False)

def process_data(feature_type: int, train_file: str, test_file: str) -> None:
    """Process the data and save the transformed test data."""
    train_df, test_df = load_data(train_file), load_data(test_file)

    test_df = normalize_features(train_df, test_df, feature_type)
    test_df = compute_max_index(test_df, feature_type)
    save_data(test_df, feature_type)
    
# Example usage for creating type "1" features
if __name__ == "__main__":
    process_data(feature_type=1, train_file="train.csv", test_file="test.csv")