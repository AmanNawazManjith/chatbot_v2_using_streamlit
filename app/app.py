import streamlit as st
import numpy as np
import pandas as pd

st.title('Greetings from COVIDBOT.')
exit_list = ['exit', 'see you later', 'bye', 'quit', 'break', 'sayonara','stop']
from response import greeting_response,bot_response

def main():
    st.subheader("Ask COVID anything related to the covid virus!")
    
    

    col1, col2 = st.columns(2)

    with col1:
        user_input = st.text_input('Enter your query',value='Hey')
        st.write('You have typed:', user_input)

    with col2:
        st.image('images/covid-Bot.gif')


    
    while True:
        if user_input.lower() in exit_list:
            st.subheader('COVID Bot: Had a good time, will chat with you later !')
            break
        else:
            if greeting_response(user_input) != None:
                st.subheader('COVID Bot:' +' '+greeting_response(user_input))
                break
            else:
                st.subheader('COVID Bot:' +' '+bot_response(user_input))
                break
    # while True:
    #     user_input = st.text("Enter your query")
    #     if user_input.lower()in exit_list:
    #         st.subheader('COVID Bot: Had a good time, will chat with you later !')
    #         break
    #     else:
    #         if greeting_response(user_input) != None:
    #             st.subheader('COVID Bot:' +' '+greeting_response(user_input))
    #         else:
    #             st.subheader('COVID Bot:' +' '+bot_response(user_input))


if __name__ == '__main__':
    main()
    