# 🛡️ End-to-End Network Security: Phishing Website Detection

An end-to-end **Machine Learning and MLOps** project for detecting phishing websites using URL and website-based features. The project follows an industry-standard architecture with modular components, experiment tracking, cloud artifact storage, and deployment-ready design.

---

## 📌 Project Overview

Phishing websites are malicious websites designed to steal sensitive user information by impersonating legitimate websites. This project builds a Machine Learning system capable of classifying websites as **Legitimate** or **Phishing** based on various URL and website-related features.

The project demonstrates a complete **production-ready MLOps workflow**, including:

- Data Ingestion from MongoDB
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation
- MLflow Experiment Tracking
- DagsHub Integration
- AWS S3 Artifact Storage
- FastAPI Deployment
- CI/CD using GitHub Actions

---

# 🎯 Objectives

- Build an end-to-end Machine Learning pipeline.
- Automate data ingestion from MongoDB.
- Validate incoming datasets.
- Transform and preprocess data.
- Train multiple Machine Learning models.
- Select the best performing model.
- Track experiments using MLflow.
- Store trained models and artifacts in AWS S3.
- Deploy the model using FastAPI.
- Automate deployment using GitHub Actions.

---

# ⚙️ Technologies Used

- **Python 3.11**
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- CatBoost
- MLflow
- DagsHub
- MongoDB
- AWS S3
- FastAPI
- Docker
- GitHub Actions
- PyYAML
- ConfigBox (python-box)
- Ensure
- Joblib
- Logging

---

# 📋 Prerequisites

Before running the project, make sure the following software is installed:

- Python **3.11**
- Git
- MongoDB
- Docker (Optional)
- AWS Account
- DagsHub Account

Verify Python version:

```bash
python --version
```

Expected Output:

```text
Python 3.11.x
```

---

# 📂 Dataset

Dataset Used:

**phishingData.csv**

The dataset contains website and URL-related features used for phishing website detection.

## Features

| Feature |
|----------|
| having_IP_Address |
| URL_Length |
| Shortining_Service |
| having_At_Symbol |
| double_slash_redirecting |
| Prefix_Suffix |
| having_Sub_Domain |
| SSLfinal_State |
| Domain_registeration_length |
| Favicon |
| port |
| HTTPS_token |
| Request_URL |
| URL_of_Anchor |
| Links_in_tags |
| SFH |
| Submitting_to_email |
| Abnormal_URL |
| Redirect |
| on_mouseover |
| RightClick |
| popUpWidnow |
| Iframe |
| age_of_domain |
| DNSRecord |
| web_traffic |
| Page_Rank |
| Google_Index |
| Links_pointing_to_page |
| Statistical_report |

### Target Column

```
Result
```

- **1 → Legitimate Website**
- **-1 → Phishing Website**

---

# 📂 Project Structure

```
NetworkSecurity/
│
├── artifacts/
│
├── config/
│   └── config.yaml
│
├── notebook/
│
├── networksecurity/
│   │
│   ├── components/
│   │      data_ingestion.py
│   │      data_validation.py
│   │      data_transformation.py
│   │      model_trainer.py
│   │      model_evaluation.py
│   │      model_pusher.py
│   │
│   ├── config/
│   │      configuration.py
│   │
│   ├── entity/
│   │
│   ├── pipeline/
│   │
│   ├── utils/
│   │
│   ├── exception/
│   │
│   └── logging/
│
├── app.py
├── main.py
├── params.yaml
├── schema.yaml
├── requirements.txt
└── README.md
```

---

# 🚀 End-to-End Workflow

```
                   MongoDB
                      │
                      ▼
──────────────────────────────────
      Data Ingestion
──────────────────────────────────
Read Dataset
Train-Test Split
Store Raw Data
                      │
                      ▼
──────────────────────────────────
      Data Validation
──────────────────────────────────
Validate Schema
Check Missing Columns
Check Data Drift
                      │
                      ▼
──────────────────────────────────
    Data Transformation
──────────────────────────────────
Data Cleaning
Feature Engineering
Scaling
Preprocessing
                      │
                      ▼
──────────────────────────────────
      Model Training
──────────────────────────────────
Train Multiple Models

• Logistic Regression
• Decision Tree
• Random Forest
• Gradient Boosting
• AdaBoost
• XGBoost
• CatBoost

Select Best Model
                      │
                      ▼
──────────────────────────────────
     Model Evaluation
──────────────────────────────────
Accuracy
Precision
Recall
F1 Score

Log Experiments to MLflow
                      │
                      ▼
──────────────────────────────────
      Model Pusher
──────────────────────────────────
Upload Artifacts
to AWS S3 Bucket
                      │
                      ▼
──────────────────────────────────
      FastAPI Deployment
──────────────────────────────────
Prediction API
```

---

# ☁️ AWS S3 Artifact Storage

After successful model training and evaluation, the pipeline uploads important artifacts to an **Amazon S3 Bucket**.

Artifacts uploaded include:

- Trained Model (`model.pkl`)
- Preprocessor (`preprocessor.pkl`)
- Model Metrics
- Pipeline Artifacts
- Configuration Files (optional)

Benefits:

- Centralized artifact storage
- Easy model version management
- Cloud accessibility
- Simplified deployment
- Production-ready workflow

---

# 📊 Pipeline Components

## 1️⃣ Data Ingestion

Responsible for:

- Connecting to MongoDB
- Reading the dataset
- Exporting the dataset
- Train-Test Split
- Saving artifacts

Output:

```
train.csv
test.csv
```

---

## 2️⃣ Data Validation

Performs:

- Schema Validation
- Missing Column Check
- Data Drift Detection
- Dataset Validation

Output:

```
validation_status.txt
```

---

## 3️⃣ Data Transformation

Performs:

- Feature Selection
- Data Cleaning
- Scaling
- Data Preprocessing

Outputs:

```
transformed_train.npy
transformed_test.npy
preprocessor.pkl
```

---

## 4️⃣ Model Training

Trains multiple Machine Learning algorithms:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- AdaBoost
- XGBoost
- CatBoost

Selects the best-performing model based on evaluation metrics.

Outputs:

```
model.pkl
metrics.json
```

---

## 5️⃣ Model Evaluation

Evaluates the trained model using:

- Accuracy
- Precision
- Recall
- F1 Score

Logs:

- Metrics
- Parameters
- Artifacts
- Models

using **MLflow**.

---

## 6️⃣ Model Pusher

Uploads the best model and associated artifacts to an **AWS S3 Bucket**.

Uploaded artifacts:

- model.pkl
- preprocessor.pkl
- Metrics
- Metadata

---

# 📈 MLOps Features

- End-to-End Machine Learning Pipeline
- Modular Project Structure
- Configuration Driven Development
- Custom Logging
- Custom Exception Handling
- YAML Configuration Files
- MongoDB Data Source
- Data Drift Detection
- Multiple Model Comparison
- Hyperparameter Tuning
- MLflow Experiment Tracking
- DagsHub Integration
- AWS S3 Artifact Storage
- FastAPI Deployment
- Docker Support
- GitHub Actions CI/CD
- Production-Ready Architecture

---

# ⚙️ Configuration Files

### config.yaml

Stores project paths and artifact locations.

### schema.yaml

Contains dataset schema used during validation.

### params.yaml

Contains model hyperparameters.

---

# 📦 Utility Functions

Reusable utility functions include:

- read_yaml()
- create_directories()
- save_json()
- load_json()
- save_bin()
- load_bin()
- evaluate_models()

---

# ▶️ Installation

## Clone Repository

```bash
git clone <repository-url>
```

Move to project directory

```bash
cd NetworkSecurity
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Verify Python Version

```bash
python --version
```

Install Required Packages

```bash
pip install -r requirements.txt
```

Run the Training Pipeline

```bash
python main.py
```

Run FastAPI Server

```bash
uvicorn app:app --reload
```

---

# ⭐ Key Features

- End-to-End MLOps Pipeline
- MongoDB Data Ingestion
- Data Validation & Drift Detection
- Automated Data Transformation
- Multiple ML Model Comparison
- Hyperparameter Tuning
- MLflow Experiment Tracking
- DagsHub Integration
- AWS S3 Artifact Storage
- FastAPI REST API
- Docker Support
- GitHub Actions CI/CD
- Modular & Scalable Architecture

---

# 📌 Future Enhancements

- Kubernetes Deployment
- Airflow Pipeline Automation
- Model Monitoring Dashboard
- Automated Retraining
- Drift Monitoring
- Grafana & Prometheus Integration
- Email Notifications
- Real-time Streaming Predictions

---

# 👨‍💻 Author

**Aftabalam Makandar**

AI/ML Intern | Machine Learning & NLP Enthusiast

---

# 🙏 Acknowledgement

This project was developed as part of learning **Machine Learning Engineering** and **MLOps**, implementing a production-ready phishing website detection system.