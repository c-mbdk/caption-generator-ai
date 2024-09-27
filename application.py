import streamlit as st

from utils import generate_caption, local_css

def main():

       # Settings
       st.set_page_config(layout="wide", page_title='Caption Generator')
       st.title('Caption Generator')

       # Loading css
       local_css("frontend/css/streamlit.css")

       # Selecting a theme
       theme = st.sidebar.selectbox('Select a Theme', (
             'Beauty', 'Love', 'Courage', 'Death', 'Friendship', 'Power', 'Fear', 'Faith', 'Hope', 'Dedication', 
             'Grief', 'Desire', 'Gratitude')
       )

       if theme:
              response = generate_caption(theme)
              st.header(response['theme'])
              st.markdown(response['caption'])

if __name__ == '__main__':
    main()