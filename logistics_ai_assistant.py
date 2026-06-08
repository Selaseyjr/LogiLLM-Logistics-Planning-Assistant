import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# Load API Key
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.set_page_config(
    page_title="AI Logistics Planning Assistant",
    page_icon="🚚",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚚 AI Logistics Planning Assistant")
st.markdown(
    """
    Optimize shipment planning using AI-powered logistics recommendations.
    """
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("⚙️ Settings")

temperature = st.sidebar.slider(
    "Creativity Level",
    min_value=0.0,
    max_value=1.5,
    value=0.3,
    step=0.1
)
st.sidebar.title("About")

st.sidebar.info(
    """
    AI-powered logistics planning assistant.

    Features:
    - Transport mode recommendations
    - Cost analysis
    - Risk assessment
    - Sustainability insights
    """
)

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    origin = st.text_input("Origin")

    destination = st.text_input("Destination")

    cargo_type = st.selectbox(
        "Cargo Type",
        [
            "Electronics",
            "Medical Supplies",
            "Food Products",
            "Industrial Equipment",
            "Consumer Goods"
        ]
    )

with col2:

    weight = st.number_input(
        "Shipment Weight (kg)",
        min_value=1,
        value=100
    )

    urgency = st.selectbox(
        "Delivery Urgency",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    budget = st.selectbox(
        "Business Priority",
        [
            "Lowest Cost",
            "Balanced",
            "Fastest Delivery"
        ]
    )

# --------------------------------------------------
# BUTTON
# --------------------------------------------------

if st.button("Generate Logistics Plan"):

    prompt = f"""
You are an expert logistics and supply chain consultant.

Analyze the following shipment:

Origin: {origin}
Destination: {destination}
Cargo Type: {cargo_type}
Weight: {weight} kg
Urgency: {urgency}
Business Priority: {budget}

Provide:

1. Recommended Transport Mode
2. Justification
3. Cost Considerations
4. Speed Considerations
5. Risk Assessment
6. Sustainability Considerations
7. Executive Summary

Keep the response professional and practical.
"""

    with st.spinner("Generating recommendation..."):

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior logistics consultant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

    st.success("Recommendation Generated")

    st.markdown(result)
    
