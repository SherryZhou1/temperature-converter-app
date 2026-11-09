
# ==========================================
# TEMPERATURE CONVERTER WEB APP
# Built using Python and Streamlit
# ==========================================

# SECTION 1: Import Streamlit
import streamlit as st

# SECTION 2: Configure the web page
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)

# SECTION 3: Add custom CSS for a clean interface
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fb;
    }

    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# SECTION 4: Display the app title and description
st.title("🌡️ Temperature Converter")

st.write(
    "Welcome! Use this app to convert temperatures "
    "between Celsius and Fahrenheit."
)

st.divider()

# SECTION 5: Get temperature input from the user
temperature = st.number_input(
    "Enter Temperature:",
    value=25.0,
    step=1.0,
    format="%.2f"
)

# SECTION 6: Let the user select conversion type
conversion_type = st.selectbox(
    "Select Conversion Type:",
    [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius"
    ]
)

# SECTION 7: Create the Convert button
if st.button("Convert Temperature"):

    # Convert Celsius to Fahrenheit
    if conversion_type == "Celsius to Fahrenheit":

        converted_temperature = (temperature * 9/5) + 32

        formula = "°F = (°C × 9/5) + 32"

        unit = "°F"

    # Convert Fahrenheit to Celsius
    else:

        converted_temperature = (temperature - 32) * 5/9

        formula = "°C = (°F - 32) × 5/9"

        unit = "°C"

    # SECTION 8: Display the conversion result
    st.success("Conversion Successful!")

    st.subheader("Converted Temperature")

    st.metric(
        label="Result",
        value=f"{converted_temperature:.2f} {unit}"
    )

    # SECTION 9: Display the formula used
    st.subheader("Formula Used")

    st.code(formula, language="text")

    # SECTION 10: Display a helpful message
    st.info(
        "Thank you for using the Temperature Converter!"
    )

# SECTION 11: Footer
st.divider()

st.caption("Built with Python and Streamlit ❤️")
