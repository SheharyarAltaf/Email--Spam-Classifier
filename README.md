# Email Spam Classifier

## Overview

This project implements an email spam classifier using machine learning. The application provides a user-friendly interface to input email text and predict whether the email is spam or not.

## Features

- **Text Preprocessing**: Cleans and transforms the input email text by converting it to lowercase, removing punctuation and stop words, and applying stemming.
- **Spam Classification**: Utilizes a machine learning model to classify the input email.
- **Streamlit Interface**: Simple web interface for user interaction.

## Technologies Used

- **Python**: Programming language for implementation.
  ![Python](https://img.shields.io/badge/Python-306998?style=for-the-badge&logo=python&logoColor=white&color=306998)

- **Streamlit**: Framework for building the web application interface.
  ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4F?style=for-the-badge&logo=streamlit&logoColor=white&color=FF4B4F)

- **NLTK**: Library for natural language processing tasks.
  ![NLTK](https://img.shields.io/badge/NLTK-3F6C6B?style=for-the-badge&logo=nltk&logoColor=white&color=3F6C6B)

- **Pickle**: Used for loading pre-trained models and vectorizers.
  ![Pickle](https://img.shields.io/badge/Pickle-FFA500?style=for-the-badge&logo=python&logoColor=white&color=FFA500)

## Installation

To run this project, you need to install the required libraries. Run the following command:

```bash
pip install streamlit pandas numpy scikit-learn nltk
