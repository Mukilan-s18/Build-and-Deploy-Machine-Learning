# Build and Deploy Machine Learning

A comprehensive, production-grade collection of machine learning laboratory experiments and an end-to-end deployed mini-project covering data preprocessing, supervised learning, unsupervised learning, deep learning, hyperparameter optimization, REST API engineering, and containerization.

---

## Repository Architecture & Structure

Each experiment is self-contained within its own dedicated directory, featuring runnable Jupyter Notebooks (`.ipynb`), synthetic datasets, trained models, visual diagnostic outputs, and instructions.

```
├── .gitignore
├── README.md
├── Experiment_01_Environment_and_Preprocessing/
│   ├── data/
│   │   └── messy_dataset.csv
│   └── experiment.ipynb
├── Experiment_02_Supervised_Learning_SVM_RF/
│   ├── outputs/
│   │   ├── rf_confusion_matrix.png
│   │   └── svm_confusion_matrix.png
│   └── experiment.ipynb
├── Experiment_03_Decision_Trees/
│   ├── outputs/
│   │   ├── decision_tree_viz.png
│   │   └── dt_confusion_matrix.png
│   └── experiment.ipynb
├── Experiment_04_Advanced_Supervised_Learning/
│   ├── outputs/
│   │   ├── rf_feature_importances.png
│   │   └── svm_kernels_comparison.png
│   └── experiment.ipynb
├── Experiment_05_Unsupervised_Learning_KMeans_PCA/
│   ├── outputs/
│   │   └── kmeans_pca_visualization.png
│   └── experiment.ipynb
├── Experiment_06_Neural_Networks_CNN/
│   ├── outputs/
│   │   └── nn_comparison.png
│   └── experiment.ipynb
├── Experiment_07_Generative_Models_GANs/
│   ├── outputs/
│   │   ├── image_at_epoch_0001.png
│   │   ├── image_at_epoch_0002.png
│   │   └── image_at_epoch_0003.png
│   └── experiment.ipynb
├── Experiment_08_Model_Evaluation_Improvement/
│   ├── outputs/
│   │   └── cv_scores.png
│   └── experiment.ipynb
├── Experiment_09_REST_API_Docker/
│   ├── app/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   ├── model.pkl
│   │   └── requirements.txt
│   └── experiment.ipynb
└── Mini_Project_House_Price_Prediction/
    ├── app/
    │   ├── Dockerfile
    │   ├── app.py
    │   ├── model.pkl
    │   ├── requirements.txt
    │   ├── static/
    │   └── templates/
    │       └── index.html
    ├── data/
    │   ├── raw_house_data.csv
    │   └── processed_house_data.csv
    ├── models/
    │   └── best_house_price_model.pkl
    ├── outputs/
    │   ├── actual_vs_predicted.png
    │   ├── feature_importance.png
    │   ├── model_comparison.png
    │   └── residual_distribution.png
    ├── Documentation.md
    └── experiment.ipynb
```

---

## Detailed Experiments Breakdown

| Module | Title | Key Techniques & Algorithms | Primary Outputs |
| :--- | :--- | :--- | :--- |
| **Exp 01** | **Environment & Preprocessing** | Missing value imputation, Standard scaling, One-hot encoding, Scikit-learn Pipelines | Clean dataset & transformation pipelines |
| **Exp 02** | **Supervised Learning (SVM & RF)** | Linear Support Vector Machines, Random Forest classification | Confusion matrices & classification reports |
| **Exp 03** | **Classification with Decision Trees** | DecisionTreeClassifier, tree structure pruning, multiclass evaluation | Decision tree diagram & Confusion matrix |
| **Exp 04** | **Advanced Supervised Learning** | Kernel comparisons (RBF, Poly, Sigmoid, Linear), Random Forest feature importance | Feature importance ranking, kernel comparison bar charts |
| **Exp 05** | **Unsupervised Learning (K-Means & PCA)** | K-Means clustering, Principal Component Analysis (PCA) 2D projection | Cluster separation & Centroid projections |
| **Exp 06** | **Neural Networks & CNNs** | Feedforward Neural Networks (FNN), Convolutional Neural Networks (CNN) with TensorFlow/Keras | Training & validation loss/accuracy curves |
| **Exp 07** | **Generative Models with GANs** | Deep Convolutional Generative Adversarial Networks (DCGAN) on MNIST | Synthesized handwritten digit images per epoch |
| **Exp 08** | **Model Evaluation & Improvement** | K-Fold Cross-Validation, GridSearchCV hyperparameter optimization | Cross-validation fold score distribution |
| **Exp 09** | **REST API for Model Deployment** | Flask microservice API development, endpoint testing, Docker packaging | Microservice container & prediction endpoints |
| **Mini Project** | **End-to-End House Price Prediction** | Regression ensembles, Grid Search tuning, interactive UI, Flask REST API & Docker | Interactive valuation UI, full pipeline, Docker image |

---

## Mini Project Highlights

The **Smart Real Estate Valuator** mini-project represents a complete production-style ML lifecycle:
1. **Data Preparation**: Generated multi-attribute housing dataset; imputed missing data via median strategy; created engineered ratios (`total_rooms`, `room_to_area_ratio`).
2. **Model Comparison**: Benchmarked Linear Regression, Random Forest, and Gradient Boosting Regressors across MAE, RMSE, and $R^2$.
3. **Hyperparameter Tuning**: Utilized 5-Fold `GridSearchCV` on Gradient Boosting to optimize estimators, learning rates, and tree depths.
4. **REST API & Web UI**: Developed a Flask application offering both JSON REST endpoints (`/predict`, `/health`) and a web interface styled with modern CSS.
5. **Dockerization**: Provided a lightweight Docker configuration (`python:3.9-slim`) for containerized deployment.

---

## Local Development & Setup

### Prerequisites
- Python 3.9 or higher
- Git & Docker (optional, for containerization)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mukilan-s18/Build-and-Deploy-Machine-Learning.git
   cd Build-and-Deploy-Machine-Learning
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install jupyter jupytext nbconvert pandas numpy scikit-learn matplotlib seaborn tensorflow flask requests joblib
   ```

### Running the Mini Project Web App
```bash
cd Mini_Project_House_Price_Prediction/app
python app.py
```
Open your browser and navigate to `http://localhost:5000` to interact with the web interface.

### Running via Docker
```bash
cd Mini_Project_House_Price_Prediction/app
docker build -t house-price-predictor .
docker run -p 5000:5000 house-price-predictor
```

---

## Course Learning Outcomes Met
- Mastered the lifecycle and components of machine learning development.
- Acquired hands-on experience across multiple ML frameworks (Scikit-Learn, TensorFlow, Keras).
- Solved architectural design issues in model packaging, persistence, and feature leakage prevention.
- Containerized models and built production-ready REST APIs.
