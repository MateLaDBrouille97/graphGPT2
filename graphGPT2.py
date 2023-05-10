import os
import streamlit as st
import pandas as pd
from langchain.llms import OpenAI
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


with st.sidebar:
  st.header("CSV")
  csv = st.file_uploader("Upload your CSV", type=['csv'])

    
  st.header("API KEY")
  openaikey = st.text_input("Your openai key", value="", type="password",placeholder="openai key")



st.markdown(f"""
    ## \U0001F60A! Question Answering with your CSV file
    1) Upload a CSV. 
    2) Enter OpenAI API key. This costs $. Set up billing at [OpenAI](https://platform.openai.com/account).
    3) Type a question and Press 'Run'.
    4) You can plot your data with the good prompt🎈 """)

st.header("Ask your CSV 💬")

user_question = st.text_input("Ask a question about your CSV:")


def qg(csv_reader2,user_question):
    if openaikey is not None:
          os.environ["OPENAI_API_KEY"] = openaikey
    if csv is not None:
          prompt_text = user_question
          if prompt_text:
             llm = OpenAI()
             pandas_ai = PandasAI(llm)
             result=pandas_ai.run(csv_reader2, prompt=prompt_text)
             
    return (result)


def main():
    
   if csv:
      csv_reader2 = pd.read_csv(csv)
      csv_reader2.columns = csv_reader2.columns.str.strip()
      with st.expander('Dataframe'):
           st.subheader(csv.name)
           st.dataframe(csv_reader2)
      
   if st.button("Run", type="primary"):   
    if user_question:
      result=qg(csv_reader2=csv_reader2,user_question=user_question)
      st.write(result)
      st.set_option('deprecation.showPyplotGlobalUse', False)
      st.pyplot(print(result))
          

    
if __name__ == '__main__':
    main()
  