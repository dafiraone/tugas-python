# import cv2
# import numpy as np
# import os

# # Step 1: Define paths to your dataset folders
# dataset_path = "garbage_classification"
# garbage_types = ["paper", "cardboard", "biological", "plastic", "bottle-glass", "clothes", "shoes", "battery", "trash"]

# # Step 2: Extract HOG features from the dataset
# def extract_features(image):
#     # Resize image to fit HOG window size
#     win_size = (64, 128)
#     image_resized = cv2.resize(image, win_size)
    
#     # Initialize HOG descriptor
#     block_size = (16, 16)
#     block_stride = (8, 8)
#     cell_size = (8, 8)
#     nbins = 9
#     hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)
    
#     # Compute HOG features
#     features = hog.compute(image_resized)
#     return features.flatten()


# # Step 3: Prepare data and train SVM classifier
# def train_classifier():
#     features = []
#     labels = []
    
#     for idx, garbage_type in enumerate(garbage_types):
#         folder_path = os.path.join(dataset_path, garbage_type)
#         for image_name in os.listdir(folder_path):
#             image_path = os.path.join(folder_path, image_name)
#             image = cv2.imread(image_path)
#             if image is not None:
#                 hog_features = extract_features(image)
#                 features.append(hog_features)
#                 labels.append(idx)
    
#     features = np.array(features, dtype=np.float32)
#     labels = np.array(labels)
    
#     # Train SVM classifier
#     svm = cv2.ml.SVM_create()
#     svm.setType(cv2.ml.SVM_C_SVC)
#     svm.setKernel(cv2.ml.SVM_LINEAR)
#     svm.train(features, cv2.ml.ROW_SAMPLE, labels)
    
#     return svm

# # Step 4: Save trained classifier
# def save_classifier(svm, filename):
#     svm.save(filename)

# # Train the classifier
# print("Training classifier...")
# classifier = train_classifier()

# # Save the trained classifier
# classifier_filename = "garbage_classifier.xml"
# print("Saving classifier to", classifier_filename)
# save_classifier(classifier, classifier_filename)

# print("Classifier training and saving completed.")

import cv2
import numpy as np
import os
from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import joblib

def extract_hog_features(image):
    win_size = (64, 128)
    block_size = (16, 16)
    block_stride = (8, 8)
    cell_size = (8, 8)
    nbins = 9
    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)
    features = hog.compute(image)
    return features.flatten()

def load_dataset(dataset_path):
    data = []
    labels = []
    label_map = {"paper": 0, "cardboard": 1, "biological": 2, "plastic": 3, "bottle-glass": 4, "apparel": 5, "battery": 6, "trash": 7} # Add more classes as needed

    for label_name, label_id in label_map.items():
     folder_path = os.path.join(dataset_path, label_name)
     for filename in os.listdir(folder_path):
      if filename.endswith(".jpg"):
       file_path = os.path.join(folder_path, filename)
       image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
       image = cv2.resize(image, (64, 128))
       features = extract_hog_features(image)
       data.append(features)
       labels.append(label_id)
    
    return np.array(data), np.array(labels)

dataset_path = "garbage_classification"
data, labels = load_dataset(dataset_path)

print('start training')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

print("training")

# Train the SVM model with grid search for hyperparameter tuning
param_grid = {'C': [1, 10], 'kernel': ['linear', 'rbf']}
svm_model = svm.SVC(probability=True)

print("grid")

grid_search = GridSearchCV(svm_model, param_grid, cv=5, n_jobs=4)
grid_search.fit(X_train, y_train)
print("fitting")

# Create and train the SVM model
# svm_model = svm.SVC(kernel='linear', probability=True)
# svm_model.fit(X_train, y_train)

# Evaluate the model
print("predicting")
best_model = grid_search.best_estimator_
best_accuracy = grid_search.best_score_
print(f"Accuracy w/ grid {best_accuracy:.2f}%")

y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test best model: {accuracy:.2f}%")

# y_pred = svm_model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy * 100:.2f}%")


# Save the trained model
joblib.dump(grid_search, "garbage_classifier.pkl")