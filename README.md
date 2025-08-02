# House Price Prediction Pipeline

This repository contains an **end-to-end Machine Learning pipeline** for predicting house prices using **ZenML** for orchestration and **MLflow** for experiment tracking.

---

## Project Overview

The pipeline automates the following stages:

1. **Data Ingestion** – Reads raw housing data from a `.zip` archive.
2. **Missing Value Handling** – Supports strategies like:
   - Drop missing values
   - Fill using mean, median, mode, or a constant
3. **Feature Engineering** – Performs:
   - Log transformation
   - Min-Max Scaling
   - Standard Scaling
   - One-Hot Encoding
4. **Outlier Detection** – Removes extreme values from key features.
5. **Data Splitting** – Splits dataset into **train/test** sets.
6. **Model Building** – Trains a regression model (Random Forest or other sklearn models).
7. **Model Evaluation** – Calculates metrics like **MSE** and logs them to MLflow.

The project is built on **ZenML** to manage ML pipelines and artifacts efficiently.

---

## Project Structure
```
house\_Price\_Prediction/
│
├── data/                      \# Dataset archive
├── steps/                     \# ZenML steps for each pipeline stage
│   ├── data\_ingestion\_steps.py
│   ├── handle\_missing\_values\_steps.py
│   ├── feature\_engineering\_step.py
│   ├── outlier\_detection\_step.py
│   ├── data\_splitter\_step.py
│   ├── model\_builder\_step.py
│   └── model\_evaluator\_step.py
│
├── src/                       \# Core ML logic
│   ├── handle\_missing\_values.py
│   ├── feature\_engineering.py
│   ├── data\_splitter.py
│   ├── model\_builder.py
│   └── model\_evaluator.py
│
├── pipelines/
│   └── training\_pipeline.py    \# Main ZenML pipeline definition
│
├── mlruns/                     \# MLflow experiment storage
├── requirements.txt
└── README.md
```


## Installation & Setup

1. Clone the Repository

git clone https://github.com/ndangi168/house_Price_Prediction.git
cd house_Price_Prediction

2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install Dependencies

pip install -r requirements.txt


⸻

## Requirements

Here’s the exact requirements.txt for reproducibility:

###  Core Python
	•	pandas==2.2.2
	•	numpy==1.26.4
	•	scikit-learn==1.4.2

###  ZenML & MLflow
	•	zenml[server]==0.64.0
	•	mlflow==2.14.1

###  Visualization & Logging (optional but recommended)
	•	matplotlib==3.8.4
	•	seaborn==0.13.2
	•	loguru==0.7.2

###  For handling compressed datasets
	•	zipfile36==0.1.3

###  For Jupyter or Notebook runs (optional)
	•	jupyter==1.0.0
	•	ipykernel==6.29.4


⸻

## Running the Pipeline

Initialize ZenML:

1. zenml init

Start ZenML Local Dashboard (macOS users set the env variable first):

2. export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES 
3. zenml up

Run the Pipeline:

4. python pipelines/training_pipeline.py

Track Experiments in MLflow:
If not using ZenML Pro, run MLflow manually:

5. mlflow ui --host 127.0.0.1 --port 5000

Then open http://127.0.0.1:5000.

⸻

## Features
	•	End-to-end automated ML pipeline
	•	Configurable feature engineering and missing value handling
	•	Built-in outlier detection
	•	MLflow integration for experiment tracking
	•	Modular ZenML step-based design

⸻

## Tech Stack
	•	Python 3.9+
	•	ZenML 0.64
	•	MLflow
	•	Scikit-learn
	•	Pandas / NumPy

⸻

## Example Metrics

The pipeline evaluates the model using:
	•	Mean Squared Error (MSE)
	•	R² Score

All metrics and models are logged in MLflow.

⸻