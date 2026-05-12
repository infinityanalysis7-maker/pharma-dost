# Save this as app.py
# If using Replit, search for 'Streamlit' in the Packages tab first!

import streamlit as st

# 2026 Most Common Generic Mappings
DATA = {
    "PAN-D": {"salt": "Pantoprazole (40mg) + Domperidone (30mg)", "brand_price": 160, "gen_price": 28},
    "AUGMENTIN 625": {"salt": "Amoxycillin (500mg) + Potassium Clavulanate (125mg)", "brand_price": 201, "gen_price": 60},
    "GLYCOMET 500": {"salt": "Metformin (500mg)", "brand_price": 22, "gen_price": 6},
    "TELMA 40": {"salt": "Telmisartan (40mg)", "brand_price": 95, "gen_price": 14},
    "LIPVAS 10": {"salt": "Atorvastatin (10mg)", "brand_price": 85, "gen_price": 18}
}

st.set_page_config(page_title="Pharma-Dost", page_icon="💊")

st.title("💊 Pharma-Dost")
st.subheader("Stop overpaying for medicines.")

query = st.text_input("Enter Brand Name (e.g. Pan-D, Augmentin):").upper()

if query:
    if query in DATA:
        res = DATA[query]
        savings = res['brand_price'] - res['gen_price']
        percent = int((savings / res['brand_price']) * 100)
        
        st.success(f"Found Generic Alternative for {query}!")
        
        col1, col2 = st.columns(2)
        col1.metric("Branded Price", f"₹{res['brand_price']}")
        col2.metric("Generic Price", f"₹{res['gen_price']}", f"-{percent}%", delta_color="normal")
        
        st.info(f"**Chemical Salt:** {res['salt']}")
        st.warning(f"💡 You save **₹{savings}** per strip! That's **₹{savings * 12}** a year if taken monthly.")
        
        if st.button("Find Nearest Jan Aushadhi Store"):
            st.write(f"Searching for stores near you... [Google Maps Link](https://www.google.com/maps/search/Jan+Aushadhi+Kendra)")
    else:
        st.error("Medicine not in MVP list. Try 'Pan-D' or 'Telma 40'.")

st.markdown("---")
st.caption("Note: Always consult your doctor before switching medications.")
