import streamlit as st

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"  # Default page
if "upload_clicked" not in st.session_state:
    st.session_state.upload_clicked = False
if "upload_done" not in st.session_state:
    st.session_state.upload_done = False  # Track if insertion has been done

st.title("Welcome to ATS Chatbot")

# Create two columns for side-by-side buttons
col1, col2 = st.columns(2)

with col1:
    resume_upload_clicked = st.button("Resume Upload")

with col2:
    start_chat_clicked = st.button("Start chatting")

if resume_upload_clicked:
    st.session_state.upload_clicked = True  # Track button click

if st.session_state.upload_clicked and not st.session_state.upload_done:

    from llm import model
    from connection import collection, DuplicateKeyError
    
    
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file:
        from files_handling import save, os

        
        file_path = save(uploaded_file)

        st.success(f"File saved successfully: {uploaded_file.name}")
        
      
        from langchain_community.document_loaders import PyPDFLoader
        from details import ResumeDetails

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Resume file not found: {file_path}")
        
        loader = PyPDFLoader(file_path)
        docs = loader.load()

        if not docs:
            raise ValueError("No content found in the resume PDF.")

        structured_model = model.with_structured_output(ResumeDetails)
        result = structured_model.invoke(docs[0].page_content)
        dict_result = result.model_dump()

        if not st.session_state.upload_done:  # Prevent duplicate insertion
            
            st.session_state.upload_done = True  # Mark as inserted
            
            try:
                insert_result = collection.insert_one(dict_result)
                print(f"Data inserted into DB with ID: {insert_result.inserted_id}")
            except DuplicateKeyError:
                print("Duplicate document found. Not inserting ...\n")
                
            st.success("Click on the Start chatting button if you want to chat.")
            st.session_state.model = model
            st.session_state.collection = collection
            st.session_state.file_path = file_path
            
if start_chat_clicked:
    st.switch_page("pages/chat.py")
