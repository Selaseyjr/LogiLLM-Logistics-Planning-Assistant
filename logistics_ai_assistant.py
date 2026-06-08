import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="LogiLLM Control Tower",
    page_icon="🚚",
    layout="wide"
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container{
    padding-top: 2rem;
}

[data-testid="metric-container"] {
    border: 1px solid #e6e6e6;
    padding: 15px;
    border-radius: 10px;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚚 LogiLLM Control Tower")

st.caption(
    "AI-Powered Logistics Planning and Shipment Decision Support Platform"
)

st.markdown("""
### Supply Chain Decision Intelligence

Optimize transportation planning using AI-driven recommendations
for mode selection, cost efficiency, risk assessment,
and sustainability evaluation.
""")

# --------------------------------------------------
# KPI DASHBOARD
# --------------------------------------------------

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric("Shipments Analyzed", "1,247")

with kpi2:
    st.metric("Planning Efficiency", "+18%")

with kpi3:
    st.metric("Average Lead Time", "2.4 Days")

with kpi4:
    st.metric("Risk Alerts", "23")

st.divider()

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙️ Planning Settings")

temperature = st.sidebar.slider(
    "AI Creativity",
    min_value=0.0,
    max_value=1.5,
    value=0.3,
    step=0.1
)

st.sidebar.markdown("---")

st.sidebar.subheader("About")

st.sidebar.info(
    """
    LogiLLM Control Tower provides:

    • Transport mode recommendations

    • Cost-speed tradeoff analysis

    • Shipment risk assessment

    • Sustainability insights

    • Executive logistics summaries
    """
)

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "Shipment Planning",
        "Risk Analysis",
        "Sustainability"
    ]
)

# --------------------------------------------------
# TAB 1
# --------------------------------------------------

with tab1:

    st.subheader("Shipment Information")

    col1, col2 = st.columns(2)

    with col1:

        origin = st.text_input(
            "Origin Location",
            placeholder="Frankfurt"
        )

        destination = st.text_input(
            "Destination Location",
            placeholder="Hamburg"
        )

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

        cargo_value = st.number_input(
            "Cargo Value (€)",
            min_value=1000,
            value=50000,
            step=1000
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

        delivery_window = st.selectbox(
            "Required Delivery Window",
            [
                "24 Hours",
                "48 Hours",
                "3-5 Days",
                "Flexible"
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

    st.divider()

    if st.button("Generate Logistics Plan"):

        prompt = f"""
You are a senior logistics and supply chain consultant.

Analyze this shipment:

Origin: {origin}
Destination: {destination}
Cargo Type: {cargo_type}
Cargo Value: €{cargo_value}
Weight: {weight} kg
Urgency: {urgency}
Delivery Window: {delivery_window}
Business Priority: {budget}

Provide:

# Recommended Transport Mode

# Justification

# Cost Considerations

# Speed Considerations

# Operational Risks

# Sustainability Considerations

# Executive Summary

Use professional business language.
"""

        with st.spinner("Generating logistics recommendation..."):

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=temperature,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert logistics consultant with 20 years of supply chain experience."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            result = response.choices[0].message.content

        st.success("Recommendation Generated Successfully")

        st.subheader("Shipment Profile")

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric("Weight", f"{weight} kg")

        with m2:
            st.metric("Cargo Value", f"€{cargo_value:,.0f}")

        with m3:
            st.metric("Urgency", urgency)

        st.divider()

        st.subheader("AI Recommendation")

        st.markdown(result)

# --------------------------------------------------
# TAB 2
# --------------------------------------------------

with tab2:

    st.subheader("Operational Risk Indicator")

    if urgency == "High":
        risk_score = 80
    elif urgency == "Medium":
        risk_score = 55
    else:
        risk_score = 25

    st.progress(risk_score)

    st.markdown(
        f"### Estimated Operational Risk Score: {risk_score}/100"
    )

    st.info(
        """
        This score is based on urgency level and shipment
        complexity. Higher values indicate increased planning
        and execution risk.
        """
    )

# --------------------------------------------------
# TAB 3
# --------------------------------------------------

with tab3:

    st.subheader("Sustainability Guidance")

    st.success(
        """
        Rail and sea freight generally produce lower carbon
        emissions than air freight.

        Consider balancing delivery speed with environmental
        impact where possible.
        """
    )

    st.metric(
        "Estimated Sustainability Rating",
        "B+"
    )
```

