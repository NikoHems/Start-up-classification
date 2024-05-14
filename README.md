# Startup Success Prediction

This repository contains a machine learning application aimed at predicting the success of startups using a binary classification approach.

## Repository Structure

- **Data/**: Contains the dataset used for training and validation.
- **README.md**: Documentation for the repository.
- **app.py**: Streamlit application for model deployment.
- **main.ipynb**: Jupyter Notebook containing data cleaning, EDA, feature engineering, and model training.
- **requirements.txt**: List of Python dependencies required to run the project.

## Installation

### Requirements

A list of Python dependencies is listed in `requirements.txt`. They can be installed with pip:
```bash
pip install -r requirements.txt
```

### Data

We use the following dataset:

- [Crunchbase Startup Investments Dataset](https://www.kaggle.com/datasets/arindam235/startup-investments-crunchbase/data). This dataset underwent thorough data cleaning, exploratory data analysis (EDA), and feature engineering to optimize the inputs for model training.

## Project Overview

I developed a machine learning application aimed at predicting the success of startups using a binary classification approach. The model was trained on a comprehensive dataset from Crunchbase.

### Why Did I Do This Project?

Venture capitalists often have a hard time selecting successful startups. They often search long on Crunchbase. To help them, I thought of building a classification model that helps select successful startups.

### Models

I explored and deployed seven different models to ensure robustness and reliability of the predictions. The models included:

- Logistic Regression
- Decision Trees
- K-Nearest Neighbors (KNN)
- CatBoost
- Random Forest
- XGBoost
- Neural Network (developed using PyTorch)

### Outcome

Among the models tested, the best-performing model (XGBoost) achieved an impressive F1 score of 86%, indicating a high level of accuracy in predicting startup success.

### Deployment

The final deployment of the model was done through a Streamlit app, providing a user-friendly interface that allows easy interaction with the predictive system.

## License

This project is licensed under the MIT License.
