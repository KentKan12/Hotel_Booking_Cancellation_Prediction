import streamlit as st
import joblib
import pandas as pd
import numpy as np
import datetime
import plotly.express as px

# =========================================================
# 1. KONFIGURASI HALAMAN WEB & TEMA
# =========================================================
st.set_page_config(
    page_title="Hotel Insight Dashboard",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS berdasarkan "UI/UX REDESIGN PROMPT"
st.markdown("""
<style>

/* =======================================================
    GLOBAL & TYPOGRAPHY
======================================================= */
.stApp {
    background: #F8FAFC;
    font-family: 'Inter', sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    color: #0F172A !important;
}

h1 { font-weight: 800 !important; }
h2 { font-weight: 700 !important; }
h3 { 
    font-weight: 700 !important; 
    color: #1E293B !important; 
    border-bottom: 2px solid #E2E8F0; 
    padding-bottom: 0.5rem; 
    margin-top: 2rem;
}

p, span, small {
    color: #334155;
}

.subtitle-text {
    color: #64748B !important;
}

/* =======================================================
    LABEL FORM
======================================================= */
div[data-testid="stWidgetLabel"] label, div[data-testid="stWidgetLabel"] label p {
    color: #475569 !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
}

/* =======================================================
    INPUT COMPONENTS
======================================================= */
.stTextInput input, 
.stNumberInput input, 
.stDateInput input, 
.stTimeInput input, 
textarea {
    background: #FFFFFF !important;
    color: #334155 !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 8px !important;
    transition: all 0.25s ease !important;
    height: 42px !important;
}

div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 8px !important;
    color: #334155 !important;
    transition: all 0.25s ease !important;
}

/* Hover & Focus State */
input:hover, textarea:hover, div[data-baseweb="select"] > div:hover {
    border-color: #D97706 !important;
}

input:focus, textarea:focus, div[data-baseweb="select"] > div:focus-within {
    border-color: #D97706 !important;
    box-shadow: 0 0 0 3px rgba(217,119,6,0.15) !important;
}


/* =======================================================
    FILE UPLOADER STYLING & BUTTON COLOR
======================================================= */
/* Area Kotak Drag & Drop File Uploader */
section[data-testid="stFileUploaderDropzone"] {
    background-color: #FFFFFF !important; /* Ganti warna background di sini (misal: #FFFFFF atau #F1F5F9) */
    border: 2px dashed #CBD5E1 !important; /* Warna border putus-putus */
    border-radius: 12px !important;
    transition: all 0.25s ease !important;
}

/* Tampilan saat Mouse Mengambang (Hover) */
section[data-testid="stFileUploaderDropzone"]:hover {
    background-color: #FFFBEB !important; /* Warna background saat mouse mengambang di atasnya */
    border-color: #D97706 !important;     /* Warna border berubah jadi Emas/Amber saat di-hover */
}

/* Mengubah warna teks instruksi di dalam File Uploader */
section[data-testid="stFileUploaderDropzone"] span, 
section[data-testid="stFileUploaderDropzone"] small {
    color: #FFFFFF !important;
}

/* 1. Mengubah warna tulisan pada tombol "Browse files" */
section[data-testid="stFileUploaderDropzone"] button {
    background-color: #202A44 !important; /* Warna latar tombol (misal: Navy gelap) */
    border: 1px solid #0E1B2E !important;
    border-radius: 6px !important;
    color: #FFFFFF;
}

section[data-testid="stFileUploaderDropzone"] button,
section[data-testid="stFileUploaderDropzone"] button * {
    color: #FFFFFF !important; /* Warna tulisan "Browse files" menjadi Putih murni */
}

/* Efek Hover untuk tombol "Browse files" */
section[data-testid="stFileUploaderDropzone"] button:hover {
    background-color: #D97706 !important; 
    border-color: #D97706 !important;
}

/* =======================================================
    DIVIDER
======================================================= */
hr {
    border-color: #E2E8F0 !important;
    margin: 32px 0 !important;
}

/* =======================================================
    SUBMIT BUTTON
======================================================= */
div[data-testid="stFormSubmitButton"], .download-btn-container {
    display: flex;
    justify-content: center;
    margin-top: 32px;
    margin-bottom: 16px;
}

div[data-testid="stFormSubmitButton"] > button, div[data-testid="stDownloadButton"] > button {
    width: 240px !important;
    height: 48px !important;
    background: #D97706 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stFormSubmitButton"] > button:hover, div[data-testid="stDownloadButton"] > button:hover {
    background: #B45309 !important;
    color: white !important;
    box-shadow: 0 4px 12px rgba(180, 83, 9, 0.3) !important;
    transform: translateY(-1px);
}

/* =======================================================
    SIDEBAR & NAVIGATION
======================================================= */
[data-testid="stSidebar"] {
    background: #0E1B2E !important;
}

[data-testid="stSidebar"] * {
    color: #E2E8F0 !important;
}

section[data-testid="stSidebar"] .stRadio > div[role="radiogroup"] {
    gap: 8px;
}

section[data-testid="stSidebar"] .stRadio label {
    background: transparent;
    padding: 12px 16px;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.25s ease;
    border-left: 4px solid transparent;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255, 255, 255, 0.05);
    border-left: 4px solid #D97706;
}

section[data-testid="stSidebar"] .stRadio span[data-baseweb="radio"] > div:first-child {
    display: none;
}

section[data-testid="stSidebar"] .stRadio div[data-testid="stMarkdownContainer"] p {
    font-size: 1rem;
    margin: 0;
}

section[data-testid="stSidebar"] .stRadio label[data-checked="true"] {
    background: rgba(255, 255, 255, 0.1);
    border-left: 4px solid #D97706;
}
section[data-testid="stSidebar"] .stRadio label[data-checked="true"] p {
    color: #FFFFFF !important;
    font-weight: 600;
}

/* =======================================================
    CUSTOM CARDS & BADGES (FOR RESULTS)
======================================================= */
.dashboard-card {
    background: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    height: 100%;
}

/* =======================================================
   1. KPI CARDS 
======================================================= */
.kpi-card {
    text-align: center;
    height: 125px !important; /* Tinggi fixed seragam untuk semua card */
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    padding: 12px 16px !important;
}

.kpi-label {
    font-size: 0.85rem !important;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}

.kpi-value {
    font-size: 1.75rem !important; /* Disesuaikan agar angka panjang tidak pecah 2 baris */
    font-weight: 800;
    color: #0F172A;
    line-height: 1.2;
    white-space: nowrap !important; /* Mencegah teks terpotong ke bawah */
}

/* =======================================================
   2. BUNGKUS PLOTLY CHART MENJADI CARD TANPA HTML DIV SLICING
======================================================= */
div[data-testid="stPlotlyChart"] {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 12px !important;
    padding: 16px !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
}

.insight-mini-card {
    background: #F8FAFC;
    border-left: 4px solid #D97706;
    padding: 16px;
    margin-bottom: 12px;
    border-radius: 4px 8px 8px 4px;
    color: #334155;
    font-size: 0.95rem;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}

.risk-badge {
    display: inline-block;
    padding: 8px 24px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 1.1rem;
    margin-top: 16px;
}
.risk-high { background: #FEE2E2; color: #DC2626; }
.risk-medium { background: #FEF3C7; color: #D97706; }
.risk-low { background: #DCFCE7; color: #16A34A; }

/* Status Badges untuk tabel */
.badge-table {
    padding: 4px 8px;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
}

/* =======================================================
1. WARNA TEKS DI DALAM EXPANDER (Ketentuan CSV)
======================================================= */
/* Mengubah teks biasa & daftar list di dalam expander agar gelap (tidak menyatu dengan background) */
div[data-testid="stExpanderDetails"] p, 
div[data-testid="stExpanderDetails"] li, 
div[data-testid="stExpanderDetails"] span {
    color: #334155 !important; /* Warna Slate Dark (sangat jelas terbaca) */
}
div[data-testid="stExpanderDetails"] strong {
    color: #0F172A !important; /* Warna Navy Gelap */
}

/* =======================================================
    3. WARNA JUDUL EXPANDER SAAT TERBUKA (DIKLIK)
======================================================= */

/* 1. Background & Border utama saat expander terbuka */
div[data-testid="stExpander"] details[open] summary {
    background-color: #0F172A !important;
    border-color: #0F172A !important;
    border-radius: 8px !important;
    transition: background-color 0.25s ease;
}

/* 2. Warna teks & ikon di dalam judul saat terbuka */
div[data-testid="stExpander"] details[open] summary * {
    color: #FFFFFF !important;
    fill: #FFFFFF !important;
}

/* 3. Efek hover sederhana saat terbuka (hanya sedikit menerangkan warna background) */
div[data-testid="stExpander"] details[open] summary:hover {
    background-color: #1E293B !important;
    border-color: #1E293B !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 2. LOAD MODEL & ARTIFACTS
# =========================================================
import os

# Mendapatkan direktori tempat file app.py ini berada (folder streamlit/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Bergerak satu langkah keluar (..) lalu masuk ke folder models/
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "hotel_cancellation_model.joblib")

@st.cache_resource
def load_artifacts():
    return joblib.load(MODEL_PATH)

try:
    artifacts = load_artifacts()
    model = artifacts['model']
    target_encoder = artifacts['target_encoder']
    best_threshold = artifacts['best_threshold']
    global_mean_train = artifacts['global_mean_train']
    country_risk_mapping = artifacts['country_risk_mapping']
    agent_frequency_map = artifacts['agent_frequency_map']
    customer_type_map = artifacts['customer_type_map']
    meal_map = artifacts['meal_map']
    room_map = artifacts['room_map']
    feature_names = artifacts['feature_names']
except Exception as e:
    st.error(f"Model artifacts tidak ditemukan di path: {MODEL_PATH}")
    st.caption(f"Detail error: {e}")
    st.stop()
# =========================================================
# 3. HELPER FUNCTION: PREPROCESSING UNIVERSAL (SINGLE & BATCH)
# =========================================================
def preprocess_data(df_input):
    df_raw = df_input.copy()
    
    # Cleaning dasar (Mencegah error jika data mentah ada yang kosong)
    df_raw['children'] = df_raw.get('children', 0).fillna(0)
    df_raw['babies'] = df_raw.get('babies', 0).fillna(0)
    df_raw['agent'] = df_raw.get('agent', 0).fillna(0)
    df_raw['company'] = df_raw.get('company', 0).fillna(0)
    
    if 'meal' in df_raw.columns:
        df_raw['meal'] = df_raw['meal'].replace('Undefined', 'SC')
    
    # Kalkulasi Otomatis (Jika di file CSV tidak ada, sistem akan membuatnya)
    if 'arrival_date_month_num' not in df_raw.columns and 'arrival_date_month' in df_raw.columns:
        months_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
        df_raw['arrival_date_month_num'] = df_raw['arrival_date_month'].map(months_map).fillna(1)
        
    if 'arrival_day_of_week' not in df_raw.columns and 'arrival_date_year' in df_raw.columns:
        temp_date = pd.to_datetime(
            df_raw['arrival_date_year'].astype(str) + '-' +
            df_raw['arrival_date_month_num'].astype(str) + '-' +
            df_raw['arrival_date_day_of_month'].astype(str), errors='coerce'
        )
        df_raw['arrival_day_of_week'] = temp_date.dt.dayofweek.fillna(0).astype(int)

    # 1. Segment Channel Risk
    def assign_segment_channel_risk(row):
        combination = f"{row.get('market_segment', 'Undefined')}_via_{row.get('distribution_channel', 'Undefined')}"
        if combination in ['Groups_via_TA/TO']: return 4  
        elif combination in ['Offline TA/TO_via_Corporate', 'Groups_via_Direct', 'Groups_via_Corporate', 'Online TA_via_TA/TO', 'Offline TA/TO_via_TA/TO', 'Online TA_via_Corporate']: return 3  
        elif combination in ['Aviation_via_Corporate', 'Corporate_via_TA/TO', 'Online TA_via_GDS', 'Corporate_via_Corporate', 'Offline TA_via_Direct', 'Offline TA_via_GDS', 'Complementary_via_Corporate']: return 2  
        else: return 1  
            
    df_raw['segment_channel_risk'] = df_raw.apply(assign_segment_channel_risk, axis=1)
    
    # 2. Parking & Repeated Guest
    df_raw['has_parking_request'] = (df_raw.get('required_car_parking_spaces', 0) > 0).astype(int)
    total_past_bookings = df_raw.get('previous_cancellations', 0) + df_raw.get('previous_bookings_not_canceled', 0)
    df_raw['is_repeated_guest_refined'] = ((df_raw.get('is_repeated_guest', 0) == 1) | (total_past_bookings > 0)).astype(int)
    
    # 3. Guest Type & Total Guests
    df_raw['total_guests'] = df_raw.get('adults', 0) + df_raw['children'] + df_raw['babies']
    def segment_guest_type(row):
        if row['total_guests'] == 1: return 'Single'
        elif row['total_guests'] == 2 and row.get('adults', 0) == 2: return 'Couple'
        elif row['children'] > 0 or row['babies'] > 0: return 'Family'
        else: return 'Group'
    df_raw['guest_type_category'] = df_raw.apply(segment_guest_type, axis=1)
    
    # 4. ADR Per Person
    df_raw['adr_per_person'] = np.where(df_raw['total_guests'] > 0, df_raw.get('adr', 0) / df_raw['total_guests'], df_raw.get('adr', 0))
    
    # 5. Country Risk Bin
    map_country_num = {'High_Risk_Country': 3, 'Medium_Risk_Country': 2, 'Low_Risk_Country': 1}
    df_raw['country_risk_bin'] = df_raw.get('country', 'PRT').apply(lambda x: map_country_num.get(country_risk_mapping.get(x, 'Low_Risk_Country'), 1))
    
    # 6. Log Lead Time
    df_raw['lead_time'] = np.log1p(df_raw.get('lead_time', 0))
    
    # 7. Mean Risk Encodings
    df_raw['customer_type_cancel_risk'] = df_raw.get('customer_type', 'Transient').apply(lambda x: customer_type_map.get(x, global_mean_train))
    df_raw['meal_cancel_risk'] = df_raw.get('meal', 'BB').apply(lambda x: meal_map.get(x, global_mean_train))
    df_raw['reserved_room_type_cancel_risk'] = df_raw.get('reserved_room_type', 'A').apply(lambda x: room_map.get(x, global_mean_train))
    
    # 8. Agent Density
    df_raw['agent_booking_density'] = df_raw['agent'].apply(lambda x: agent_frequency_map.get(x, 0))
    
    # 9. Seasonal Cycles
    df_raw['month_sin'] = np.sin(2 * np.pi * df_raw.get('arrival_date_month_num', 1) / 12.0)
    df_raw['month_cos'] = np.cos(2 * np.pi * df_raw.get('arrival_date_month_num', 1) / 12.0)
    
    # 10. Ordinal Encodings
    mapping_hotel = {'City Hotel': 1, 'Resort Hotel': 0}
    mapping_deposit = {'No Deposit': 0, 'Refundable': 1, 'Non Refund': 2}
    
    df_raw['hotel'] = df_raw.get('hotel', 'City Hotel').map(mapping_hotel).fillna(1)
    df_raw['deposit_type'] = df_raw.get('deposit_type', 'No Deposit').map(mapping_deposit).fillna(0)
    
    # B. Target Encoding
    # Susun kolom agar sesuai dengan saat training
    df_ordered = df_raw[[col for col in feature_names if col in df_raw.columns]]
    
    # Jika ada kolom feature_names yang tidak ada di CSV, tambahkan dengan nilai 0
    for col in feature_names:
        if col not in df_ordered.columns:
            df_ordered[col] = 0
            
    df_ordered = df_ordered[feature_names] # Pastikan urutan final 100% cocok
    df_encoded = target_encoder.transform(df_ordered)
    
    return df_encoded

# =========================================================
# 4. SIDEBAR NAVIGATION
# =========================================================
st.sidebar.markdown("""
<div style='padding: 1.5rem 0 2rem 0.5rem;'>
    <h1 style='color: #D97706; font-size: 2rem; margin:0;'>🏨 HOTEL INSIGHT</h1>
    <p style='color: #94A3B8; font-size: 1rem; margin-top: 4px;'>Analytics Dashboard</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<hr style='margin-top: 0; margin-bottom: 2rem; border-color: rgba(255,255,255,0.1) !important;'>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "",
    ["🛡️ Cancellation Risk Model", "📊 Portfolio Risk Monitor"],
    label_visibility="collapsed"
)

# =========================================================
# HALAMAN 1: SINGLE BOOKING PREDICTOR
# =========================================================
if page == "🛡️ Cancellation Risk Model":
    st.title("Cancellation Risk Predictor")
    st.markdown("<p class='subtitle-text'>Analyze individual guest booking risk seamlessly.</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    
    with st.form("single_predictor_form"):
        st.subheader("👤 Guest Profile")
        col1, col2, col3 = st.columns(3)
        with col1: country = st.text_input("Country Code (ISO)", value="PRT").upper()
        with col2: customer_type = st.selectbox("Customer Type", ["Transient", "Transient-Party", "Contract", "Group"])
        with col3: is_repeated_guest = st.selectbox("Is Repeated Guest?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        
        col4, col5, col_empty = st.columns(3)
        with col4: prev_cancels = st.number_input("Previous Cancellations", min_value=0, value=0)
        with col5: prev_not_cancels = st.number_input("Previous Bookings Not Canceled", min_value=0, value=0)

        st.subheader("📅 Reservation Details")
        col6, col7, col8 = st.columns(3)
        with col6: hotel = st.selectbox("Hotel Type", ["City Hotel", "Resort Hotel"])
        with col7: arrival_date = st.date_input("Arrival Date", datetime.date(2026, 6, 15))
        with col8: lead_time = st.number_input("Lead Time (Days)", min_value=0, value=30)
        
        col9, col10, col_empty2 = st.columns(3)
        with col9: stays_week = st.number_input("Stays in Week Nights", min_value=0, value=2)
        with col10: stays_weekend = st.number_input("Stays in Weekend Nights", min_value=0, value=1)

        st.subheader("💳 Room & Transaction")
        col11, col12, col13 = st.columns(3)
        with col11: reserved_room = st.selectbox("Reserved Room Type", ["A", "B", "C", "D", "E", "F", "G", "H", "L"])
        with col12: meal = st.selectbox("Meal Plan", ["BB", "HB", "FB", "SC"])
        with col13: deposit_type = st.selectbox("Deposit Type", ["No Deposit", "Non Refund", "Refundable"])
        
        col14, col15, col16 = st.columns(3)
        with col14: adr = st.number_input("ADR (Price per Night €)", min_value=1.0, value=100.0)
        with col15: adults = st.number_input("Adults", min_value=1, value=2)
        with col16: children = st.number_input("Children (Inc. Babies)", min_value=0, value=0)
        
        col17, col18, col_empty3 = st.columns(3)
        with col17: parking = st.number_input("Required Parking Spaces", min_value=0, value=0)
        with col18: special_requests = st.number_input("Total Special Requests", min_value=0, value=0)
        
        market_segment = "Online TA"
        distribution_channel = "TA/TO"
        agent = 9
        company = 0
        
        submit_btn = st.form_submit_button("Submit Prediction", type="primary", use_container_width=False)

    if submit_btn:
        arrival_year = arrival_date.year
        arrival_month = arrival_date.month
        arrival_day = arrival_date.day
        arrival_week = arrival_date.isocalendar().week  
        arrival_day_of_week = arrival_date.weekday()    
        
        input_data = {
            'hotel': hotel, 'lead_time': lead_time, 'arrival_date_year': arrival_year,
            'arrival_date_week_number': arrival_week, 'arrival_date_day_of_month': arrival_day,
            'stays_in_weekend_nights': stays_weekend, 'stays_in_week_nights': stays_week,
            'previous_cancellations': prev_cancels, 'previous_bookings_not_canceled': prev_not_cancels,
            'deposit_type': deposit_type, 'company': float(company), 'total_of_special_requests': special_requests,
            'arrival_day_of_week': arrival_day_of_week, 'arrival_date_month_num': arrival_month,
            'required_car_parking_spaces': parking, 'is_repeated_guest': is_repeated_guest,
            'adults': adults, 'children': children, 'babies': 0, 'adr': adr, 'country': country,
            'customer_type': customer_type, 'meal': meal, 'reserved_room_type': reserved_room,
            'agent': agent, 'market_segment': market_segment, 'distribution_channel': distribution_channel
        }
        
        X_single = preprocess_data(pd.DataFrame([input_data]))
        prob_cancel = model.predict_proba(X_single)[:, 1][0]
        
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Risk Assessment Result</h2>", unsafe_allow_html=True)
        
        if prob_cancel > best_threshold:
            badge_class = "risk-high"
            badge_text = "🔴 HIGH RISK"
        elif prob_cancel >= 0.30:
            badge_class = "risk-medium"
            badge_text = "🟡 MEDIUM RISK"
        else:
            badge_class = "risk-low"
            badge_text = "🟢 LOW RISK"

        st.markdown(f"""
        <div class="dashboard-card" style="text-align: center; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 24px;">
            <p class="subtitle-text" style="font-weight: 600; margin-bottom: 8px; font-size: 1.1rem;">Cancellation Probability</p>
            <div style="font-size: 3.5rem; font-weight: 800; color: #0F172A; line-height: 1;">{prob_cancel:.1%}</div>
            <div class="risk-badge {badge_class}">{badge_text}</div>
        </div>
        """, unsafe_allow_html=True)
                
        insights_html = f"""<div class="dashboard-card"><h4 style="margin-top:0; margin-bottom:1rem; color: #0F172A;">💡 Prescriptive Operational Insights</h4>"""
        
        if prob_cancel > best_threshold:
            insights_html += f"<p style='color: #475569; margin-bottom: 16px;'>Tamu berada di <b>zona risiko tinggi</b> (Probabilitas > {best_threshold:.0%}). Lakukan intervensi berikut:</p>"
            if parking == 0:
                insights_html += "<div class='insight-mini-card'><b>🚗 Aksi A:</b> Tawarkan konfirmasi slot parkir gratis. Berdasarkan data, permintaan parkir menurunkan risiko pembatalan hingga 0%.</div>"
            if special_requests == 0:
                insights_html += "<div class='insight-mini-card'><b>✉️ Aksi B:</b> Kirim survei preferensi layanan. Mengisi permintaan khusus terbukti menurunkan probabilitas pembatalan sebesar ~13%.</div>"
            insights_html += "<div class='insight-mini-card' style='border-left-color: #DC2626; background: #FEF2F2;'><b>🏨 Strategi Overbooking:</b> Buka 1 slot <i>overbooking</i> di kelas kamar ini untuk memitigasi potensi kehilangan pendapatan.</div>"
        else:
            insights_html += "<div class='insight-mini-card' style='border-left-color: #16A34A; background: #F0FDF4;'><b>🟢 Status Aman:</b> Tamu ini memiliki kepastian kedatangan yang tinggi. Tidak diperlukan tindakan <i>overbooking</i> agresif.</div>"
            
        insights_html += "</div>"
        
        st.markdown(insights_html, unsafe_allow_html=True)

# =========================================================
# HALAMAN 2: PORTFOLIO RISK MONITOR
# =========================================================
elif page == "📊 Portfolio Risk Monitor":
    st.title("Cancellation Overview")
    st.markdown("<p class='subtitle-text'>Monitor booking cancellations, key insights, and overbooking strategy via bulk processing.</p>", unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    # --- PANDUAN INPUT DAN DOWNLOAD TEMPLATE ---
    with st.expander("📖 Lihat Panduan Format CSV & Download Template Data"):
        st.markdown("""
        **Ketentuan Format File CSV yang Diunggah:**
        1. **Format File:** File harus berformat `.csv` dengan pemisah koma.
        2. **Panduan Kolom & Tipe Data:** Silakan unduh file **Kamus_Data_Reservasi.txt** di bawah ini untuk melihat daftar lengkap tipe data (Angka/Kategori) dan nilai valid yang diizinkan untuk setiap kolom.
        3. Kolom status akhir (seperti `is_canceled`, `reservation_status`) tidak perlu diisi untuk prediksi tamu baru.
        """)
        
        # 1. Membuat sample CSV Template
        sample_data = pd.DataFrame([{
            'hotel': 'City Hotel', 'lead_time': 45, 'arrival_date_year': 2026,
            'arrival_date_month': 'June', 'arrival_date_day_of_month': 15,
            'stays_in_weekend_nights': 1, 'stays_in_week_nights': 2,
            'adults': 2, 'children': 0, 'babies': 0, 'meal': 'BB',
            'country': 'PRT', 'market_segment': 'Online TA', 'distribution_channel': 'TA/TO',
            'is_repeated_guest': 0, 'previous_cancellations': 0,
            'previous_bookings_not_canceled': 0, 'reserved_room_type': 'A',
            'deposit_type': 'No Deposit', 'agent': 9, 'company': 0,
            'customer_type': 'Transient', 'adr': 110.0,
            'required_car_parking_spaces': 0, 'total_of_special_requests': 1
        }])
        sample_csv = sample_data.to_csv(index=False).encode('utf-8')
        
        # 2. Membuat Data Dictionary TXT (sesuai input & mengabaikan Undefined)
        dictionary_text = """DICTIONARY TEXT"""
        
        # 3. Layout Download Buttons menggunakan Columns
        st.markdown("<br>", unsafe_allow_html=True)
        col_dl1, col_dl2 = st.columns(2)
        
        with col_dl1:
            st.download_button(
                label="📥 Download Template CSV",
                data=sample_csv,
                file_name="template_reservasi.csv",
                mime="text/csv",
                use_container_width=True
            )
            
        with col_dl2:
            st.download_button(
                label="📓 Download Kamus Data (TXT)",
                data=dictionary_text.encode('utf-8'),
                file_name="Kamus_Data_Reservasi.txt",
                mime="text/plain",
                use_container_width=True
            )
    # File Uploader
    uploaded_file = st.file_uploader("Upload Reservation Data (Format .CSV)", type=["csv"])
    
    if uploaded_file is not None:
        with st.spinner("Analyzing reservation data..."):
            # 1. Load Data
            df_batch = pd.read_csv(uploaded_file)
            
            # 2. Prediksi via fungsi Preprocessing Universal
            try:
                X_batch = preprocess_data(df_batch)
                probs = model.predict_proba(X_batch)[:, 1]
            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses data: {str(e)}")
                st.stop()
            
            # 3. Labeling Risiko
            df_batch['Cancellation_Probability'] = probs
            def categorize_risk(p):
                if p > best_threshold: return 'High Risk'
                elif p >= 0.30: return 'Medium Risk'
                else: return 'Low Risk'
            
            df_batch['Risk_Level'] = df_batch['Cancellation_Probability'].apply(categorize_risk)
            
            # 4. Kalkulasi KPI
            total_bookings = len(df_batch)
            high_risk_df = df_batch[df_batch['Risk_Level'] == 'High Risk']
            est_cancellations = len(high_risk_df)
            cancel_rate = est_cancellations / total_bookings if total_bookings > 0 else 0
            
            # Hitung Revenue (Jika ada data lama menginap, kalikan dengan ADR. Jika tidak, pakai ADR saja)
            if 'stays_in_weekend_nights' in df_batch.columns and 'stays_in_week_nights' in df_batch.columns:
                revenue_at_risk = (high_risk_df['adr'] * (high_risk_df['stays_in_weekend_nights'] + high_risk_df['stays_in_week_nights'])).sum()
            else:
                revenue_at_risk = high_risk_df['adr'].sum()
                
            st.markdown("<hr>", unsafe_allow_html=True)
            
            # --- RENDER KPI CARDS ---
            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.markdown(f"""
                <div class="dashboard-card kpi-card" style="border-top: 4px solid #000080;">
                    <div class="kpi-label">Total Bookings</div>
                    <div class="kpi-value">{total_bookings:,}</div>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                st.markdown(f"""
                <div class="dashboard-card kpi-card" style="border-top: 4px solid #D97706;">
                    <div class="kpi-label">Est. Cancellations</div>
                    <div class="kpi-value" style="color: #D97706;">{est_cancellations:,}</div>
                </div>
                """, unsafe_allow_html=True)

            with c3:
                st.markdown(f"""
                <div class="dashboard-card kpi-card" style="border-top: 4px solid #00FFEF;">
                    <div class="kpi-label">Cancellation Rate</div>
                    <div class="kpi-value">{cancel_rate:.1%}</div>
                </div>
                """, unsafe_allow_html=True)

            with c4:
                st.markdown(f"""
                <div class="dashboard-card kpi-card" style="border-top: 4px solid #DC2626;">
                    <div class="kpi-label">Revenue at Risk</div>
                    <div class="kpi-value" style="color: #DC2626;">${revenue_at_risk:,.0f}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            # --- RENDER CHARTS ---
            # --- RENDER CHARTS ---
            col_chart1, col_chart2 = st.columns([1, 1.2])

            # ---------------------------------------------------------
            # CHART 1: DONUT CHART (CANCELLATIONS BY RISK LEVEL)
            # ---------------------------------------------------------
            with col_chart1:
                risk_counts = df_batch['Risk_Level'].value_counts().reset_index()
                risk_counts.columns = ['Risk', 'Count']
                color_map = {'High Risk': '#DC2626', 'Medium Risk': '#F59E0B', 'Low Risk': '#10B981'}
                
                fig_pie = px.pie(
                    risk_counts, 
                    values='Count', 
                    names='Risk', 
                    hole=0.55, 
                    color='Risk', 
                    color_discrete_map=color_map,
                    title="<b>Cancellations by Risk Level</b>"
                )
                
                # Tampilkan Nama Kelas (Label) & Persentase langsung di dalam chart
                fig_pie.update_traces(
                    textinfo='label+percent', 
                    textposition='inside',
                    insidetextorientation='horizontal',
                    textfont=dict(size=12, color='#FFFFFF', family='Arial')
                )
                
                fig_pie.update_layout(
                    title=dict(font=dict(size=16, color='#0F172A'), y=0.95, x=0.02),
                    margin=dict(t=30, b=30, l=30, r=60),  # Memberikan jarak (padding) dari tepi card
                    showlegend=True,
                    legend=dict(
                        font=dict(color='#0F172A', size=11),
                        orientation="h",
                        yanchor="bottom",
                        y=-0.15,
                        xanchor="center",
                        x=0.5
                    ),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                
                st.plotly_chart(fig_pie, use_container_width=True)

            # ---------------------------------------------------------
            # CHART 2: BAR CHART (HIGH RISK BY MARKET SEGMENT)
            # ---------------------------------------------------------
            with col_chart2:
                if 'market_segment' in df_batch.columns:
                    segment_counts = high_risk_df['market_segment'].value_counts().reset_index()
                    segment_counts.columns = ['Segment', 'High Risk Count']
                    
                    # Palet warna menarik terpisah per kelas segmen
                    segment_colors = ['#0F172A', '#2563EB', '#D97706', '#059669', '#7C3AED', '#DB2777', '#475569']
                    
                    fig_bar = px.bar(
                        segment_counts, 
                        x='Segment', 
                        y='High Risk Count', 
                        color='Segment', # Memisahkan warna berdasarkan kelas
                        color_discrete_sequence=segment_colors,
                        title="<b>High Risk by Market Segment</b>"
                    )
                    
                    # Tampilkan angka nilai di atas setiap batang (Bar)
                    fig_bar.update_traces(
                        texttemplate='%{y:,}', 
                        textposition='outside',
                        textfont=dict(color='#0F172A', size=11, family='Arial')
                    )
                    
                    fig_bar.update_layout(
                        title=dict(font=dict(size=16, color='#0F172A'), y=0.95, x=0.02),
                        margin=dict(t=60, b=20, l=20, r=20),
                        showlegend=False, # Legend di-hide karena sumbu X sudah jelas
                        xaxis=dict(
                            title="", 
                            tickfont=dict(color='#0F172A', size=11),
                            showgrid=False
                        ),
                        yaxis=dict(
                            title="Bookings", 
                            tickfont=dict(color='#0F172A', size=11), 
                            showgrid=True, 
                            gridcolor='#E2E8F0' # Warna garis grid yang lembut
                        ),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)'
                    )
                    
                    st.plotly_chart(fig_bar, use_container_width=True)
                else:
                    st.info("Market segment data not available in the uploaded file.")
            
            # --- RENDER TABLE & DOWNLOAD ---
            st.markdown("### 📋 Booking Details & Export")

            # Pilih kolom yang relevan untuk ditampilkan agar tidak terlalu padat
            display_cols = [col for col in ['hotel', 'lead_time', 'country', 'market_segment', 'adr'] if col in df_batch.columns]
            display_cols += ['Cancellation_Probability', 'Risk_Level']

            # Batasi hanya 100 baris pertama untuk ditampilkan agar Pandas Styler tidak berat/error
            df_display = df_batch[display_cols].head(10)

            # Styling tabel Streamlit
            st.dataframe(
                df_display.style.map(  # Catatan: di Pandas versi baru, .map() menggantikan .applymap()
                    lambda val: 'color: #DC2626; font-weight: bold;' if val == 'High Risk' 
                    else ('color: #D97706; font-weight: bold;' if val == 'Medium Risk' 
                    else 'color: #16A34A; font-weight: bold;'), 
                    subset=['Risk_Level']
                ), 
                use_container_width=True
            )
            
            # Download Button (Dibungkus dengan div agar center mengikuti CSS submit button)
            csv_data = df_batch.to_csv(index=False).encode('utf-8')
            
            st.markdown("<div class='download-btn-container'>", unsafe_allow_html=True)
            st.download_button(
                label="📥 Export Processed Report (CSV)",
                data=csv_data,
                file_name="portfolio_risk_assessment.csv",
                mime="text/csv"
            )
            st.markdown("</div>", unsafe_allow_html=True)