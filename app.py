import streamlit as st

# Page configuration
st.set_page_config(page_title="The Vitality Link", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    /* HEADER IMAGE */
    .header-container {
        text-align: center;
        margin-bottom: 20px;
    }

    .header-container img {
        max-width: 100%;
        height: auto;
        border-radius: 12px;
    }

    /* TAB STYLING */
    div[data-testid="stTabs"] button {
        color: #CD7F32;
        font-weight: bold;
        background-color: #F9F5EF;
        border-bottom: 2px solid transparent;
    }

    div[data-testid="stTabs"] button:hover {
        color: #D8A25C !important;
        border-bottom: 2px solid #D8A25C;
        background-color: #fefbf8;
    }

    div[data-testid="stTabs"] button[aria-selected="true"] {
        color: #CD7F32 !important;
        border-bottom: 3px solid #CD7F32 !important;
        background-color: #fffaf3;
    }

    div[data-testid="stTabs"] > div[role="tablist"] {
        border-bottom: 2px solid #CD7F32;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER IMAGE
st.markdown("""
    <div class="header-container">
        <img src="https://raw.githubusercontent.com/shellyland/vitality-link-assets/main/vitalityheader.jpg" alt="The Vitality Link Header">
    </div>
""", unsafe_allow_html=True)

# Branding
st.title("Golden Lifestyle Solutions")
st.subheader("**Elevating life’s rhythm with trusted, non-medical resources.**")

# MAIN TABS
main_tabs = st.tabs(["Our Roots", "Welcome", "Tiers", "Honoree Form"])

# --- OUR ROOTS ---
with main_tabs[0]:
    st.markdown("## Our Roots")
    st.markdown("""
At **The Vitality Link**, we don’t just serve — we honor.

Life’s rhythm is similar to a tree’s seasonal changes. Just as trees adapt and flourish through each cycle, we too can thrive as we navigate transitions. This principle shapes our core values:

- **Growth** — Leaves represent regeneration and renewal.  
- **Connection** — Branches symbolize a trusted network of supportive resources.  
- **Resilience** — Roots embody the lasting legacy of our founder’s grandparents. Caring for them in their later years was a full-circle privilege — and that experience became the foundation of our mission.

That’s why those we serve are called **Honorees** — because aging should be celebrated, not diminished.
""")

# --- WELCOME ---
with main_tabs[1]:
    st.markdown("### Welcome to The Vitality Link!")
    st.markdown("""
We're your personal concierge. If you're here, you value a higher quality of life — and we can help. 

We proudly refer to those we serve as **Honorees** — because you are more than a client. You are valued, celebrated, and worthy of seamless support. 

Whether you need a hand with errands, non-medical transportation, wellness check-ins, digital support, or social enrichment — we’ll guide you every step of the way.
""")

# --- TIERS ---
with main_tabs[2]:
    st.markdown("## Choose Your Tier")

    tier = st.radio("Select a Service Tier:", ["Bronze", "Silver", "Gold", "Platinum"], horizontal=True)

    if tier == "Bronze":
        st.markdown("### Bronze Tier")
        st.markdown("""
- Local transportation assistance (non-medical)  
- Errand running  
- Wellness check-in (phone call or virtual)
""")
    elif tier == "Silver":
        st.markdown("### Silver Tier")
        st.markdown("""
- All Bronze services  
- Companionship during local outings (appointments, shopping, etc.)  
- Assistance with scheduling appointments
""")
    elif tier == "Gold":
        st.markdown("### Gold Tier")
        st.markdown("""
- All Silver services  
- Event planning and coordination for Honorees (birthday, social, etc.)  
- Dedicated personal concierge for priority scheduling
""")
    elif tier == "Platinum":
        st.markdown("### Platinum Tier")
        st.markdown("""
- All Gold services  
- Custom wellness experience (personalized outings, special requests)  
- Full priority access with on-demand concierge support
""")

# --- FORM TAB ---
with main_tabs[3]:
    st.markdown("### Honoree Form")
    with st.form("honoree_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number (Optional)")
        age = st.number_input("Age", min_value=50, max_value=120, step=1)
        insurance = st.selectbox(
            "Insurance Coverage Type",
            ["Select", "Medicaid", "Medicare", "Private Insurance", "Unsure"]
        )
        tier_selection = st.selectbox(
            "Select Your Tier:",
            ["Select One", "Bronze", "Silver", "Gold", "Platinum"]
        )
        services_interested = st.multiselect(
            "Which services are you interested in?",
            ["Errand Assistance", "Appointment Transportation", "Wellness & Independence Support", "Technology Assistance", 
             "Community-Based Social Engagement", "Fitness & Wellness", "Financial Literacy Education", "Sexual Health Awareness"]
        )
        submit = st.form_submit_button("Submit")

    if submit:
        st.success(f"Thank you, {full_name}! You've selected the **{tier_selection}** tier. We will follow up at {email}.")
        st.info("Your journey to a fulfilling and intuitive experience begins now.")

# --- Footer ---
st.markdown("---")
st.markdown("*Empowered by IND Designs | COPYRIGHT©2025*")
