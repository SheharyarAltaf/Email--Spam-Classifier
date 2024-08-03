# Email Spam Classifier

## Overview

This project implements an email spam classifier using machine learning. The application provides a user-friendly interface to input email text and predict whether the email is spam or not.

## Features

- **Text Preprocessing**: Cleans and transforms the input email text by converting it to lowercase, removing punctuation and stop words, and applying stemming.<br>
- **Spam Classification**: Utilizes a machine learning model to classify the input email.<br>
- **Streamlit Interface**: Simple web interface for user interaction.<br>

## Technologies Used

- **Python**: Programming language for implementation.
  ![Python](https://www.python.org/community/logos/python-logo-master-v3-TM.png)

- **Streamlit**: Framework for building the web application interface.
  ![Streamlit](https://streamlit.io/images/brand/streamlit-logo-primary-colour.svg)

- **NLTK**: Library for natural language processing tasks.
  ![NLTK](https://www.nltk.org/_images/nltk_logo.png)

- **Pickle**: Used for loading pre-trained models and vectorizers.
  ![Pickle](https://docs.python.org/3/_images/pickle.svg)

## Installation

To run this project, you need to install the required libraries. Run the following command:

```bash
pip install streamlit pandas numpy scikit-learn nltk
