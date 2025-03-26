import os

def save(uploaded_file):
    uploaded_path = "resume"
    os.makedirs(uploaded_path, exist_ok=True)
    
    file_path = os.path.join(uploaded_path, uploaded_file.name)
    
    with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    
    return file_path