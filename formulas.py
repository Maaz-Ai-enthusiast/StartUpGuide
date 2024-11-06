import streamlit as st

# Title and Description
st.title("Startup Growth Metrics Calculator")
st.write("A tool to help startups calculate essential growth metrics.")

# Metric Calculation Sections

# 1. Customer Acquisition Cost (CAC)
with st.expander("1. Customer Acquisition Cost (CAC)"):
    st.write("Calculate the cost of acquiring a new customer.")
    marketing_expenses = st.number_input("Total Marketing Expenses", min_value=0.0, step=0.01)
    sales_expenses = st.number_input("Total Sales Expenses", min_value=0.0, step=0.01)
    customers_acquired = st.number_input("Number of Customers Acquired", min_value=1)
    if st.button("Calculate CAC"):
        cac = (marketing_expenses + sales_expenses) / customers_acquired
        st.write(f"Customer Acquisition Cost (CAC): ${cac:.2f}")

# 2. Average Revenue Per User (ARPU)
with st.expander("2. Average Revenue Per User (ARPU)"):
    st.write("Represents the average revenue generated per user.")
    total_revenue = st.number_input("Total Revenue", min_value=0.0, step=0.01)
    total_customers = st.number_input("Total Number of Customers", min_value=1)
    if st.button("Calculate ARPU"):
        arpu = total_revenue / total_customers
        st.write(f"Average Revenue Per User (ARPU): ${arpu:.2f}")

# 3. Lifetime Value (LTV)
with st.expander("3. Lifetime Value (LTV)"):
    st.write("Indicates the total revenue a business expects to earn from a customer.")
    purchase_value = st.number_input("Average Purchase Value", min_value=0.0, step=0.01)
    purchase_frequency = st.number_input("Average Purchase Frequency", min_value=0.0, step=0.01)
    customer_lifetime = st.number_input("Customer Lifetime", min_value=0.0, step=0.01)
    if st.button("Calculate LTV"):
        ltv = purchase_value * purchase_frequency * customer_lifetime
        st.write(f"Lifetime Value (LTV): ${ltv:.2f}")

# 4. LTV to CAC Ratio
with st.expander("4. LTV to CAC Ratio"):
    st.write("Helps assess the profitability of each customer.")
    ltv = st.number_input("Lifetime Value (LTV)", min_value=0.0, step=0.01)
    cac = st.number_input("Customer Acquisition Cost (CAC)", min_value=0.0, step=0.01)
    if st.button("Calculate LTV to CAC Ratio"):
        if cac != 0:
            ltv_to_cac_ratio = ltv / cac
            st.write(f"LTV to CAC Ratio: {ltv_to_cac_ratio:.2f}")
        else:
            st.write("CAC cannot be zero.")

# 5. Break-Even Point (BEP)
with st.expander("5. Break-Even Point (BEP)"):
    st.write("Indicates the number of units needed to cover both fixed and variable costs.")
    fixed_costs = st.number_input("Fixed Costs", min_value=0.0, step=0.01)
    unit_price = st.number_input("Unit Price", min_value=0.0, step=0.01)
    variable_cost_per_unit = st.number_input("Variable Cost per Unit", min_value=0.0, step=0.01)
    if st.button("Calculate BEP"):
        if unit_price > variable_cost_per_unit:
            bep = fixed_costs / (unit_price - variable_cost_per_unit)
            st.write(f"Break-Even Point (BEP): {bep:.2f} units")
        else:
            st.write("Unit Price must be greater than Variable Cost per Unit.")

# 6. Gross Margin
with st.expander("6. Gross Margin"):
    st.write("Shows the profit made from each unit after deducting the production cost.")
    revenue = st.number_input("Revenue", min_value=0.0, step=0.01)
    cogs = st.number_input("Cost of Goods Sold (COGS)", min_value=0.0, step=0.01)
    if st.button("Calculate Gross Margin"):
        if revenue != 0:
            gross_margin = ((revenue - cogs) / revenue) * 100
            st.write(f"Gross Margin: {gross_margin:.2f}%")
        else:
            st.write("Revenue cannot be zero.")

# 7. Contribution Margin
with st.expander("7. Contribution Margin"):
    st.write("Measures the remaining revenue after variable costs.")
    variable_costs = st.number_input("Variable Costs", min_value=0.0, step=0.01)
    if st.button("Calculate Contribution Margin"):
        if revenue != 0:
            contribution_margin = ((revenue - variable_costs) / revenue) * 100
            st.write(f"Contribution Margin: {contribution_margin:.2f}%")
        else:
            st.write("Revenue cannot be zero.")

# 8. Retention Rate
with st.expander("8. Retention Rate"):
    st.write("Calculates the percentage of customers retained over a specific period.")
    end_customers = st.number_input("Customers at End of Period", min_value=0)
    new_customers = st.number_input("New Customers Acquired", min_value=0)
    start_customers = st.number_input("Customers at Start of Period", min_value=1)
    if st.button("Calculate Retention Rate"):
        retention_rate = ((end_customers - new_customers) / start_customers) * 100
        st.write(f"Retention Rate: {retention_rate:.2f}%")

# 9. Churn Rate
with st.expander("9. Churn Rate"):
    st.write("Reflects the percentage of customers who stop using the product or service.")
    lost_customers = st.number_input("Customers Lost During Period", min_value=0)
    if st.button("Calculate Churn Rate"):
        churn_rate = (lost_customers / start_customers) * 100
        st.write(f"Churn Rate: {churn_rate:.2f}%")

# 10. Payback Period
with st.expander("10. Payback Period"):
    st.write("Time required to recover the CAC.")
    monthly_gross_margin_per_customer = st.number_input("Monthly Gross Margin per Customer", min_value=0.0, step=0.01)
    if st.button("Calculate Payback Period"):
        if monthly_gross_margin_per_customer != 0:
            payback_period = cac / monthly_gross_margin_per_customer
            st.write(f"Payback Period: {payback_period:.2f} months")
        else:
            st.write("Monthly Gross Margin per Customer cannot be zero.")

# 11. Average Order Value (AOV)
with st.expander("11. Average Order Value (AOV)"):
    st.write("Average value of each customer order.")
    total_orders = st.number_input("Total Number of Orders", min_value=1)
    if st.button("Calculate AOV"):
        aov = total_revenue / total_orders
        st.write(f"Average Order Value (AOV): ${aov:.2f}")
