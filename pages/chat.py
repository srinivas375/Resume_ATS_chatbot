import templates
import streamlit as st 
from langchain_core.prompts import load_prompt

if "model" in st.session_state:
    print("using the llm model\n")
    print("using the database\n")
    
    
    
else:
    print("need to create the llm model and database")
    
    from llm import model
    from connection import collection
    
    st.session_state.model = model
    st.session_state.collection = collection
    
    
prompt = st.text_input("Enter your prompt here")

if prompt:
    
    template_1 = load_prompt("extract_template.json")
    
    chain = template_1 | st.session_state.model
    
    result = chain.invoke({
        "text":prompt
    })
    
    skills = result.content.split(',')
    skills = [skill.strip() for skill in skills]
        
    query = {"technical_skills": {"$all": skills}}
    
    data = st.session_state.collection.find(query)

    text = []
    if data:
        for val in data:
            text.append(val)

    template_2 = load_prompt("process_data_template.json")
    
    process = template_2 | st.session_state.model
    
    final_output = process.invoke({
        "query" : prompt,
        "data" : text
    })
    
    st.write(final_output.content)
        
    
    

    
