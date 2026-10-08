# Build and Deploy Machine Learning
This repository contains a comprehensive set of machine learning experiments covering data preprocessing, supervised learning, unsupervised learning, deep learning, and deployment. Each experiment is self-contained within its own directory and includes data generation, model training, evaluation, and visualizations.

## Project Structure
- **Experiment_01_Environment_and_Preprocessing**: Data cleaning, handling missing values, encoding, and scaling.
- **Experiment_02_Supervised_Learning_SVM_RF**: Support Vector Machines and Random Forest classifiers.
- **Experiment_03_Decision_Trees**: Decision Tree implementation and evaluation.
- **Experiment_04_Advanced_Supervised_Learning**: Advanced SVM kernels and feature importance in Random Forests.
- **Experiment_05_Unsupervised_Learning_KMeans_PCA**: K-Means clustering and Principal Component Analysis.
- **Experiment_06_Neural_Networks_CNN**: Feedforward Neural Networks and Convolutional Neural Networks using TensorFlow/Keras.
- **Experiment_07_Generative_Models_GANs**: Generative Adversarial Networks trained on MNIST.
- **Experiment_08_Model_Evaluation_Improvement**: Hyperparameter tuning via Grid Search and k-fold cross-validation.
- **Experiment_09_REST_API_Docker**: Flask REST API for model deployment and containerization with Docker.

## Setup Instructions
To run these experiments locally, ensure you have Python 3.9+ installed and set up a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt # (Dependencies can be found in the setup instructions)
```

Each folder contains a `.ipynb` notebook which can be executed directly.
