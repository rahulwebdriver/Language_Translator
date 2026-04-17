from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("Rahul's GPT")
user_language=st.selectbox(label='Choose the language for the output: ',
             options=['English','Hindi','German','French','Sanskrit','Italian','Gujarati'])

User_text=st.text_input('Enter your text here')


model=ChatGroq(model="llama-3.3-70b-versatile",temperature=0)

#Template
prompt=PromptTemplate(template="Give the deatils of following text into {language}:{text}",
                      input_variables=["language", "text"] )



if st.button('Submit'):
    if User_text.strip() == "":
        st.warning("Please enter some text")

    final_prompt=prompt.format(language=user_language,
                               text=User_text)
    result=model.invoke(final_prompt)
    st.write(result.content)






