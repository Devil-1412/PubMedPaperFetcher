from openai import OpenAI
import json
from typing import List, Dict

API_KEY = "api key for openai"
# Set your OpenAI API key
client = OpenAI(api_key = API_KEY)


def process_query_with_llm(query: str, debug: bool) -> Dict[str, str]:
    """
    Use an LLM to process a natural language query and extract structured search parameters.

    Args:
    - query (str): The natural language query to process.
    - debug (bool): Flag to print debug messages.

    Returns:
    - Dict[str, str]: A dictionary containing the extracted search parameters:
                       'keywords', 'year', and 'affiliation_type'.
    """
    if debug:
        print(f"Processing query with LLM: {query}")

    prompt = f"""
    You are a highly accurate assistant that extracts structured PubMed search parameters from user queries.
    Your output must be in valid JSON format, without extra words or connectors like AND, after, or before.

    Given the following user query, extract the structured parameters:
    - "keywords" should not be a comma-separated string of key terms.
    - "year" should be in the format YYYY.
    - "affiliation" should describe the type of affiliation (e.g., biotech companies).


    Return the structured parameters in the following JSON format:
    {{
        "keywords": "<keywords>",
        "year": "<YYYY>",
        "affiliation_type": "<affiliation>"
    }}
    Following is an example of a valid response:
    {{
        "keywords": "AI in healthcare",
        "year": "2020",
        "affiliation_type": "biotech companies"
    }}
    Your output should be in the same format as example
    """
    if debug:
        print("Sending query to LLM")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ],
        max_tokens=200
    )
    if debug:
        print("LLM response received")

    parameters = response.choices[0].message.content.strip()
    parameters = json.loads(parameters)
    return parameters


def build_pubmed_query(parameters: Dict[str, str], debug: bool) -> str:
    """
    Build a PubMed query string based on the structured parameters.

    Args:
    - parameters (Dict[str, str]): The structured search parameters extracted by the LLM.
    - debug (bool): Flag to print debug messages.

    Returns:
    - str: A string representing the constructed PubMed query.
    """
    if debug:
        print("Building PubMed query")

    # Extract the structured parameters
    keywords = parameters.get("keywords", "")
    year = parameters.get("year", "")
    affiliation_type = parameters.get("affiliation_type", "")

    # Construct the PubMed query string
    query = f"{keywords} AND {year}"

    # Add affiliation type if specified
    if affiliation_type:
        query += f" AND {affiliation_type}"

    if debug:
        print(f"Constructed PubMed query: {query}")

    return query