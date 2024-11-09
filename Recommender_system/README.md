
# Doctor Recommendation System Based on Symptoms

## Overview

This recommender system involves a medical chatbot system (preceding steps) that interacts with patients to understand their symptoms and recommend a suitable doctor. The goal is to suggest doctors based on the patient's symptoms, pre-existing conditions, and the specialist type recommended by the chatbot. The system utilizes natural language processing (NLP) techniques to find similar symptoms from past patients and recommends the top doctors based on patient feedback and ratings.

## Data

The provided dataset (`Final_data.csv`) contains the following columns:

- **Patient ID**: A unique identifier for each patient.
- **Symptoms**: A list of symptoms reported by the patient.
- **Specialist Type**: The type of medical specialist the patient was referred to (e.g., Cardiologist, Dermatologist).
- **Rating**: A rating (1-5) given to the doctor by the patient.
- **Age**: The age of the patient.
- **Gender**: The gender of the patient.
- **Pre-existing Conditions**: Any pre-existing medical conditions the patient has (e.g., Asthma, Diabetes).
- **Doctor Name**: The name of the doctor who treated the patient.
- **Doctor ID**: A unique identifier for each doctor.

## Code Functionality

The code provided in the Jupyter notebook (`Recommendation_based_on_symptoms.ipynb`) performs the following tasks:

1. **Symptom Matching**: The system inputs new symptoms and filters the data to find similar cases from the dataset.
2. **Doctor Recommendation**: It ranks doctors based on patient feedback, focusing on matching symptoms, pre-existing conditions, and specialist type.
3. **Natural Language Processing (NLP)**: NLP techniques are used to match the new patient's symptoms with stored symptoms to recommend the most suitable doctors.
4. **Recommendation Output**: The system outputs a list of doctors along with their average rating and the number of patients they have treated for similar conditions.

## Usage

1. **Data Preparation**: Load the dataset and preprocess it.
2. **Symptom Input**: Provide the patient's symptoms and pre-existing conditions.
3. **Recommendation**: The system returns a ranked list of doctors who have treated similar cases, along with their ratings and details.
