import streamlit as st

# Global Styling
st.set_page_config(page_title="Startup Growth Metrics Calculator", layout="wide")
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .card {
        background-color: #1E1E1E;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }
    .metric-title {
        font-size: 1.3em;
        font-weight: bold;
        color: #FFFFFF;
        margin-bottom: 10px;
    }
    .metric-description {
        font-size: 0.9em;
        color: #A0A0A0;
        margin-bottom: 1em;
    }
    .stButton>button {
        border: none;
        color: white;
        background-color: #4CAF50;
        padding: 10px 20px;
        font-size: 1em;
        cursor: pointer;
        border-radius: 5px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<h1 class='main-title'>📊 Startup Growth Metrics Calculator</h1>", unsafe_allow_html=True)
st.write("Optimize your startup’s financial performance by calculating and analyzing key metrics. Each metric will guide you through understanding and improving business profitability.")

# 1. Customer Acquisition Cost (CAC) Card
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='metric-title'>Customer Acquisition Cost (CAC)</p>", unsafe_allow_html=True)
    st.markdown("<p class='metric-description'>Calculate the cost of acquiring a new customer.</p>", unsafe_allow_html=True)
    marketing_expenses = st.number_input("Total Marketing Expenses", min_value=0.0, step=0.01)
    sales_expenses = st.number_input("Total Sales Expenses", min_value=0.0, step=0.01)
    customers_acquired = st.number_input("Number of Customers Acquired", min_value=1)
    if st.button("Calculate CAC"):
        cac = (marketing_expenses + sales_expenses) / customers_acquired
        st.metric("CAC", f"${cac:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

# 2. Lifetime Value (LTV) Card
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='metric-title'>Lifetime Value (LTV)</p>", unsafe_allow_html=True)
    st.markdown("<p class='metric-description'>Estimate the total revenue per customer over their relationship with the business.</p>", unsafe_allow_html=True)
    purchase_value = st.number_input("Average Purchase Value", min_value=0.0, step=0.01)
    purchase_frequency = st.number_input("Average Purchase Frequency", min_value=0.0, step=0.01)
    customer_lifetime = st.number_input("Customer Lifetime", min_value=0.0, step=0.01)
    if st.button("Calculate LTV"):
        ltv = purchase_value * purchase_frequency * customer_lifetime
        st.metric("LTV", f"${ltv:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

# 3. LTV to CAC Ratio Card
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='metric-title'>LTV to CAC Ratio</p>", unsafe_allow_html=True)
    st.markdown("<p class='metric-description'>Assess the profitability of each customer with this ratio.</p>", unsafe_allow_html=True)
    if 'ltv' in locals() and 'cac' in locals() and cac > 0:
        ltv_to_cac_ratio = ltv / cac
        st.metric("LTV to CAC Ratio", f"{ltv_to_cac_ratio:.2f}")
    else:
        st.write("Please calculate valid LTV and CAC values first.")
    st.markdown("</div>", unsafe_allow_html=True)

# 4. Average Revenue Per User (ARPU) Card
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='metric-title'>Average Revenue Per User (ARPU)</p>", unsafe_allow_html=True)
    st.markdown("<p class='metric-description'>Calculate the average revenue generated per user.</p>", unsafe_allow_html=True)
    total_revenue = st.number_input("Total Revenue", min_value=0.0, step=0.01)
    total_customers = st.number_input("Total Number of Customers", min_value=1)
    if st.button("Calculate ARPU"):
        arpu = total_revenue / total_customers
        st.metric("ARPU", f"${arpu:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Break-Even Point (BEP) Card
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<p class='metric-title'>Break-Even Point (BEP)</p>", unsafe_allow_html=True)
    st.markdown("<p class='metric-description'>Identify the number of units needed to cover both fixed and variable costs, achieving profitability.</p>", unsafe_allow_html=True)
    fixed_costs = st.number_input("Fixed Costs", min_value=0.0, step=0.01)
    unit_price = st.number_input("Unit Price", min_value=0.0, step=0.01)
    variable_cost_per_unit = st.number_input("Variable Cost per Unit", min_value=0.0, step=0.01)
    if st.button("Calculate BEP"):
        if unit_price > variable_cost_per_unit:
            bep = fixed_costs / (unit_price - variable_cost_per_unit)
            st.metric("BEP", f"{bep:.2f} units")
        else:
            st.write("Unit Price must be greater than Variable Cost per Unit.")
    st.markdown("</div>", unsafe_allow_html=True)

# Summary & Insights Section
st.markdown("---")
st.subheader("📈 Summary & Insights")
if 'cac' in locals() and 'ltv' in locals():
    st.write(f"**LTV to CAC Ratio:** A value of {ltv_to_cac_ratio:.2f} indicates that for every dollar spent on acquisition, you generate {ltv_to_cac_ratio:.2f} in revenue. A healthy ratio is 3:1 or higher.")
if 'bep' in locals():
    st.write(f"**Break-Even Point:** To cover costs, aim to sell at least {bep:.2f} units. Understanding BEP helps manage cash flow.")

# Sidebar for Quick Tips
st.sidebar.title("💡 Quick Tips")
st.sidebar.info("""
- **CAC**: Lowering CAC helps improve profitability.
- **LTV**: Increasing customer lifetime or frequency raises LTV.
- **BEP**: Know the minimum sales required to break even.
""")

# Footer
st.markdown("---")
st.write("Developed to assist startups in tracking and optimizing financial performance effectively.")
