# Streamlit Skincare Assistant 
import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Skincare Assistant",
                   page_icon="💅",
                   layout="wide")

# --- Styling ---
st.markdown("""
    <style>
        .title-style {
            font-size: 52px;
            font-weight: 600;
            font-family: 'Georgia', serif;
            color: #B76E79;
            text-align: center;
            margin-bottom: 30px;
        }
        .section-header {
            font-size: 26px;
            color: #5D3A58;
            margin-top: 40px;
            font-weight: bold;
            border-bottom: 2px solid #eac9d1;
        }
        .product-title {
            font-size: 20px;
            font-weight: 600;
            color: #9C2C77;
        }
        .product-card {
            background-color: #fdf6f9;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(230, 202, 215, 0.4);
            margin-bottom: 20px;
        }
    </style>
""",
            unsafe_allow_html=True)

st.markdown('<div class="title-style">✨ Personalized Skincare Assistant</div>',
            unsafe_allow_html=True)

# --- Product Database ---
skincare_routines = {
    ("oily", "acne"): {
        "AM": [
            {"name": "Clean & Clear Foaming Face Wash", "type": "Face Wash", "desc": "Oil control cleanser.", "price": "$5", "rating": 4.4},
            {"name": "The Ordinary Niacinamide", "type": "Serum", "desc": "Controls oil & acne.", "price": "$6", "rating": 4.6},
            {"name": "Neutrogena Oil-Free Moisturizer", "type": "Moisturizer", "desc": "Non-comedogenic.", "price": "$10", "rating": 4.5},
            {"name": "La Roche-Posay Anthelios SPF 60", "type": "Sunscreen", "desc": "SPF for oily skin.", "price": "$35", "rating": 4.8}
        ],
        "PM": [
            {"name": "Simple Gel Wash", "type": "Face Wash", "desc": "Gentle night cleanser.", "price": "$7", "rating": 4.2},
            {"name": "COSRX AHA BHA Serum", "type": "Serum", "desc": "Acne exfoliant.", "price": "$18", "rating": 4.6},
            {"name": "Neutrogena Hydro Boost", "type": "Moisturizer", "desc": "Hydrating gel.", "price": "$14", "rating": 4.7},
            {"name": "The Inkey List Retinol", "type": "Retinol", "desc": "Anti-acne retinol.", "price": "$10", "rating": 4.5}
        ]
    },
    ("oily", "dullness"): {
        "AM": [
            {"name": "CeraVe Foaming Cleanser", "type": "Face Wash", "desc": "Brightens and balances oil.", "price": "$13", "rating": 4.5},
            {"name": "Good Molecules Niacinamide Brightening Toner", "type": "Toner", "desc": "Evens out tone.", "price": "$14", "rating": 4.4},
            {"name": "L'Oreal Revitalift Vitamin C Serum", "type": "Serum", "desc": "Radiance booster.", "price": "$25", "rating": 4.6},
            {"name": "Biore UV Aqua Rich SPF 50+", "type": "Sunscreen", "desc": "Lightweight sunscreen.", "price": "$11", "rating": 4.7}
        ],
        "PM": [
            {"name": "Neutrogena Deep Clean Cleanser", "type": "Face Wash", "desc": "Deep pore cleanser.", "price": "$8", "rating": 4.3},
            {"name": "The Ordinary Glycolic Acid 7%", "type": "Toner", "desc": "Exfoliating for glow.", "price": "$10", "rating": 4.5},
            {"name": "CeraVe PM Lotion", "type": "Moisturizer", "desc": "Oil-free hydration.", "price": "$12", "rating": 4.6},
            {"name": "Naturium Retinol Serum", "type": "Retinol", "desc": "Refines skin texture.", "price": "$20", "rating": 4.5}
        ]
    },
    ("oily", "aging"): {
        "AM": [
            {"name": "La Roche-Posay Effaclar Gel Cleanser", "type": "Face Wash", "desc": "Oil-balancing and anti-aging.", "price": "$16", "rating": 4.6},
            {"name": "Olay Regenerist Vitamin C + Peptide 24", "type": "Serum", "desc": "Brightens & firms.", "price": "$30", "rating": 4.7},
            {"name": "Paula's Choice CLEAR Oil-Free Moisturizer", "type": "Moisturizer", "desc": "Anti-aging & acne safe.", "price": "$29", "rating": 4.6},
            {"name": "EltaMD UV Clear SPF 46", "type": "Sunscreen", "desc": "Great for acne-prone, aging skin.", "price": "$39", "rating": 4.8}
        ],
        "PM": [
            {"name": "The Inkey List Salicylic Cleanser", "type": "Face Wash", "desc": "Controls breakouts.", "price": "$10", "rating": 4.4},
            {"name": "The Ordinary Granactive Retinoid 2%", "type": "Retinoid", "desc": "Anti-aging without irritation.", "price": "$10", "rating": 4.5},
            {"name": "CeraVe Skin Renewing Night Cream", "type": "Moisturizer", "desc": "Peptides for firm skin.", "price": "$18", "rating": 4.6}
        ]
    },
    ("dry", "acne"): {
        "AM": [
            {"name": "Cetaphil Gentle Skin Cleanser", "type": "Face Wash", "desc": "Hydrating & acne-friendly.", "price": "$9", "rating": 4.6},
            {"name": "The Ordinary Niacinamide", "type": "Serum", "desc": "Reduces acne & hydrates.", "price": "$6", "rating": 4.6},
            {"name": "CeraVe Moisturizing Cream", "type": "Moisturizer", "desc": "Deep hydration.", "price": "$13", "rating": 4.8},
            {"name": "Aveeno Positively Radiant SPF 30", "type": "Sunscreen", "desc": "Non-irritating SPF.", "price": "$16", "rating": 4.5}
        ],
        "PM": [
            {"name": "La Roche-Posay Toleriane Hydrating Cleanser", "type": "Face Wash", "desc": "Hydrating cleanser.", "price": "$15", "rating": 4.7},
            {"name": "Paula's Choice 2% BHA", "type": "Exfoliant", "desc": "Gentle acne treatment.", "price": "$29", "rating": 4.6},
            {"name": "Neutrogena Hydro Boost Gel-Cream", "type": "Moisturizer", "desc": "Deep hydration.", "price": "$17", "rating": 4.7}
        ]
    },
    ("dry", "dullness"): {
        "AM": [
            {"name": "Eucerin Hydrating Cleanser", "type": "Face Wash", "desc": "Gentle cleansing.", "price": "$11", "rating": 4.5},
            {"name": "La Roche-Posay Vitamin C Serum", "type": "Serum", "desc": "Brightens dull skin.", "price": "$40", "rating": 4.7},
            {"name": "The Ordinary Natural Moisturizing Factors", "type": "Moisturizer", "desc": "Restores skin barrier.", "price": "$8", "rating": 4.6},
            {"name": "EltaMD UV Daily SPF 40", "type": "Sunscreen", "desc": "Hydrating sunscreen.", "price": "$35", "rating": 4.8}
        ],
        "PM": [
            {"name": "CeraVe Hydrating Cleanser", "type": "Face Wash", "desc": "Moisture-retaining.", "price": "$13", "rating": 4.7},
            {"name": "The Ordinary Lactic Acid 5%", "type": "Exfoliant", "desc": "Gentle resurfacer.", "price": "$8", "rating": 4.5},
            {"name": "First Aid Beauty Ultra Repair Cream", "type": "Moisturizer", "desc": "Deep nourishment.", "price": "$34", "rating": 4.7}
        ]
    },
    ("dry", "aging"): {
        "AM": [
            {"name": "Vanicream Gentle Cleanser", "type": "Face Wash", "desc": "Non-drying cleanser.", "price": "$10", "rating": 4.6},
            {"name": "Olay Regenerist Collagen Peptide", "type": "Serum", "desc": "Plumps & firms.", "price": "$30", "rating": 4.7},
            {"name": "CeraVe Skin Renewing Day Cream", "type": "Moisturizer", "desc": "SPF + anti-aging.", "price": "$22", "rating": 4.5},
            {"name": "Neutrogena Rapid Wrinkle Repair SPF 30", "type": "Sunscreen", "desc": "Anti-wrinkle SPF.", "price": "$25", "rating": 4.6}
        ],
        "PM": [
            {"name": "CeraVe Cream to Foam Cleanser", "type": "Face Wash", "desc": "Cleans & hydrates.", "price": "$13", "rating": 4.5},
            {"name": "The Ordinary Retinol 0.5% in Squalane", "type": "Retinol", "desc": "Anti-aging night serum.", "price": "$10", "rating": 4.5},
            {"name": "Eucerin Q10 Anti-Wrinkle Cream", "type": "Moisturizer", "desc": "Nourishes & firms.", "price": "$12", "rating": 4.6}
        ]
    },
    ("combination", "acne"): {
        "AM": [
            {"name": "Neutrogena Oil-Free Acne Wash", "type": "Face Wash", "desc": "Controls breakouts.", "price": "$9", "rating": 4.4},
            {"name": "The Ordinary Niacinamide", "type": "Serum", "desc": "Balances T-zone oil.", "price": "$6", "rating": 4.6},
            {"name": "Clinique Dramatically Different Gel", "type": "Moisturizer", "desc": "Lightweight hydration.", "price": "$30", "rating": 4.5},
            {"name": "EltaMD UV Clear SPF 46", "type": "Sunscreen", "desc": "Great for acne-prone skin.", "price": "$39", "rating": 4.8}
        ],
        "PM": [
            {"name": "La Roche-Posay Effaclar Cleanser", "type": "Face Wash", "desc": "For oily/combination skin.", "price": "$16", "rating": 4.6},
            {"name": "COSRX AHA BHA Toner", "type": "Toner", "desc": "Exfoliates & treats acne.", "price": "$15", "rating": 4.5},
            {"name": "Neutrogena Hydro Boost", "type": "Moisturizer", "desc": "Hydration for dry areas.", "price": "$14", "rating": 4.7}
        ]
    },
    ("combination", "dullness"): {
        "AM": [
            {"name": "Simple Refreshing Facial Wash", "type": "Face Wash", "desc": "Brightens skin gently.", "price": "$7", "rating": 4.3},
            {"name": "The Ordinary Ascorbyl Glucoside Solution 12%", "type": "Serum", "desc": "Brightening Vitamin C.", "price": "$10", "rating": 4.4},
            {"name": "Belif Aqua Bomb", "type": "Moisturizer", "desc": "Hydrating & light.", "price": "$38", "rating": 4.6},
            {"name": "Supergoop! Unseen Sunscreen SPF 40", "type": "Sunscreen", "desc": "Invisible SPF.", "price": "$36", "rating": 4.7}
        ],
        "PM": [
            {"name": "Neutrogena Bright Boost Gel Cleanser", "type": "Face Wash", "desc": "Polishes & refines.", "price": "$8", "rating": 4.3},
            {"name": "The Ordinary Mandelic Acid 10%", "type": "Exfoliant", "desc": "Brightens and resurfaces.", "price": "$7", "rating": 4.5},
            {"name": "Glow Recipe Watermelon Glow Sleeping Mask", "type": "Moisturizer", "desc": "Radiance overnight.", "price": "$45", "rating": 4.6}
        ]
    },
    ("combination", "aging"): {
        "AM": [
            {"name": "CeraVe Hydrating Cream-to-Foam Cleanser", "type": "Face Wash", "desc": "Gentle yet effective.", "price": "$13", "rating": 4.6},
            {"name": "Vichy LiftActiv Vitamin C Serum", "type": "Serum", "desc": "Targets early signs of aging.", "price": "$30", "rating": 4.6},
            {"name": "Neutrogena Hydro Boost Water Gel", "type": "Moisturizer", "desc": "Oil-free anti-aging hydration.", "price": "$14", "rating": 4.7},
            {"name": "Aveeno Positively Radiant Daily Moisturizer SPF 30", "type": "Sunscreen", "desc": "Anti-aging with SPF.", "price": "$20", "rating": 4.5}
        ],
        "PM": [
            {"name": "Youth to the People Superfood Cleanser", "type": "Face Wash", "desc": "Balances skin.", "price": "$36", "rating": 4.6},
            {"name": "The Inkey List Retinol", "type": "Retinol", "desc": "Reduces fine lines.", "price": "$10", "rating": 4.5},
            {"name": "CeraVe Skin Renewing Night Cream", "type": "Moisturizer", "desc": "Hydration & repair.", "price": "$18", "rating": 4.6}
        ]
    },
    ("sensitive", "acne"): {
        "AM": [
            {"name": "Avene Tolerance Extremely Gentle Cleanser", "type": "Face Wash", "desc": "Ultra-mild cleanser.", "price": "$24", "rating": 4.5},
            {"name": "Paula’s Choice Calm Repairing Serum", "type": "Serum", "desc": "Soothes redness & acne.", "price": "$34", "rating": 4.6},
            {"name": "Cetaphil Daily Hydrating Lotion", "type": "Moisturizer", "desc": "Soothing moisturizer.", "price": "$12", "rating": 4.7},
            {"name": "Blue Lizard Sensitive SPF 30", "type": "Sunscreen", "desc": "Mineral-based SPF.", "price": "$15", "rating": 4.6}
        ],
        "PM": [
            {"name": "La Roche-Posay Toleriane Dermo-Cleanser", "type": "Face Wash", "desc": "Cleanses without irritation.", "price": "$15", "rating": 4.7},
            {"name": "Avene TriAcneal Night Smoothing Lotion", "type": "Treatment", "desc": "Anti-acne & gentle.", "price": "$45", "rating": 4.5},
            {"name": "Avene Skin Recovery Cream", "type": "Moisturizer", "desc": "Calms skin overnight.", "price": "$35", "rating": 4.6}
        ]
    },
    ("sensitive", "dullness"): {
        "AM": [
            {"name": "La Roche-Posay Toleriane Hydrating Gentle Cleanser", "type": "Face Wash", "desc": "Non-stripping wash.", "price": "$16", "rating": 4.6},
            {"name": "The Ordinary Ascorbyl Tetraisopalmitate", "type": "Serum", "desc": "Gentle brightening.", "price": "$17", "rating": 4.4},
            {"name": "Aveeno Calm + Restore Oat Gel", "type": "Moisturizer", "desc": "Soothes sensitive skin.", "price": "$24", "rating": 4.7},
            {"name": "EltaMD UV Elements SPF 44", "type": "Sunscreen", "desc": "Mineral SPF for sensitive skin.", "price": "$36", "rating": 4.8}
        ],
        "PM": [
            {"name": "Avene Gentle Milk Cleanser", "type": "Face Wash", "desc": "Mild makeup remover.", "price": "$20", "rating": 4.5},
            {"name": "First Aid Beauty Facial Radiance Pads", "type": "Exfoliant", "desc": "Gentle glow pads.", "price": "$17", "rating": 4.6},
            {"name": "La Roche-Posay Cicaplast Baume B5", "type": "Moisturizer", "desc": "Soothes irritation & repairs.", "price": "$15", "rating": 4.7}
        ]
    },
    ("sensitive", "aging"): {
        "AM": [
            {"name": "Eucerin Redness Relief Cleanser", "type": "Face Wash", "desc": "Gentle and soothing.", "price": "$10", "rating": 4.5},
            {"name": "The Ordinary Buffet + Copper Peptides", "type": "Serum", "desc": "Supports skin health.", "price": "$30", "rating": 4.6},
            {"name": "Neutrogena Calm & Restore Oat Gel", "type": "Moisturizer", "desc": "Hydrating & calming.", "price": "$20", "rating": 4.5},
            {"name": "CeraVe Hydrating Mineral Sunscreen SPF 30", "type": "Sunscreen", "desc": "Sensitive-safe SPF.", "price": "$15", "rating": 4.6}
        ],
        "PM": [
            {"name": "Avene Tolerance Control Cleanser", "type": "Face Wash", "desc": "Extra gentle cleanser.", "price": "$25", "rating": 4.6},
            {"name": "The Ordinary Retinol 0.2% in Squalane", "type": "Retinol", "desc": "Minimal irritation retinol.", "price": "$8", "rating": 4.4},
            {"name": "La Roche-Posay Toleriane Ultra Night", "type": "Moisturizer", "desc": "Soothing night cream.", "price": "$25", "rating": 4.7}
        ]
    }
}



# --- Routine Calendar ---
def show_routine_calendar(age, concern):
    st.markdown("<div class='section-header'>📅 Weekly Skincare Calendar</div>",
                unsafe_allow_html=True)
    calendar = {
        "Monday": "AM + PM routine",
        "Tuesday": "AM + PM routine",
        "Wednesday":
        "AM + PM + Retinol (night)" if age > 30 else "AM + PM routine",
        "Thursday": "AM + PM routine",
        "Friday": "AM + PM + Exfoliation",
        "Saturday":
        "AM + PM + Retinol (night)" if age > 30 else "AM + PM routine",
        "Sunday": "AM + PM + Hydrating mask"
    }
    for day, routine in calendar.items():
        st.write(f"{day}: {routine}")


# --- Ingredient Sensitivity Filter ---
def filter_products(products, avoid_ingredients):
    if not avoid_ingredients:
        return products
    filtered = []
    for product in products:
        if not any(ingredient.lower() in product['desc'].lower()
                   for ingredient in avoid_ingredients):
            filtered.append(product)
    return filtered


# --- User Inputs ---
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 Your name:")
with col2:
    age = st.number_input("🎂 Your age:", min_value=10, max_value=100)

if name and age:
    st.markdown('<div class="section-header">Your Skincare Preferences</div>',
                unsafe_allow_html=True)

    s_type = st.selectbox("💧 Skin Type:",
                          ["", "oily", "dry", "sensitive", "combination"])
    s_concern = st.selectbox("🔎 Primary Concern:",
                             ["", "acne", "aging", "dullness"])
    routine_time = st.radio("🕒 Routine Time:", ["AM", "PM"], horizontal=True)

    avoid_input = st.text_input("🚫 Ingredients to Avoid (comma-separated):")
    avoid_ingredients = [
        i.strip().lower() for i in avoid_input.split(",") if i.strip()
    ] if avoid_input else []

    if st.button("🔍 Show My Routine"):
        if (s_type, s_concern) in skincare_routines:
            st.markdown(
                f"<div class='section-header'>🧼 Your {routine_time} Skincare</div>",
                unsafe_allow_html=True)
            products = skincare_routines[(s_type, s_concern)][routine_time]
            filtered_products = filter_products(products, avoid_ingredients)

            if filtered_products:
                for product in filtered_products:
                    with st.container():
                        st.markdown(f"<div class='product-card'>",
                                    unsafe_allow_html=True)
                        st.markdown(
                            f"<div class='product-title'>{product['name']}</div>",
                            unsafe_allow_html=True)
                        st.markdown(
                            f"📋 {product['desc']}  \n💲 {product['price']}  \n⭐ {product['rating']}/5.0"
                        )
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning(
                    "No suitable products found after filtering out unwanted ingredients."
                )
        else:
            st.info(
                "🚫 No products found for the selected skin type and concern.")

        show_routine_calendar(age, s_concern)
        st.info(
            "⚠ Always patch test new products. Consult a dermatologist for persistent issues."
        )

    # --- Reminder Suggestion ---
    st.markdown("<div class='section-header'>⏰ Reminder Tip</div>",
                unsafe_allow_html=True)
    st.info(
        "Add reminders for your AM and PM routine in your phone's calendar or use Google Assistant/Siri for recurring skincare prompts."
    )
