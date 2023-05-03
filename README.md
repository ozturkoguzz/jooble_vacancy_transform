# jooble_vacancy_transform
This repo contains the solution for the jooble testcase which transform the sample data into the required format

The code relies on the Pandas library to perform data manipulation and transformation.

The `load_data()` function takes a file path as input and reads the data from a CSV file into a Pandas DataFrame. The function returns the loaded DataFrame.

The `normalize_features()` function takes two DataFrames as input, representing the training and test data, and a feature type integer. The function normalizes the test data features based on the mean and standard deviation of the corresponding training data features. The normalized test features are added as new columns to the test DataFrame. The function returns the modified test DataFrame.

The `compute_max_index()` function takes a test DataFrame and a feature type integer as input. The function computes the maximum value and index of each row in the columns of the test DataFrame that match the specified feature type. The computed indices are added as a new column to the test DataFrame. The function returns the modified test DataFrame.

The `save_data()` function takes a test DataFrame and a feature type integer as input. The function saves the transformed test DataFrame into a new CSV file with a filename that includes the specified feature type. The function saves only the columns related to the specified feature type.

The `process_data()` function takes a feature type integer, and the file paths for the training and test CSV files as input. The function loads the data from the CSV files into two DataFrames using the `load_data()` function. The function then applies the normalization and maximum index computations to the test data using the `normalize_features()` and `compute_max_index()` functions. Finally, the function saves the transformed test data using the `save_data()` function.

The example usage of the code in the `if __name__ == "__main__":` block calls the `process_data()` function with feature type 1, and the file paths for the training and test CSV files. The processed test data is saved into a new CSV file named "test_transformed_feature_type_1.csv".