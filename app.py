import streamlit as st

# Page configuration
st.set_page_config(page_title="The Vitality Link Introduces GRACE", layout="centered")

# Branding
st.title("GRACE – Guided Resources and Care Experience")
st.subheader("The Vitality Link | Enriching Lifestyle Connections for the Golden Generation")
st.markdown("**Enhancing life’s rhythm with trusted, non-medical resources.**")

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
        ["Errand Assistance", "Transportation", "Wellness Check-Ins", "Social Events", 
         "Financial Literacy", "Fitness & Wellness", "Community Engagment", "Digital Support", "Sexual Health Awareness", "Event Planning"]
    )
    submit = st.form_submit_button("Submit")

if submit:
    st.success(f"Thank you, {full_name}! GRACE will follow up at {email}.")
    st.info("You're now on your way to personalized, dignified lifestyle support.")

# Core services section
st.markdown("### Core Services (May Be Covered by Medicaid, Medicare Advantage, or Private Health Insurance)")
st.markdown("""
These services may be eligible under Virginia’s Medicaid Home and Community-Based Services (HCBS) waivers, such as the CCC Plus Waiver, or through supplemental Medicare Advantage plans. If a service is not covered by insurance, it can be added as a private-pay option or through sponsorships.

- **Errand Assistance** – Grocery shopping, prescription pickup, pet walking, post office trips  
- **Appointment Transportation** – Non-medical rides to doctors, wellness visits, salons, etc.  
- **Wellness & Independence Support** – Encouraging movement, mindfulness, and enrichment activities that promote self-sufficiency, friendly visits or calls focused on wellbeing  (non-clinical prompts)  
- **Technology Assistance** – Smartphones, social media, and online tools to stay connected, Organizing photos, music, email setup   
- **Community-Based Social Engagement** – Events, volunteer opportunities, legacy-building and group activities, hobby encouragement, games
- **Fitness & Wellness Referrals** – Trainers, senior workouts, group activities
""")

# Add-on services section
st.markdown("### Add-On Enhancements (Private Pay or Grant-Funded Options)")
st.markdown("""
These services are designed to enhance a vibrant lifestyle and are available as add-ons or through sponsorships.

- **Financial Literacy Education** – Budgeting, avoiding scams, accessing benefits       
- **Sexual Health Awareness** – Sexual wellness education
""")

# Eligibility section
st.markdown("### Coverage Guidelines")
st.info("""
Our services are primarily designed for able-bodied adults aged 50 and older who seek non-medical solutions. At this time, we are unable to accommodate individuals requiring mobility assistance, personal care, or medical support.  
Eligibility for Medicaid or Medicare-covered services depends on needs and assessments.  

""")

# Footer and contact
st.markdown("---")
st.markdown("*GRACE is empowered by IND Designs*")
st.markdown("For support, email **shellyland@thevitalitylink.com**")
