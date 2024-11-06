import streamlit as st

# Title and Description
st.title("📊 Startup Growth Metrics Calculator")
st.write("A tool to help startups calculate essential growth metrics efficiently and effectively.")

# Row layout with columns for each metric
col1, col2, col3, col4, col5 = st.columns(5)

# 1. Customer Acquisition Cost (CAC)
with col1:
    st.subheader("Customer Acquisition Cost (CAC)")
    st.write("Calculate the cost of acquiring a new customer.")
    marketing_expenses = st.number_input("Total Marketing Expenses", min_value=0.0, step=0.01)
    sales_expenses = st.number_input("Total Sales Expenses", min_value=0.0, step=0.01)
    customers_acquired = st.number_input("Number of Customers Acquired", min_value=1)
    if st.button("Calculate CAC", key="cac"):
        cac = (marketing_expenses + sales_expenses) / customers_acquired
        st.metric("CAC", f"${cac:.2f}")

# 2. Lifetime Value (LTV)
with col2:
    st.subheader("Lifetime Value (LTV)")
    st.write("Estimate the total revenue per customer over their relationship with the business.")
    purchase_value = st.number_input("Average Purchase Value", min_value=0.0, step=0.01)
    purchase_frequency = st.number_input("Average Purchase Frequency", min_value=0.0, step=0.01)
    customer_lifetime = st.number_input("Customer Lifetime", min_value=0.0, step=0.01)
    if st.button("Calculate LTV", key="ltv"):
        ltv = purchase_value * purchase_frequency * customer_lifetime
        st.metric("LTV", f"${ltv:.2f}")

# 3. LTV to CAC Ratio
with col3:
    st.subheader("LTV to CAC Ratio")
    st.write("Assess the profitability of each customer with this ratio.")
    if st.button("Calculate LTV to CAC Ratio", key="ltv_to_cac"):
        if customers_acquired > 0 and ltv > 0:
            ltv_to_cac_ratio = ltv / cac
            st.metric("LTV to CAC Ratio", f"{ltv_to_cac_ratio:.2f}")
        else:
            st.write("Enter valid LTV and CAC values.")

# 4. Average Revenue Per User (ARPU)
with col4:
    st.subheader("Average Revenue Per User (ARPU)")
    st.write("Calculate the average revenue generated per user.")
    total_revenue = st.number_input("Total Revenue", min_value=0.0, step=0.01)
    total_customers = st.number_input("Total Number of Customers", min_value=1)
    if st.button("Calculate ARPU", key="arpu"):
        arpu = total_revenue / total_customers
        st.metric("ARPU", f"${arpu:.2f}")

# 5. Break-Even Point (BEP)
with col5:
    st.subheader("Break-Even Point (BEP)")
    st.write("Identify the number of units needed to achieve profitability.")
    fixed_costs = st.number_input("Fixed Costs", min_value=0.0, step=0.01)
    unit_price = st.number_input("Unit Price", min_value=0.0, step=0.01)
    variable_cost_per_unit = st.number_input("Variable Cost per Unit", min_value=0.0, step=0.01)
    if st.button("Calculate BEP", key="bep"):
        if unit_price > variable_cost_per_unit:
            bep = fixed_costs / (unit_price - variable_cost_per_unit)
            st.metric("BEP", f"{bep:.2f} units")
        else:
            st.write("Unit Price must be greater than Variable Cost per Unit.")

# Additional section for Summary & Insights
st.markdown("---")
st.subheader("📈 Summary & Insights")
st.write("Here you can review your calculations and gain insights based on these metrics.")

# Display insights based on calculated values
if 'cac' in locals() and 'ltv' in locals() and cac > 0 and ltv > 0:
    st.write(f"Your LTV to CAC Ratio is {ltv_to_cac_ratio:.2f}. A healthy business should ideally have a ratio above 3:1.")
if 'bep' in locals() and bep > 0:
    st.write(f"To break even, you need to sell at least {bep:.2f} units.")

# Tips Section
st.sidebar.title("💡 Tips")
st.sidebar.write("Hover over each metric title for more details.")
st.sidebar.write("""
- **CAC**: Lowering CAC can significantly improve profitability.
- **LTV**: Increasing customer lifetime or frequency boosts LTV.
- **BEP**: Break-even helps gauge minimum sales required for profitability.
""")

# Footer
st.markdown("---")
st.write("Developed to assist startups in tracking and optimizing financial performance effectively.")
