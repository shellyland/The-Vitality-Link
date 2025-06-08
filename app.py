import streamlit as st

# Page configuration
st.set_page_config(page_title="The Vitality Link Introduces GRACE", layout="centered")

# Branding
st.title("GRACE – Guided Resources and Care Experience")
st.subheader("The Vitality Link | Enriching Lifestyle Connections for the Golden Generation")
st.markdown("**Elevating life’s rhythm with trusted, non-medical resources.**")

# Chat-style welcome message
with st.chat_message("GRACE"):
    st.markdown("Welcome to The Vitality Link! I’m GRACE, your AI-powered concierge. As an Honoree, you are more than just a client—you are valued, celebrated, and worthy of seamless solutions. Whether it’s errands, transportation, wellness, or staying connected, I’m here to ensure you have the support you need.")

# Honoree (Client) Intake Form
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
    st.success(f"Thank you, {full_name}! GRACE will follow up at {email}.")
    st.info("Your journey to a fulfilling and intuitive experience begins now.")

# Core services section
st.markdown("### Core Services (May Be Covered by Medicaid, Medicare, or Private Health Insurance)")
st.markdown("""
These services may be eligible under Virginia’s Medicaid Home and Community-Based Services (HCBS) waivers, such as the CCC Plus Waiver, or through supplemental Medicare plans. If a service is not covered by insurance, it would be an out-of-pocket expense or through sponsorships.

- **Errand Assistance** – Grocery shopping, prescription pickup, pet walking, post office trips  
- **Appointment Transportation** – Non-medical rides to doctors, salons, etc.  
- **Wellness & Independence Support** – Encouraging movement, senior workouts, mindfulness, enrichment activities that promote self-sufficiency, friendly visits or calls focused on wellbeing 
- **Technology Assistance** – Smartphones, social media, online tools to stay connected, organizing photos, music, email setup   
- **Community-Based Social Engagement** – Events, volunteer opportunities, legacy-building, group activities, hobby encouragement, games
""")

# Add-on services section
st.markdown("### Out-of-Pocket Services")
st.markdown("""
These services are designed to enrich daily living and may not be covered by insurance. They are available as out-of-pocket services or through sponsorships and grant funding.

- **Financial Literacy Education** – Budgeting, avoiding scams, accessing benefits       
- **Sexual Health Awareness** – Sexual wellness education
""")

# Eligibility section
st.markdown("### Honoree Guidelines")
st.info("""
Our services are primarily designed for able-bodied adults aged 50 and older who seek non-medical solutions. At this time, we are unable to accommodate individuals requiring mobility assistance, personal care, or medical support.  

Eligibility for Medicaid or Medicare covered services depends on needs and assessments.  

""")

# Footer and contact
st.markdown("---")
st.markdown("*GRACE is empowered by IND Designs*")
st.markdown("For support, email **shellyland@thevitalitylink.com**")
