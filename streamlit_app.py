
import streamlit
streamlit.title('Hello Kamal')
streamlit.header('Its a sunny day')
streamlit.text('come here')
streamlit.text('can you ellaborate that')


import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
