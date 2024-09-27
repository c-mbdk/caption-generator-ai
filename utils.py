from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

def generate_caption(theme):
    llm = ChatGroq(temperature=0.6, model_name="mixtral-8x7b-32768")

    prompt_template_caption = PromptTemplate(
        input_variables='theme',
        template='I want to post a thoughtful caption with my picture on Instagram on the theme of {theme}. Please suggest some quotes that I can use for my caption.'
    )

    chain = LLMChain(llm=llm, 
                     prompt=prompt_template_caption
    )
    caption = chain.run(theme)

    return {
        'theme': theme,
        'caption': caption
    }

# Styling functions
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


if __name__ == '__main__':
    print(generate_caption('Power'))