import streamlit as st

# Page configuration
st.set_page_config(page_title="The Vitality Link", layout="centered")

# Custom CSS for tier colors and header image
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

    /* BRONZE TAB */
    div[data-testid="stTabs"] button:nth-child(1) {
        color: #CD7F32;  /* Bronze */
        font-weight: bold;
        background-color: #F9F5EF;
        border-bottom: 2px solid transparent;
    }

    div[data-testid="stTabs"] button:nth-child(1):hover {
        color: #D8A25C !important;
        border-bottom: 2px solid #D8A25C;
        background-color: #fefbf8;
    }

    div[data-testid="stTabs"] button:nth-child(1)[aria-selected="true"] {
        color: #CD7F32 !important;
        border-bottom: 3px solid #CD7F32 !important;
        background-color: #fffaf3;
    }

    /* SILVER TAB */
    div[data-testid="stTabs"] button:nth-child(2) {
        color: #C0C0C0;  /* Silver */
        font-weight: bold;
        background-color: #F9F5EF;
        border-bottom: 2px solid transparent;
    }

    div[data-testid="stTabs"] button:nth-child(2):hover {
        color: #A9A9A9 !important;
        border-bottom: 2px solid #A9A9A9;
        background-color: #fefbf8;
    }

    div[data-testid="stTabs"] button:nth-child(2)[aria-selected="true"] {
        color: #C0C0C0 !important;
        border-bottom: 3px solid #C0C0C0 !important;
        background-color: #fffaf3;
    }

    /* GOLD TAB */
    div[data-testid="stTabs"] button:nth-child(3) {
        color: #FFD700;  /* Bright Gold */
        font-weight: bold;
        background-color: #F9F5EF;
        border-bottom: 2px solid transparent;
    }

    div[data-testid="stTabs"] button:nth-child(3):hover {
        color: #FFC300 !important;
        border-bottom: 2px solid #FFC300;
        background-color: #fefbf8;
    }

    div[data-testid="stTabs"] button:nth-child(3)[aria-selected="true"] {
        color: #FFD700 !important;
        border-bottom: 3px solid #FFD700 !important;
        background-color: #fffaf3;
    }

    /* PLATINUM TAB */
    div[data-testid="stTabs"] button:nth-child(4) {
        color: #E5E4E2;  /* Platinum */
        font-weight: bold;
        background-color: #F9F5EF;
        border-bottom: 2px solid transparent;
    }

    div[data-testid="stTabs"] button:nth-child(4):hover {
        color: #D3D3D3 !important;
        border-bottom: 2px solid #D3D3D3;
        background-color: #fefbf8;
    }

    div[data-testid="stTabs"] button:nth-child(4)[aria-selected="true"] {
        color: #E5E4E2 !important;
        border-bottom: 3px solid #E5E4E2 !important;
        background-color: #fffaf3;
    }

    div[data-testid="stTabs"] > div[role="tablist"] {
        border-bottom: 2px solid #CD7F32;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER IMAGE
st.markdown("""
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/shellyland/vitality-link-assets/main/vitalityheader.jpg" alt="The Vitality Link Header" style="width: 100%; max-width: 800px; border-radius: 12px;">
    </div>
""", unsafe_allow_html=True)

# Branding
st.title("Golden Lifestyle Solutions")
st.subheader("**Elevating life’s rhythm with trusted, non-medical resources.**")

# Top Tabs
roots_tab, welcome_tab, tiers_tab, form_tab = st.tabs(["Our Roots", "Welcome", "Tiers", "Honoree Form"])

# Roots Tab
with roots_tab:
    st.markdown("## Our Roots")
    st.markdown("""
At **The Vitality Link**, we don’t just serve — we honor.

Life’s rhythm is similar to a tree’s seasonal changes. Just as trees adapt and flourish through each cycle, we too can thrive as we navigate transitions. This principle shapes our core values:

- **Growth** — Leaves represent regeneration and renewal.
- **Connection** — Branches symbolize a trusted network of supportive resources.
- **Resilience** — Roots embody the lasting legacy of our founder’s grandparents. Caring for them in their later years was a full-circle privilege — and that experience became the foundation of our mission.
""")

# Welcome Tab
with welcome_tab:
    st.markdown("### Welcome to The Vitality Link!")
    st.markdown("""
    We're your personal concierge. If you're here, you value a higher quality of life — and we can help. 
    
    We call our clients **Honorees** because you are more than just a client — you are valued, celebrated, and worthy of seamless support. 
    
    Whether you need a hand with errands, non-medical transportation, wellness check-ins, digital support, or social enrichment — we’ll guide you every step of the way.
    """)

# Tiers Tab with Sub-Tabs
with tiers_tab:
    st.markdown("### Our Service Tiers")

    bronze_tab, silver_tab, gold_tab, platinum_tab = st.tabs(["Bronze", "Silver", "Gold", "Platinum"])

    with bronze_tab:
        st.markdown("## Bronze Package")
        st.markdown("""
        - Local transportation assistance (non-medical)
        - Errand running
        - Wellness check-in (phone call or virtual)
        """)

    with silver_tab:
        st.markdown("## Silver Package")
        st.markdown("""
        - All Bronze services
        - Companionship during local outings (appointments, shopping, etc.)
        - Assistance with scheduling appointments
        """)

    with gold_tab:
        st.markdown("## Gold Package")
        st.markdown("""
        - All Silver services
        - Event planning and coordination for honorees (birthday, social, etc.)
        - Dedicated personal concierge for priority scheduling
        """)

    with platinum_tab:
        st.markdown("## Platinum Package")
        st.markdown("""
        - All Gold services
        - Custom wellness experience (personalized outings, special requests)
        - Full priority access with on-demand concierge support
        """)

# Honoree Form Tab
with form_tab:
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
        services_interested = st.multiselect(
            "Which services are you interested in?",
            ["Errand Assistance", "Appointment Transportation", "Wellness & Independence Support", "Technology Assistance", 
             "Community-Based Social Engagement", "Fitness & Wellness", "Financial Literacy Education", "Sexual Health Awareness"]
        )
        submit = st.form_submit_button("Submit")

    if submit:
        st.success(f"Thank you, {full_name}! We will follow up at {email}.")
        st.info("Your journey to a fulfilling and intuitive experience begins now.")

# Footer
st.markdown("---")
st.markdown("*Empowered by IND Designs | COPYRIGHT©2025*")
