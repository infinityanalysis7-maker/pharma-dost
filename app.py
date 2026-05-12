import streamlit as st

# UI Configuration
st.set_page_config(page_title="Pharma-Dost", page_icon="💊", layout="centered")

# Custom CSS for that "Viral Startup" Look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTextInput > div > div > input {
        border-radius: 20px;
        border: 2px solid #4CAF50;
        padding: 10px 20px;
        font-size: 18px;
    }
    .result-card {
        background-color: #1e2130;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #4CAF50;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .savings-badge {
        background-color: #2e7d32;
        color: white;
        padding: 5px 12px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 14px;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 12px;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Data (Top 5 High-Impact Meds)
DATA = {
    "PAN-D": {"salt": "Pantoprazole (40mg) + Domperidone (30mg)", "brand_price": 160, "gen_price": 28},
    "AUGMENTIN 625": {"salt": "Amoxycillin (500mg) + Potassium Clavulanate (125mg)", "brand_price": 201, "gen_price": 60},
    "GLYCOMET 500": {"salt": "Metformin (500mg)", "brand_price": 22, "gen_price": 6},
    "TELMA 40": {"salt": "Telmisartan (40mg)", "brand_price": 95, "gen_price": 14},
    "LIPVAS 10": {"salt": "Atorvastatin (10mg)", "brand_price": 85, "gen_price": 18}
}

# Header Section
st.markdown("<h1 style='text-align: center; color: white;'>💊 Pharma-Dost</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #bbb;'>Search the medicine name to see how much you can save.</p>", unsafe_allow_html=True)

# Search Input
query = st.text_input("", placeholder="Try 'Pan-D' or 'Augmentin'").upper()

if query:
    if query in DATA:
        res = DATA[query]
        savings = res['brand_price'] - res['gen_price']
        percent = int((savings / res['brand_price']) * 100)
        
        # Modern Result Card
        st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h2 style="margin: 0; color: #4CAF50;">{query}</h2>
                    <span class="savings-badge">SAVE {percent}%</span>
                </div>
                <p style="color: #aaa; margin-top: 10px;"><b>Salt:</b> {res['salt']}</p>
                <hr style="border: 0.5px solid #333;">
                <div style="display: flex; justify-content: space-around; text-align: center;">
                    <div>
                        <p style="color: #888; margin: 0;">Market Price</p>
                        <h3 style="color: #ff5252; margin: 0;">₹{res['brand_price']}</h3>
                    </div>
                    <div>
                        <p style="color: #888; margin: 0;">Govt Price</p>
                        <h3 style="color: #4CAF50; margin: 0;">₹{res['gen_price']}</h3>
                    </div>
                </div>
                <div style="background: #2e7d3233; padding: 15px; border-radius: 10px; margin-top: 20px; text-align: center;">
                    <p style="margin: 0; color: #81c784;"><b>You save ₹{savings} per strip!</b></p>
                    <p style="margin: 0; font-size: 14px; color: #81c784;">That's ₹{savings * 12} per year.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("📍 Find Nearest Jan Aushadhi Kendra"):
            st.markdown("[Click here to open Google Maps](https://www.google.com/maps/search/Jan+Aushadhi+Kendra)")
            
    else:
        st.error("Medicine not in MVP list yet. Try 'PAN-D'.")

# Footer
st.markdown("""
    <div class="footer">
        Always consult your doctor before switching medications.<br>
        Built with ❤️ for Bharat.
    </div>
""", unsafe_allow_html=True)
