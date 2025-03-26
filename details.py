from typing import Optional, List, Dict
from pydantic import BaseModel, Field, EmailStr

class ResumeDetails(BaseModel):
    name: str = Field(description="The full name of the candidate, usually found at the beginning of the resume. Give the output only in lower case")
    
    mobile_number: str = Field(description="The candidate's mobile phone number.")
    
    email: EmailStr = Field(description="The candidate's email address.")
    
    about: Optional[str] = Field(description="A short personal summary or professional overview, typically written as a paragraph in the resume. Give the output only in lower case")
    
    education: List[str] = Field(description="The candidate's educational qualifications, including degrees and institutions. Give the output only in lower case")
    

    technical_skills: List[str] = Field(description="List of technical skills, including programming languages, frameworks, tools, and technologies. Ensure that the output is in lowercase and follows standard technology terms. Correct any spelling errors or variations to their proper names (e.g., 'reactjs' instead of 'react js' or 'react').")

    projects: List[Dict[str, str]] = Field(description="Projects undertaken by the candidate. Includes project titles and brief descriptions. Give the output only in lower case")
    
    soft_skills: Optional[List[str]] = Field(description="List of soft skills, including communication, teamwork, leadership, and achievements. Give the output only in lower case")
    
    experience: Optional[List[str]] = Field(description="Work experience details, including previous job roles, responsibilities, and durations. Give the output only in lower case")
    
    internships: Optional[List[Dict[str, str]]] = Field(description="Details of internships, including organization name, role, and duration. Give the output only in lower case")