import streamlit as st
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.executor import AgentExecutor
from src.agents.memory_manager import MemoryManager

# Page configuration
st.set_page_config(
    page_title="Healthcare Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "session_id" not in st.session_state:
    memory_manager = MemoryManager()
    st.session_state.session_id = memory_manager.create_session()

if "executor" not in st.session_state:
    st.session_state.executor = AgentExecutor()

# Custom CSS
st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            color: #0066cc;
            text-align: center;
            margin-bottom: 2rem;
        }
        .card {
            background-color: #f0f2f6;
            padding: 1.5rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        .success {
            background-color: #d1e7dd;
            color: #0f5132;
            padding: 1rem;
            border-radius: 0.5rem;
        }
        .error {
            background-color: #f8d7da;
            color: #842029;
            padding: 1rem;
            border-radius: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("🏥 Healthcare Assistant")
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ["Home", "Patient Dashboard", "Appointments", "Medical Records", "Analytics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown(f"**Session ID:** `{st.session_state.session_id[:8]}...`")

# Main Content
if page == "Home":
    st.markdown("<h1 class='main-header'>🏥 Healthcare Assistant</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("📅 **Appointment Booking**\nSchedule appointments with specialists")
    
    with col2:
        st.info("📋 **Medical Records**\nManage and retrieve patient history")
    
    with col3:
        st.info("🔍 **Medical Search**\nFind latest treatment information")
    
    st.markdown("---")
    
    st.subheader("🎯 Ask Your Healthcare Assistant")
    
    user_query = st.text_area(
        "Enter your medical query or appointment request:",
        placeholder="E.g., 'Book an appointment with a nephrologist for kidney disease treatment'",
        height=100
    )
    
    if st.button("🚀 Process Request", use_container_width=True):
        if user_query:
            with st.spinner("Processing your request..."):
                try:
                    result = st.session_state.executor.execute_plan(
                        user_query=user_query,
                        session_id=st.session_state.session_id
                    )
                    
                    if result.get("success"):
                        st.markdown('<div class="success">✅ Request processed successfully!</div>', unsafe_allow_html=True)
                        
                        st.subheader("📊 Execution Plan")
                        plan = result.get("plan", {})
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write("**Goals:**")
                            for goal in plan.get("goals", []):
                                st.write(f"• {goal}")
                        
                        with col2:
                            st.write("**Tools Used:**")
                            for tool in plan.get("tools_needed", []):
                                st.write(f"• {tool}")
                        
                        st.subheader("📋 Results")
                        for subtask, res in result.get("results", {}).items():
                            with st.expander(f"📌 {subtask}"):
                                st.json(res)
                    else:
                        st.markdown(f'<div class="error">❌ Error: {result.get("error")}</div>', unsafe_allow_html=True)
                
                except Exception as e:
                    st.markdown(f'<div class="error">❌ Error: {str(e)}</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a query")

elif page == "Patient Dashboard":
    st.subheader("👤 Patient Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Age", "70")
    with col2:
        st.metric("Blood Type", "O+")
    with col3:
        st.metric("Appointments", "2")
    
    st.markdown("---")
    
    st.subheader("📅 Upcoming Appointments")
    appointments_data = {
        "Date": ["2024-01-15", "2024-01-20"],
        "Doctor": ["Dr. Smith", "Dr. Johnson"],
        "Specialty": ["Nephrology", "Cardiology"],
        "Status": ["Scheduled", "Scheduled"]
    }
    st.dataframe(appointments_data, use_container_width=True)

elif page == "Appointments":
    st.subheader("📅 Appointment Management")
    
    tab1, tab2, tab3 = st.tabs(["Book Appointment", "View Appointments", "Cancel Appointment"])
    
    with tab1:
        st.write("**Book New Appointment**")
        
        col1, col2 = st.columns(2)
        with col1:
            patient_name = st.text_input("Patient Name")
            specialty = st.selectbox("Specialty", ["Nephrology", "Cardiology", "Neurology", "Oncology"])
        
        with col2:
            doctor = st.selectbox("Doctor", ["Dr. Smith", "Dr. Johnson", "Dr. Brown"])
            appointment_date = st.date_input("Appointment Date")
        
        if st.button("Book Appointment", use_container_width=True):
            st.success(f"✅ Appointment booked for {patient_name} with {doctor} on {appointment_date}")
    
    with tab2:
        st.write("**Your Appointments**")
        appointments_data = {
            "ID": ["AP001", "AP002"],
            "Doctor": ["Dr. Smith", "Dr. Johnson"],
            "Date": ["2024-01-15", "2024-01-20"],
            "Status": ["Scheduled", "Scheduled"]
        }
        st.dataframe(appointments_data, use_container_width=True)
    
    with tab3:
        st.write("**Cancel Appointment**")
        appointment_id = st.selectbox("Select Appointment", ["AP001", "AP002"])
        if st.button("Cancel", use_container_width=True):
            st.warning(f"Appointment {appointment_id} has been cancelled")

elif page == "Medical Records":
    st.subheader("📋 Medical Records Management")
    
    tab1, tab2, tab3 = st.tabs(["View Records", "Add Record", "Summarize"])
    
    with tab1:
        st.write("**Patient Medical Records**")
        records_data = {
            "Date": ["2024-01-10", "2024-01-05", "2023-12-28"],
            "Diagnosis": ["Chronic Kidney Disease", "Hypertension", "Diabetes"],
            "Treatment": ["Dialysis", "Medication", "Insulin"],
            "Doctor": ["Dr. Smith", "Dr. Brown", "Dr. Wilson"]
        }
        st.dataframe(records_data, use_container_width=True)
    
    with tab2:
        st.write("**Add Medical Record**")
        
        col1, col2 = st.columns(2)
        with col1:
            diagnosis = st.text_input("Diagnosis")
            treatment = st.text_input("Treatment")
        
        with col2:
            medications = st.text_area("Medications (comma-separated)")
            notes = st.text_area("Additional Notes")
        
        if st.button("Save Record", use_container_width=True):
            st.success("✅ Medical record saved successfully")
    
    with tab3:
        st.write("**Medical History Summary**")
        if st.button("Generate Summary"):
            st.info("Patient has history of chronic kidney disease and hypertension. Currently on dialysis and medication management.")

elif page == "Analytics":
    st.subheader("📊 Analytics & Monitoring")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Patients", "1,243", "+5.2%")
    
    with col2:
        st.metric("Appointments Scheduled", "342", "+12.1%")
    
    with col3:
        st.metric("Success Rate", "94.2%", "+2.1%")
    
    with col4:
        st.metric("Avg Response Time", "2.3s", "-0.5s")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.8rem;'>
        🏥 Healthcare Assistant v1.0 | Built with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)
