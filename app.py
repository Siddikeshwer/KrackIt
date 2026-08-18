import streamlit as st

from parsers.pdf_parser import extract_pdf_text
from parsers.docx_parser import extract_docx_text

from agents.resume_analyzer import analyze_resume
from agents.job_analyzer import analyze_job_description
from agents.interview_agent import generate_interview_questions
from agents.application_agent import generate_application_package


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="KrackIt - AI Job Cracker",
    page_icon="🚀",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚀 KrackIt")
st.subheader("AI Job Cracker")

st.write(
    "Upload your resume, provide the target job details, "
    "and let KrackIt prepare you for the application and interview."
)

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.header("🎯 Target Job")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input(
        "Company Name",
        placeholder="e.g. Google"
    )

with col2:
    role = st.text_input(
        "Job Role",
        placeholder="e.g. Software Engineer"
    )


job_description = st.text_area(
    "Job Description",
    height=250,
    placeholder="Paste the complete job description here..."
)


st.header("📄 Resume")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)


# --------------------------------------------------
# RESUME EXTRACTION
# --------------------------------------------------

resume_text = None

if uploaded_file:

    try:

        if uploaded_file.name.lower().endswith(".pdf"):
            resume_text = extract_pdf_text(uploaded_file)

        elif uploaded_file.name.lower().endswith(".docx"):
            resume_text = extract_docx_text(uploaded_file)

        if resume_text:

            with st.expander("👀 View Extracted Resume Text"):
                st.text(resume_text)

            st.success("Resume successfully extracted.")

        else:
            st.error("Could not extract text from the resume.")

    except Exception as e:
        st.error(f"Error reading resume: {e}")


# --------------------------------------------------
# MAIN BUTTON
# --------------------------------------------------

st.divider()

crack_button = st.button(
    "🚀 CRACK THIS JOB",
    type="primary",
    use_container_width=True
)


# --------------------------------------------------
# VALIDATION
# --------------------------------------------------

if crack_button:

    if not company:
        st.error("Please enter the company name.")
        st.stop()

    if not role:
        st.error("Please enter the job role.")
        st.stop()

    if not job_description:
        st.error("Please paste the job description.")
        st.stop()

    if not resume_text:
        st.error("Please upload a valid resume.")
        st.stop()


    # --------------------------------------------------
    # AI ANALYSIS
    # --------------------------------------------------

    st.divider()

    st.header("🔥 KrackIt Analysis")

    # Job analysis
    with st.spinner("Analyzing job description..."):

        try:
            job_analysis = analyze_job_description(
                company,
                role,
                job_description
            )
        except Exception as e:
            st.error(f"Job analysis failed: {e}")
            st.stop()


    # Resume analysis
    with st.spinner("Comparing your resume with the job..."):

        try:
            resume_analysis = analyze_resume(
                resume_text,
                company,
                role,
                job_description
            )
        except Exception as e:
            st.error(f"Resume analysis failed: {e}")
            st.stop()


    # Interview preparation
    with st.spinner("Generating interview questions..."):

        try:
            interview_questions = generate_interview_questions(
                resume_text,
                company,
                role,
                job_description
            )
        except Exception as e:
            st.error(f"Interview generation failed: {e}")
            st.stop()


    # Application package
    with st.spinner("Creating your application package..."):

        try:
            application_package = generate_application_package(
                resume_text,
                company,
                role,
                job_description
            )
        except Exception as e:
            st.error(f"Application generation failed: {e}")
            st.stop()


    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🎯 Job Analysis",
            "📄 Resume Analysis",
            "🎤 Interview Prep",
            "📧 Emails & Cover Letters"
        ]
    )


    with tab1:

        st.markdown(job_analysis)


    with tab2:

        st.markdown(resume_analysis)


    with tab3:

        st.markdown(interview_questions)


    with tab4:

        st.markdown(application_package)


    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------

    st.divider()

    st.caption(
        "KrackIt analyzes the information you provide. "
        "It does not guarantee employment or interview selection."
    )