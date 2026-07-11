# 🏨 Hotel Booking Cancellation Prediction

An end-to-end Machine Learning project to predict hotel booking cancellations at the time of initial booking creation using advanced gradient boosting techniques and business-driven threshold optimization.

## 📌 Project Overview
This repository contains a comprehensive data science workflow designed to help the hospitality industry mitigate revenue losses caused by sudden booking cancellations. By evaluating **9 baseline models** and adjusting thresholds based on hotel seasonality and business dynamics, this project bridges the gap between raw data and actionable revenue management strategies.

## 📂 Repository Structure
```text
hotel-booking-cancellation/
├── data/
│   └── hotel_bookings.csv          # Raw dataset (not uploaded due to size)
├── notebooks/
│   └── hotel_booking_prediction.ipynb # Full Jupyter Notebook with analysis & code
├── README.md                       # Documentation & Project Report
└── requirements.txt                # Project dependencies
```

## 📖 Business Background & Problems
Sudden booking cancellations severely disrupt hotel operations and revenue streams. If a hotel holds a room for a guest who eventually cancels (*False Negative*), it suffers an **opportunity loss**. Conversely, if a hotel aggressively overbooks assuming a guest will cancel when they actually show up (*False Positive*), it causes an **overbooking disaster**, leading to expensive walk-in relocation costs, compensation, and reputation damage.

Our goal is to build a predictive framework operating **precisely at the moment of booking creation** to anticipate cancellations and guide strategic overbooking.

## 💡 Key Insights & Feature Engineering
Advanced engineering techniques were implemented to extract hidden signals and combat **Data Leakage** (e.g., removing post-booking variables like `reservation_status`, `assigned_room_type`, and `booking_changes`):
1. **The Non-Refund Paradox (Visa Fraud Suspect):** Bookings with *Non-Refundable* deposits surprisingly showed a near 100% cancellation rate under specific combinations (International guests via TA/TO or Groups channels). This exposes fake booking syndicates used purely for overseas visa documentation. We engineered `visa_fraud_suspect` to isolate this behavioral bias.
2. **The Golden Rule of Parking (`has_parking_request`):** Guests who requested a parking space showed a **0% cancellation rate**. This binary indicator serves as the strongest proof of real intent to stay.
3. **Patures Repeat Itself (`is_repeated_guest_refined`):** Over 90% of guests who had canceled in the past canceled their current booking. Past anomalies where guests had successful stays but weren't flagged as repeated guests were corrected.
4. **Junction of Risk (`segment_channel_risk`):** Cross-tabulations between Market Segments and Distribution Channels mapped distinct risk zones. Group bookings via TA/TO represent an extreme hazard (>65% cancel rate).

## 📊 Model Performance Evaluation
9 tree-based and ensemble baseline algorithms were evaluated with built-in class balancing (`class_weight='balanced'`). The top-tier models were further optimized via `RandomizedSearchCV` and `TimeSeriesSplit`.

### The 3 Major Contenders:
1. **Baseline LightGBM (Threshold 0.50):** Delivered the highest raw **Accuracy (80.06%)** and excellent Precision (73.58%), but was conservative in capturing cancellations (Recall 80.32%).
2. **Optimized HistGradientBoosting (Threshold 0.39):** Extremely aggressive in capturing cancellations, achieving the highest **Recall (90.78%)**, but suffered a heavy drop in Precision (67.12%).
3. **Optimized LightGBM (Threshold 0.42):** The ultimate **Sweet Spot** for general operations, scoring the highest overall **F1-Score (0.7745)** with a balanced Recall of **87.32%** and a controlled Precision decline (69.58%).

## 💼 Business Strategy & Recommendations
Instead of sticking to a rigid single model, hotel revenue managers can shift thresholds dynamically based on **Hotel Kunjungan Keterisian (Seasonality)**:

* **General/Daily Operations 🟩 (LightGBM @ 0.42):** Captures 87.32% of actual cancellations while minimizing overbooking risks. This protects general daily revenue and guest satisfaction.
* **High-Season Periods 🟥 (HistGradientBoosting @ 0.39):** During extreme high-demand holidays (Lebaran, Christmas), capturing every cancellation is top priority (**Recall 90.78%**). Re-selling canceled rooms is instantaneous due to massive walk-in queues.
* **Low-Season Periods 🟨 (Baseline LightGBM @ 0.50):** When hotel occupancy is low, every single guest counts. High **Precision (73.58%)** ensures no real guest is accidentally denied a room due to false overbooking calculations.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hotel-booking-cancellation.git
   cd hotel-booking-cancellation
   ```

2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook:**
   Launch your Jupyter environment and open `notebooks/hotel_booking_prediction.ipynb` to inspect full visualizations, statistical tests, and modeling arrays.

---
*Project created as part of Advanced Analytics & Data Modeling Optimization.*
