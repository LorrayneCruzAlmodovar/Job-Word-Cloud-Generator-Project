from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  # Generate word clouds
from PIL import Image  # Load images
import numpy as np  # Convert images to numbers
import re  # clean the user_text_put and remove none words char
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter  # Count the frequency of distinct strings

# Streamlit syntax ro create title, subtitle and text_input
st.title("Job Word  Cloud Generator Project")  # set the title
st.subheader("Copy and paste your job description in the box'")  # set the sub header
text_input = st.text_input(" ").lower()  # get user input as string and turn it all lowercase

# create text input field and display it on sidebar
background_color = st.sidebar.text_input('Choose background color', value="white")

# Create number input field and display it on sidebar
height = int(st.sidebar.number_input('Choose height between 500 - 1000 pixels',
                                     value=640))
width = int(st.sidebar.number_input('Choose width between 500 - 1000 pixels',
                                    value=800))
# Create select box widget on the sidebar
shape = st.sidebar.selectbox("Select the shape", ("Rectangle", "Heart", "Star"))


# st.markdown(text_input)

# Create a function to remove none words in the job description
def text():
    pattern = r'\W+'  # return only words with in text
    # Split the text into a list of individual words
    word = re.split(pattern, text_input)
    return word


# join text with space
words = " ".join(text())

# Create a wordcloud generator
try:
    if shape == "Heart":
        image = Image.open("heart.jpeg")  # Load the image from a file

        mask = np.array(image)  # Convert the image to a numeric representation

        # Create a wordcloud generator using Heart shape
        wordcloud = WordCloud(mask=mask, background_color=background_color).generate(words)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud)
        plt.xticks([]) # hide y tick marks from the graph
        plt.yticks([]) # hide y tick marks from the graph
        # plt.axis('off')
        st.pyplot(fig)
        # st.set_option('deprecation.showPyplotGlobalUse', False)
    elif shape == "Star":
        image = Image.open("Star.jpeg")  # Load the image from a file
        mask = np.array(image)  # Convert the image to a numeric representation

        # Create a wordcloud generator using Star shape
        wordcloud = WordCloud(mask=mask, stopwords=STOPWORDS, background_color=background_color).generate(words)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud)
        plt.xticks([])
        plt.yticks([])
        # plt.axis('off')
        st.pyplot(fig)
        # st.set_option('deprecation.showPyplotGlobalUse', False)
    else:

        # Create a wordcloud generator with defaults default arguments
        wordcloud = WordCloud(stopwords=STOPWORDS, background_color=background_color,
                              height=height, width=width).generate(words)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud)
        plt.xticks([])
        plt.yticks([])
        # plt.axis('off')
        st.pyplot(fig)
except ValueError:
    st.markdown("### Please insert your job description in the text box")
st.markdown(words)
