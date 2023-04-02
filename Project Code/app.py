import streamlit as st
import pandas as pd
from MyPackage import major_project_ranking
import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

def main(): 
    global tweet
    st.title("Ranking of disaster related hashtags (from twitter) using ML and NLP.")
    menu = ["Home", "Visualise", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    tweet=''

    if choice == "Home":
        st.subheader("Enter the tweet")

        with st.form(key='form'):
            tweet = st.text_input("Enter the tweet")

            submit = st.form_submit_button(label = 'Rank')

            if submit and tweet == "":
                st.error("Tweet cant be empty")
            elif(submit and tweet != ""):
                st.dataframe(major_project_ranking.ranking(tweet))
    
    elif choice == "Visualise":
        st.subheader("Visualising the sentiment analysis of tweets")
        st.pyplot(major_project_ranking.graph())

    else:
        st.subheader("About")
        st.text("This is a web application created using streamlit.\nIt displays the ranked tweets based on their similarity according to the tweet entered\nby the user.")

if __name__ == '__main__':
    main()