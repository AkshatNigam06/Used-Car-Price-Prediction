
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from pathlib import Path

# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚘",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_model():
    model = joblib.load("car_price_model.pkl")
    columns = joblib.load("model_columns.pkl")
    return model, columns

model, model_columns = load_model()

# =========================
# CUSTOM PREMIUM UI
# =========================
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(ellipse at top right, #102d52 0%, transparent 45%),
        linear-gradient(135deg, #050b16, #0a172b 60%, #071426);
    color: #edf6ff;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 0.8rem !important;
    padding-bottom: 2rem;
    max-width: 1450px;
}

h1, h2, h3, p, label {
    color: #edf6ff;
}

.hero {
    background: linear-gradient(125deg, #0d2340, #071426 75%, #092c4a);
    border: 1px solid #1c4770;
    border-radius: 22px;
    padding: 28px;
    min-height: 290px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 15px 45px rgba(0, 0, 0, .22);
}

.eyebrow {
    color: #22d3ee;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero-title {
    font-size: clamp(30px, 3.4vw, 48px);
    line-height: 1.12;
    font-weight: 850;
    margin: 14px 0;
}

.hero-title span {
    color: #22d3ee;
}

.hero-copy {
    color: #b8cbe1;
    font-size: 15px;
    line-height: 1.8;
}

.pill {
    display: inline-block;
    border: 1px solid #245477;
    background: #102c49;
    border-radius: 30px;
    padding: 8px 12px;
    margin: 6px 5px 0 0;
    font-size: 11px;
    color: #bfefff;
}

.section-title {
    font-size: 23px;
    font-weight: 800;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #a9bfd7;
    font-size: 13px;
    margin-bottom: 18px;
}

div[data-testid="stForm"] {
    background: rgba(8, 24, 44, .82);
    border: 1px solid #1c3b5b;
    border-radius: 17px;
    padding: 20px;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background-color: #102541;
    border-color: #294866;
    border-radius: 9px;
}

input {
    color: white !important;
}

div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #06b6d4, #1685ff);
    color: #031222;
    border: none;
    border-radius: 10px;
    font-weight: 800;
    min-height: 48px;
    width: 100%;
    transition: .2s ease;
}

div[data-testid="stFormSubmitButton"] button:hover {
    color: white;
    border: 1px solid #67e8f9;
}

div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #0d3547, #0b263c);
    border: 1px solid #12677a;
    border-radius: 15px;
    padding: 20px;
}

div[data-testid="stMetricLabel"] {
    color: #b5d7e9;
}

div[data-testid="stMetricValue"] {
    color: #4ce7c2;
    font-weight: 800;
}

div[data-testid="stImage"] img {
    border-radius: 18px;
    border: 1px solid #1c4770;
    box-shadow: 0 12px 35px rgba(0, 150, 255, .18);
}

.note {
    background: #102744;
    border: 1px solid #245078;
    border-radius: 10px;
    padding: 13px;
    color: #c8dced;
    font-size: 13px;
    margin-top: 10px;
}

.result-card {
    background: linear-gradient(145deg, #0c2b43, #0a1a30);
    border: 1px solid #214768;
    border-radius: 16px;
    padding: 26px 18px;
    text-align: center;
}

.footer {
    color: #8ca9c5;
    text-align: center;
    font-size: 12px;
    padding-top: 20px;
    border-top: 1px solid #1b344d;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HERO / HEADER
# =========================
hero_left, hero_right = st.columns(
    [1.05, 1],
    gap="large",
    vertical_alignment="center"
)


with hero_left:
    st.html("""
    <div class="hero">
        <div class="eyebrow">SMARTER DECISIONS · BETTER DEALS</div>
        <h1 class="hero-title">
            Used Car Price<br>
            <span>Predictor.</span>
        </h1>
        <p class="hero-copy">
            Discover an estimated resale value using Machine Learning.
            Enter your car details and get a prediction in seconds.
        </p>
        <div style="margin-top:18px;">
            <span class="pill">✦ Random Forest ML</span>
            <span class="pill">⚡ Quick Estimate</span>
            <span class="pill">₹ Price in INR</span>
        </div>
    </div>
    """)


with hero_right:
    image_path = Path("car_hero_image.jpg")

    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.warning(
            "Car image not found. Place car_hero_image.jpg "
            "in the same folder as app.py."
        )

    st.markdown("""
    <div style="
        text-align: center;
        color: #22d3ee;
        font-size: 12px;
        letter-spacing: 3px;
        margin-top: 8px;">
        YOUR CAR · YOUR VALUE
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# FORM AND PREDICTION PANEL
# =========================
form_col, result_col = st.columns(
    [1.3, 1],
    gap="large"
)

with form_col:
    st.markdown(
        '<div class="section-title">⚙️ Enter Car Details</div>'
        '<div class="section-subtitle">'
        'Enter the vehicle specifications to estimate its resale price.'
        '</div>',
        unsafe_allow_html=True
    )

    with st.form("car_prediction_form"):
        left, right = st.columns(2)

        with left:
            year = st.number_input(
                "Manufacturing Year",
                min_value=1990,
                max_value=datetime.now().year,
                value=2018,
                step=1
            )

            km_driven = st.number_input(
                "Kilometers Driven",
                min_value=0,
                max_value=1_000_000,
                value=50000,
                step=1000
            )

            fuel = st.selectbox(
                "Fuel Type",
                ["Diesel", "Petrol", "CNG", "LPG", "Electric"]
            )

            seller_type = st.selectbox(
                "Seller Type",
                ["Individual", "Dealer", "Trustmark Dealer"]
            )

            transmission = st.selectbox(
                "Transmission",
                ["Manual", "Automatic"]
            )

        with right:
            owner = st.selectbox(
                "Previous Owner",
                [
                    "First Owner",
                    "Second Owner",
                    "Third Owner",
                    "Fourth & Above Owner",
                    "Test Drive Car"
                ]
            )

            mileage = st.number_input(
                "Mileage (km/l or km/kg)",
                min_value=1.0,
                max_value=100.0,
                value=20.0,
                step=0.5
            )

            engine = st.number_input(
                "Engine Capacity (CC)",
                min_value=100.0,
                max_value=10000.0,
                value=1200.0,
                step=50.0
            )

            max_power = st.number_input(
                "Maximum Power (bhp)",
                min_value=1.0,
                max_value=2000.0,
                value=80.0,
                step=1.0
            )

            seats = st.selectbox(
                "Number of Seats",
                [2, 4, 5, 6, 7, 8, 9, 10, 14],
                index=2
            )

        submitted = st.form_submit_button(
            "🚀  Predict Car Price"
        )

with result_col:
    st.markdown(
        '<div class="section-title">📈 Price Estimate</div>'
        '<div class="section-subtitle">'
        'Your estimated selling price will appear here.'
        '</div>',
        unsafe_allow_html=True
    )

    if submitted:
        input_data = {
            "year": year,
            "km_driven": km_driven,
            "mileage": mileage,
            "engine": engine,
            "max_power": max_power,
            "seats": seats
        }

        input_df = pd.DataFrame([input_data])

        # Create every feature used during model training
        for column in model_columns:
            if column not in input_df.columns:
                input_df[column] = 0

        # Encode selected categorical values
        categories = {
            "fuel": fuel,
            "seller_type": seller_type,
            "transmission": transmission,
            "owner": owner
        }

        for category, value in categories.items():
            dummy_column = f"{category}_{value}"

            if dummy_column in input_df.columns:
                input_df[dummy_column] = 1

        # Match the exact training feature order
        input_df = input_df.reindex(
            columns=model_columns,
            fill_value=0
        )

        try:
            prediction = float(model.predict(input_df)[0])

            if prediction < 0:
                st.warning(
                    "The model returned a negative estimate. "
                    "Please try different car details."
                )
            else:
                st.metric(
                    label="Estimated Selling Price",
                    value=f"₹ {prediction:,.0f}"
                )

                st.markdown("""
                <div class="note">
                    ⓘ This is a machine-learning estimate,
                    not a guaranteed market price.
                </div>
                """, unsafe_allow_html=True)

                st.markdown("### 🚘 Car Summary")

                summary_left, summary_right = st.columns(2)

                with summary_left:
                    st.write(f"**Year:** {year}")
                    st.write(f"**Fuel:** {fuel}")
                    st.write(f"**Transmission:** {transmission}")
                    st.write(f"**Owner:** {owner}")

                with summary_right:
                    st.write(f"**Engine:** {engine:,.0f} CC")
                    st.write(f"**Mileage:** {mileage:.1f}")
                    st.write(f"**Max Power:** {max_power:.0f} bhp")
                    st.write(f"**Seats:** {seats}")

        except Exception as error:
            st.error(f"Prediction failed: {error}")

    else:
        st.markdown("""
        <div class="result-card">
            <div style="font-size: 48px;">🚘</div>
            <div style="
                font-size: 19px;
                font-weight: 800;
                color: #d9f4ff;
                margin-top: 12px;">
                Ready to estimate?
            </div>
            <div style="
                color: #a9bfd7;
                font-size: 13px;
                margin-top: 8px;
                line-height: 1.7;">
                Enter the car details and click
                <b>Predict Car Price</b> to get your estimate.
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown("""
<div class="footer">
    USED CAR PRICE PREDICTION
    &nbsp; • &nbsp;
    RANDOM FOREST REGRESSOR
    &nbsp; • &nbsp;
    BUILT WITH STREAMLIT
</div>
""", unsafe_allow_html=True)
