from langchain_core.prompts import PromptTemplate


extract_template = PromptTemplate(
    template="""
    Extract only the technical skills from the given text and return them as a comma-separated list.
    
    - If there is only one skill, return just that word.
    - The extracted skills must be in lowercase.
    - Standardize the skills to their correct technology terms (e.g., "reactjs" instead of "react js" or "react").
    - If any spelling mistakes exist, correct them to the proper technical term.

    Input text: {text}
    """,
    input_variables=["text"]
)



process_data_template = PromptTemplate(
    template = """
    Below provided text contains the resume details of the persons, that came as output of a query.Generate a nice looking formated breif simple output of the resulted datas according to the related to the given query.Don't give the next chat continued response at the end.
    query : {query}
    resulted_data : {data}
    """,
    input_variables = ["query","resulted_data"]
)


extract_template.save("extract_template.json")
process_data_template.save("process_data_template.json")