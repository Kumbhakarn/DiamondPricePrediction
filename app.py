import streamlit as st
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline  # Assuming this is your pipeline for prediction

# Set the page configuration
st.set_page_config(page_title="Diamond Price Prediction", page_icon="💎", layout="centered")

# Header
st.title("💎 Diamond Price Prediction 💎")

# Introduction text
st.markdown("""
    Welcome to the **Diamond Price Prediction** app! Here, you can enter the details of a diamond, 
    and we will predict its price based on features like **Carat**, **Cut**, **Color**, **Clarity**, 
    and other attributes.
    
    Just fill out the form below and click the **Predict** button to get the estimated price.
""")

# Styling the form
st.markdown("""
    <style>
    .form-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stInput input {
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Form for the user to enter details
with st.form(key='diamond_form', clear_on_submit=True):
    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    # Input fields with sample values (range examples)
    carat = st.number_input(
        'Carat (weight)',
        min_value=0.0, 
        step=0.01, 
        format="%.2f",
        help="Typical range: 0.2 to 5.0 carats"
    )

    depth = st.number_input(
        'Depth (percentage)',
        min_value=0.0, 
        step=0.01, 
        format="%.2f",
        help="Typical range: 58% to 75%"
    )

    table = st.number_input(
        'Table (percentage)',
        min_value=0.0, 
        step=0.01, 
        format="%.2f",
        help="Typical range: 50% to 70%"
    )

    x = st.number_input(
        'X Dimension (Length in mm)',
        min_value=0.0, 
        step=0.01, 
        format="%.2f",
        help="Typical range: 4.0 mm to 10.0 mm"
    )

    y = st.number_input(
        'Y Dimension (Width in mm)',
        min_value=0.0, 
        step=0.01, 
        format="%.2f",
        help="Typical range: 4.0 mm to 10.0 mm"
    )

    z = st.number_input(
        'Z Dimension (Height in mm)',
        min_value=0.0, 
        step=0.01, 
        format="%.2f",
        help="Typical range: 2.0 mm to 6.0 mm"
    )
    
    cut = st.selectbox(
        'Cut',
        ['Fair', 'Good', 'Very Good', 'Ideal', 'Excellent'],
        help="Quality of the cut. 'Excellent' gives the best shine and brilliance."
    )

    color = st.selectbox(
        'Color',
        ['D', 'E', 'F', 'G', 'H', 'I', 'J'],
        help="Color scale from D (colorless) to J (light yellow or brown)."
    )

    clarity = st.selectbox(
        'Clarity',
        ['SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2', 'IF', 'FL'],
        help="Clarity grades from 'FL' (Flawless) to 'SI1' (Slightly Included)."
    )

    submit_button = st.form_submit_button(label='Predict')

    st.markdown('</div>', unsafe_allow_html=True)

# When the user submits the form
if submit_button:
    # Show a loading spinner while making predictions
    with st.spinner('Predicting diamond price...'):
        # Create the data object using user inputs
        data = CustomData(
            carat=carat,
            depth=depth,
            table=table,
            x=x,
            y=y,
            z=z,
            cut=cut,
            color=color,
            clarity=clarity
        )
        
        # Get the data in DataFrame format for prediction
        final_new_data = data.get_data_as_dataframe()

        # Initialize prediction pipeline and get the prediction
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(final_new_data)

        # Round off the predicted price
        predicted_price = round(prediction[0], 2)

    # Display the result
    st.success(f"💰 The predicted price of the diamond is: **${predicted_price}**")
    
    # Additional details (optional, for a more polished result)
    st.markdown("""
    ---
    ### Want to know more?
    The prediction is based on a machine learning model that takes into account various attributes of a diamond such as carat, cut, color, clarity, and size. Each attribute affects the price of a diamond differently.
    
    Have fun experimenting with different inputs and see how the predicted price changes!
    """)

# Add a footer with contact info or additional details (optional)
st.markdown("""
    ---
    **Contact us:** [info@diamondpricepredictor](mailto:info@diamondpricepredictor)
    """)