## Start-up classification modelStart-up classification model

I developed a machine learning application aimed at predicting the success of startups using a binary classification approach. The model was trained on a comprehensive dataset from Crunchbase, which can be viewed here: https://www.kaggle.com/datasets/arindam235/startup-investments-crunchbase/data. This dataset underwent thorough data cleaning, exploratory data analysis (EDA), and feature engineering to optimize the inputs for model training.

I explored and deployed seven different models to ensure robustness and reliability of the predictions. The models included Logistic Regression, Decision Trees, K-Nearest Neighbors (KNN), CatBoost, Random Forest, and XGBoost, all implemented using Scikit-learn. Additionally, a Neural Network model was developed using PyTorch to harness deep learning capabilities. 

The final deployment of the model was done through a Streamlit app, providing a user-friendly interface that allows easy interaction with the predictive system. Among the models tested, the best-performing model (XGBoost) achieved an impressive F1 score of 86%, indicating a high level of accuracy in predicting startup success.
