import streamlit as st

st.image("your_header_image.jpg", use_column_width=True)

# Page configuration
st.set_page_config(page_title="The Vitality Link | Golden Lifestyle Solutions", layout="centered")

# Custom CSS for bronze styling (tabs + mail link)
st.markdown("""
    <style>
    /* TAB STYLING */
    div[data-testid="stTabs"] button {
        color: #CD7F32;  /* Classic Bronze */
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

    /* REMOVE/OVERRIDE DEFAULT RED LINE UNDER TABS */
    div[data-testid="stTabs"] > div[role="tablist"] {
        border-bottom: 2px solid #CD7F32;  /* Bronze line instead of red */
    }

    /* MAILTO LINK STYLING */
    a[href^="mailto"] {
        color: #CD7F32 !important;
        font-weight: bold;
        text-decoration: none;
    }

    a[href^="mailto"]:hover {
        color: #D8A25C !important;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)


# Branding
st.title("The Vitality Link | Golden Lifestyle Solutions")
st.subheader("**Elevating life’s rhythm with trusted, non-medical resources.**")

# Create tabs
roots_tab, welcome_tab, services_tab, form_tab = st.tabs(["Our Roots", "Welcome", "Services", "Honoree Form"])

# Roots tab
with roots_tab:
    st.markdown("## Our Roots")
    st.markdown("""
At **The Vitality Link**, we don’t just serve — we honor.
Our family tree logo represents more than a design — it reflects our values:

- **Connection** – A trusted network of resources and meaningful relationships  
- **Growth** – Supporting vitality, independence, and well-being  
- **Roots** – Inspired by **Ma Clemmie**, grandmother/second mom — whose strength, love, and resilience shaped my world. When she became unwell, I had the honor of caring for her — a full-circle act of love that now guides everything I do.  
- **Elevation** – Because life’s rhythm, like trees, is about rising, reaching, and thriving — at every age.
""")

# Welcome tab
with welcome_tab:
        st.markdown("### Welcome to The Vitality Link!")
        st.markdown("""
        We're your personal concierge. So, if you're here, you value a higher quality of life — and we can help. 
        
        We call our clients **Honorees** because you are more than just a client — you are valued, celebrated, and worthy of seamless support. 
        
        Whether you need a hand with errands, non-medical transportation, wellness check-ins, digital support or social enrichment — we’ll guide you every step of the way.
        """)

# Services tab
with services_tab:
    st.markdown("### Core Services (May Be Covered by Medicaid, Medicare, or Private Health Insurance)")
    st.markdown("""
    These services may be eligible under Virginia’s Medicaid Home and Community-Based Services (HCBS) waivers, such as the CCC Plus Waiver, or through supplemental Medicare plans. If a service is not covered by insurance, it would be an out-of-pocket expense or via sponsorships.

    - **Errand Assistance** – Grocery shopping, prescription pickup, pet walking, post office trips  
    - **Appointment Transportation** – Non-medical rides to doctors, salons, etc.  
    - **Wellness & Independence Support** – Encouraging movement, senior workouts, mindfulness, enrichment activities that promote self-sufficiency, friendly visits or calls focused on wellbeing 
    - **Technology Assistance** – Smartphones, social media, online tools to stay connected, organizing photos, music, email setup   
    - **Community-Based Social Engagement** – Events, volunteer opportunities, legacy-building, group activities, hobby encouragement, games
    """)

    st.markdown("### Out-of-Pocket Services")
    st.markdown("""
    These services are designed to enrich daily living and may not be covered by insurance. They are available as out-of-pocket services or through sponsorships and grant funding.

    - **Financial Literacy Education** – Budgeting, avoiding scams, accessing benefits       
    - **Sexual Health Awareness** – Sexual wellness education
    """)

    st.markdown("### Honoree Guidelines")
    st.info("""
    Our services are primarily designed for able-bodied adults aged 50 and older who seek non-medical solutions. At this time, we are unable to accommodate individuals requiring mobility assistance, personal care, or medical support.  

    Eligibility for Medicaid or Medicare-covered support may require a non-medical needs assessment conducted through authorized channels. 
    """)

# Honoree Form tab
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

# Footer and contact
st.markdown("---")
st.markdown("*Empowered by IND Designs*")





