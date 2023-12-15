import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from model

def getLlamaresponse(input_text,no_words,blog_style):
    
    ## call the model - llama 2
    llm = CTransformers(
                        model="D:\ML - AI Projects\Blog Generation LLM App\models\llama-2-7b-chat.ggmlv3.q6_K.bin",
                        model_type="llama",
                        config={'max_new_tokens':256, 'temperature':0.4}
                    )

    ## Prompt template
    
    template="""
        write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_Style","input_text","no_words"],template=template)

    ## Generate response
    
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs", 
                   page_icon="🔗", 
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Gererate Blogs with Llama 2 🔗 ")

input_text = st.text_area("Enter your topic here")

## Creating 2 more columns

col1, col2 = st.columns(2)

with col1:
    no_words=st.text_input("Enter the number of words")
    
with col2:
    blog_style=st.selectbox("Writing the blog for",('Reasearchers','Data Scientists','Common People'), index=0)
    
submit=st.button("Generate Blog")

## Final response

if submit:
    st.write(getLlamaresponse(input_text,no_words,blog_style))
    