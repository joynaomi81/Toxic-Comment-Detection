# Toxic-Comment-Detection
This project focuses on detecting and classifying toxic comments such as hate speech, toxic comments, non- toxic comments, etc.

# Dataset
Toxic Comments Classification dataset sourced from kaggle was used for this project. The dataset shape contains 20,000 rows and 2 columns,which includes comments text column and toxic column which is the label (1= Toxic, 0=Non_toxic)

# Data preprocessing
Text Normalization

* Lowering text.
* Tokenization .
* Stemming.
* Removing stopwords.
* Removing punctuation.
  

* Vectorization

This is the process of converting text into numerical vectors. For this project, Term Frequency-Inverse Document Frequency (TF-IDF) was used.

# Model Training
Naive Bayes was used in this project. The model was trained using Term Frequency-Inverse Document Frequency (TF-IDF) representation. The Naive Bayes classifier is used to classify the text into toxic or non toxic categories.

# Model Evaluation
The classification report and accuracy of the Naive Bayes model includes:

Accuracy: 0.89932, meaning the model detected the comment_text correctly for approximately 89% of the comments_text samples

Classification Report:
              precision    recall  f1-score   support

           0       0.92      0.88      0.90      1994
           1       0.88      0.92      0.90      1999

    accuracy                           0.90      3993
   macro avg       0.90      0.90      0.90      3993
weighted avg       0.90      0.90      0.90      3993


