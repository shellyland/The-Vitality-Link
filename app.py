# Tabs layout — Main sections
main_tabs = st.tabs(["Our Roots", "Welcome", "Tiers", "Honoree Form"])

# --- OUR ROOTS TAB ---
with main_tabs[0]:
    st.markdown("## Our Roots")
    st.markdown("""
At **The Vitality Link**, we don’t just serve — we honor.

Life’s rhythm is similar to a tree’s seasonal changes. Just as trees adapt and flourish through each cycle, we too can thrive as we navigate transitions. This principle shapes our core values:

- **Growth** — Leaves represent regeneration and renewal.
- **Connection** — Branches symbolize a trusted network of supportive resources.
- **Resilience** — Roots embody the lasting legacy of our founder’s grandparents. Caring for them in their later years was a full-circle privilege — and that experience became the foundation of our mission.
""")

# --- WELCOME TAB ---
with main_tabs[1]:
    st.markdown("### Welcome to The Vitality Link!")
    st.markdown("""
We're your personal concierge. If you're here, you value a higher quality of life — and we can help. 

We call our clients **Honorees** because you are more than just a client — you are valued, celebrated, and worthy of seamless support. 

Whether you need a hand with errands, non-medical transportation, wellness check-ins, digital support, or social enrichment — we’ll guide you every step of the way.
""")

# --- TIERS TAB WITH SUBTABS ---
with main_tabs[2]:
    st.markdown("## Concierge Service Tiers")
    tier_tabs = st.tabs(["Bronze", "Silver", "Gold", "Platinum"])

    with tier_tabs[0]:
        st.markdown("### Bronze Package")
        st.markdown("""
- Local transportation assistance (non-medical)  
- Errand running  
- Wellness check-in (phone call or virtual)  
""")

    with tier_tabs[1]:
        st.markdown("### Silver Package")
        st.markdown("""
- All Bronze services  
- Companionship during local outings (appointments, shopping, etc.)  
- Assistance with scheduling appointments  
""")

    with tier_tabs[2]:
        st.markdown("### Gold Package")
        st.markdown("""
- All Silver services  
- Event planning and coordination for honorees (birthday, social, etc.)  
- Dedicated personal concierge for priority scheduling  
""")

    with tier_tabs[3]:
        st.markdown("### Platinum Package")
        st.markdown("""
- All Gold services  
- Custom wellness experience (personalized outings, special requests)  
- Full priority access with on-demand concierge support  
""")

# --- HONOREE FORM TAB ---
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
        services_interested = st.multiselect(
            "Which services are you interested in?",
            ["Errand Assistance", "Appointment Transportation", "Wellness & Independence Support", "Technology Assistance", 
             "Community-Based Social Engagement", "Fitness & Wellness", "Financial Literacy Education", "Sexual Health Awareness"]
        )
        submit = st.form_submit_button("Submit")

    if submit:
        st.success(f"Thank you, {full_name}! We will follow up at {email}.")
        st.info("Your journey to a fulfilling and intuitive experience begins now.")
