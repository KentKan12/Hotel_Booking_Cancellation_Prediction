# 🏨 Hotel Booking Cancellation Predictor & Risk Analysis

An end-to-end Data Science project focusing on predicting hotel booking cancellations.  
This project covers **Exploratory Data Analysis (EDA)**, model training, hyperparameter tuning with **LightGBM**, custom threshold optimization, and deployment into an interactive **Streamlit** web application.

🔗 **Demo:** [hotelbookingcancellationprediction.streamlit.app](https://hotelbookingcancellationprediction.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LightGBM](https://img.shields.io/badge/LightGBM-Tuned-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-F7931E)

---

## 📌 Project Overview & Workflow

This project follows a complete Data Science pipeline designed to tackle high cancellation rates in the hospitality industry:

1. **Exploratory Data Analysis (EDA):** Identify patterns in guest lead times, booking channels, cancellation trends, and customer demographics.
2. **Model Building & Experimentation:** Train and evaluate multiple classification algorithms to establish a strong baseline.
3. **Hyperparameter Tuning & Threshold Optimization:** Fine-tune a **LightGBM (LGBM)** classifier and apply optimal thresholding to minimize false negatives (costly unpredicted cancellations) while maintaining high accuracy.
4. **Streamlit Deployment:** Deploy the tuned LightGBM model into a user-friendly web interface for real-time inference and business reporting.

---

## 📊 Dataset Source

- **Dataset Name:** [Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) by Jesse Mostipak
- **Description:** Contains booking information for a city hotel and a resort hotel, including booking date, length of stay, number of adults/children, country, market segment, and cancellation status.

---

## 💡 Key Application Features

- 🛡️ **Single Guest Risk Predictor:** Input reservation details manually to get real-time cancellation probabilities with risk levels (Low, Medium, High).
- 📋 **Batch Prediction & Export:** Upload/process datasets in bulk, view formatted risk tables, and export result summaries for reporting.
- 🎨 **Clean & Responsive UI:** Customized Streamlit configurations for an intuitive and seamless user experience.

---

## 📂 Repository Structure

```text
hotel_booking_cancellation_classification/
│
├── .streamlit/
│   └── config.toml          # Custom Streamlit UI theme settings
│
├── dataset/                 # Raw and processed datasets
│   └── hotel_bookings.csv
│
├── notebook/                # Jupyter Notebooks for EDA & Modeling
│   └── hotel_cancellation_eda_modeling.ipynb
│
├── models/                  # Saved tuned LightGBM model & threshold artifacts
│   └── model.pkl
│
├── streamlit/               # Main Streamlit web application
│   └── app.py
│
├── .gitignore               # Ignored files for Git version control
├── README.md                # Project documentation
└── requirements.txt         # Required Python dependencies


To run the Streamlit app locally, follow these steps (all combined in one command block):

bash
# 1. Clone Repository
git clone https://github.com/USERNAME_KAMU/hotel-cancellation-prediction.git
cd hotel-cancellation-prediction

# 2. (Optional) Create a Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Run the Streamlit App
streamlit run streamlit/app.py

Tech Stack & Libraries:
Language: Python

Machine Learning: LightGBM, Scikit-Learn

Web Framework: Streamlit

Data Manipulation: Pandas, NumPy

Data Visualization: Plotly, Seaborn, Matplotlib
```
