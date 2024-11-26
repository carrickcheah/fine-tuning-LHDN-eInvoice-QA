import json
from openai import OpenAI
import os
import pandas as pd
from pprint import pprint

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    project=os.environ.get("project id")
)

def main():
    # Read dataset
    recipe_df = pd.read_csv("src/data/cookbook_recipes_nlg_10k.csv")
    print(recipe_df.head())  # Display the first few rows of the dataset

# Entry point
if __name__ == "__main__":
    main()
