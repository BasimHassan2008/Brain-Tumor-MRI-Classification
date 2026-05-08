import os

# Define the path to your training data folder in Google Drive (from kernel state)
train_data_path = '/content/drive/My Drive/Cancer Prediction/MRI SCAN DATASET/Training'
test_data_path = '/content/drive/My Drive/Cancer Prediction/MRI SCAN DATASET/Testing'

# List the contents of the training data path to verify
if os.path.exists(train_data_path):
    print(f"Contents of training folder '{train_data_path}':")
    for item in os.listdir(train_data_path):
        print(item)
else:
    print(f"The specified training path still does not exist: {train_data_path}")
    print("Please double-check the folder name 'Cancer Prediction/MRI SCAN DATASET/Training' in your Google Drive.")

# List the contents of the testing data path to verify
if os.path.exists(test_data_path):
    print(f"\nContents of testing folder '{test_data_path}':")
    for item in os.listdir(test_data_path):
        print(item)
else:
    print(f"\nThe specified testing path still does not exist: {test_data_path}")
    print("Please double-check the folder name 'Cancer Prediction/MRI SCAN DATASET/Testing' in your Google Drive.")