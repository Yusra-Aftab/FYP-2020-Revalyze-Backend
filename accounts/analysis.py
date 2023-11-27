
# from nltk.tokenize import sent_tokenize
import openai
import pandas as pd
import time
from authentication.settings import API_KEY
from accounts.models import Analysis
from accounts.models import Analysis_Report
from nltk.tokenize import sent_tokenize

openai.api_key =API_KEY

def split_text_into_chunks(file_text, chunk_size):
    words = file_text.split()  # Split the text into words
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    return [' '.join(chunk) for chunk in chunks]

def Moderate(name, prompt):

    Category = []
    Flagged = []
    chunk_size = 200

    chunks = split_text_into_chunks(prompt, chunk_size)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk}\n")

        response = openai.moderations.create(
                input=chunk
            )
            # Accessing the results from the response
        result = response.results[0]

        # Accessing categories and category_scores
        categories = result.categories
        flag = result.flagged

        if flag:
            for category in categories:
                if category[1]:
                    Category.append(category[0])
                    Flagged.append(category[1])

        time.sleep(20)         


    analysis_instance = Analysis(name=name, flag=flag, categories=Category, flagged=Flagged)
    analysis_instance.save()
    print(analysis_instance)

    sentences = sent_tokenize(prompt)
    Report = ""
    Sentiments = []
    for sentence in sentences:

        response = openai.moderations.create(
                input = sentence
            )
            # Accessing the results from the response
        result = response.results[0]

        
        categories = result.categories
        flag = result.flagged

        if flag:
            for category in categories:
                if category[1]:
                    Sentiments.append(category[0])

            Report += f"\nDetected Line: {sentence}\nDetected Categories: {Sentiments}\n"
        
        Sentiments.clear()

        time.sleep(20)


    print(Report)
    report_instance = Analysis_Report(name=name, report=Report)
    report_instance.save()       





