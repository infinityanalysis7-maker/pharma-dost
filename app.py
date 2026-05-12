import streamlit as st

# UI Configuration
st.set_page_config(page_title="Pharma-Dost", page_icon="💊", layout="centered")

# The "Insane 3D" CSS Injection
st.markdown("""
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e293b, #0f172a, #111827);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glassmorphic Search Bar */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 15px !important;
        color: white !important;
        padding: 15px 25px !important;
        font-size: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
        transition: 0.3s all ease;
    }
    .stTextInput > div > div > input:focus {
        border: 1px solid #4CAF50 !important;
        box-shadow: 0 0 20px rgba(76, 175, 80, 0.4) !important;
    }

    /* 3D Floating Result Card */
    .result-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        margin-top: 30px;
        box-shadow: 20px 20px 60px #080a0f, -20px -20px 60px #161a25;
        transition: transform 0.3s ease;
    }
    .result-card:hover {
        transform: translateY(-5px);
    }

    /* Glowing Savings Badge */
    .savings-badge {
        background: linear-gradient(135deg, #4CAF50, #2E7D32);
        color: white;
        padding: 8px 20px;
        border-radius: 100px;
        font-weight: 800;
        letter-spacing: 1px;
        box-shadow: 0 0 15px rgba(76, 175, 80, 0.5);
        text-transform: uppercase;
    }

    /* Custom Button Style */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# Data
DATA = {
    "PAN-D": {"salt": "Pantoprazole (40mg) + Domperidone (30mg)", "brand_price": 160, "gen_price": 28},
    "AUGMENTIN 625": {"salt": "Amoxycillin (500mg) + Potassium Clavulanate (125mg)", "brand_price": 201, "gen_price": 60},
    "GLYCOMET 500": {"salt": "Metformin (500mg)", "brand_price": 22, "gen_price": 6},
    "TELMA 40": {"salt": "Telmisartan (40mg)", "brand_price": 95, "gen_price": 14}
}

# 3D Header
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="font-size: 3.5rem; font-weight: 800; color: white; margin-bottom: 0; text-shadow: 2px 2px 10px rgba(0,0,0,0.5);">
            💊 Pharma-Dost
        </h1>
        <p style="color: #94a3b8; font-size: 1.2rem; font-weight: 400;">
            Saving Bharat, one pill at a time.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Centered Search
query = st.text_input("", placeholder="Search Brand Name (e.g., PAN-D)").upper()

if query:
    if query in DATA:
        res = DATA[query]
        savings = res['brand_price'] - res['gen_price']
        percent = int((savings / res['brand_price']) * 100)
        
        st.markdown(f"""
            <div class="result-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
                    <h2 style="color: white; margin: 0; font-size: 2rem;">{query}</h2>
                    <span class="savings-badge">SAVE {percent}%</span>
                </div>
                <p style="color: #94a3b8; font-size: 1.1rem;"><b>Salt Composition:</b><br>{res['salt']}</p>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 30px 0;">
                    <div style="background: rgba(255,82,82,0.1); padding: 20px; border-radius: 15px; border: 1px solid rgba(255,82,82,0.2);">
                        <p style="color: #ff5252; margin: 0; font-size: 0.9rem; font-weight: bold; text-transform: uppercase;">Standard Price</p>
                        <h2 style="color: #ff5252; margin: 0;">₹{res['brand_price']}</h2>
                    </div>
                    <div style="background: rgba(76,175,80,0.1); padding: 20px; border-radius: 15px; border: 1px solid rgba(76,175,80,0.2);">
                        <p style="color: #4CAF50; margin: 0; font-size: 0.9rem; font-weight: bold; text-transform: uppercase;">Generic Price</p>
                        <h2 style="color: #4CAF50; margin: 0;">₹{res['gen_price']}</h2>
                    </div>
                </div>
                
                <div style="background: linear-gradient(90deg, rgba(76,175,80,0.2) 0%, rgba(46,125,50,0.2) 100%); padding: 20px; border-radius: 15px; text-align: center;">
                    <h3 style="margin: 0; color: #81c784;">Total Savings: ₹{savings} / strip</h3>
                    <p style="margin: 0; color: #81c784; opacity: 0.8;">Estimated annual savings: ₹{savings * 12}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("") # Spacer
        if st.button("📍 Find Nearest Jan Aushadhi Kendra"):
            st.markdown("[Opening Google Maps...](https://www.google.com/maps/search/Jan+Aushadhi+Kendra)")
    else:
        st.warning("We're currently adding more medicines to our 3D vault. Try 'PAN-D'!")

st.markdown("<div style='margin-top: 100px; text-align: center; color: #475569; font-size: 0.8rem;'>Built with pride for a healthier India.</div>", unsafe_allow_html=True)
