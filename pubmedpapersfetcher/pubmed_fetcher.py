import requests
import xmltodict
import pandas as pd
import argparse
import re


# Function to search PubMed database
def search_pubmed(query, debug):
    """
    Search PubMed using the provided query and return a list of PubMed IDs.
    """
    if debug:
        print("Searching PubMed for query")

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 30,
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception("Failed to connect to PubMed API")

    if debug:
        print("Response received from PubMed API")

    data = xmltodict.parse(response.text)
    id_list = data['eSearchResult']['IdList']['Id']

    if debug:
        print(id_list)
    return id_list


# Function to fetch paper details by PubMed IDs
def fetch_paper_details(pubmed_ids, debug):
    """
    Fetch detailed information for each PubMed ID and return a list of papers.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    papers = []
    API_KEY = "6a40318fb31df07dc8b4977917d57b071f08"

    for pubmed_id in pubmed_ids:
        if debug:
            print(f"Fetching details for PubMed ID: {pubmed_id}")

        try:
            params = {
                "db": "pubmed",
                "id": pubmed_id,
                "retmode": "xml",
                "api_key": API_KEY
            }
            response = requests.get(url, params=params)
            response.raise_for_status()

            if debug:
                print(f"Response received from PubMed API for {pubmed_id}")

            paper_data = xmltodict.parse(response.text)['PubmedArticleSet']['PubmedArticle']
            authors, non_academic = extract_authors_info(paper_data, debug)
            if non_academic:
                authors_name = "\n".join(
                    f"{author['name']}"
                    for author in authors
                )
                authors_affiliation = "\n".join(
                    f"{author.get('affiliation', 'N/A')}"
                    for author in authors
                )
                authors_email = "\n".join(
                    f"{author.get('email', 'N/A')}"
                    for author in authors
                )
                pdate = paper_data['MedlineCitation']['Article']['Journal']['JournalIssue']['PubDate']
                paper = {
                    "PubmedID": pubmed_id,
                    "Title": paper_data['MedlineCitation']['Article']['ArticleTitle'],
                    "PublicationDate": f"{pdate.get('Day', "")}/{pdate.get('Month', "")}/{pdate.get('Year')}",
                    "Authors": authors_name,
                    "Affiliation": authors_affiliation,
                    "Email": authors_email
                }
                papers.append(paper)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred for PubMed ID {pubmed_id}: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred for PubMed ID {pubmed_id}: {req_err}")
        except KeyError:
            print(f"PubMed ID {pubmed_id} not found or restricted.")

    if debug:
        print(f"Total papers fetched: {len(papers)}")
    return papers


# Helper function to extract author details
def extract_authors_info(paper_data, debug):
    """
    Extract the authors and their affiliations.
    """
    if debug:
        print("Extracting authors information")

    authors_info = []
    non_academic_keywords = [
        "Pharma", "Biotech", "Therapeutics", "Biosciences", "Inc.", "Ltd", "LLC", "Corp.",
        "Corporation", "AG", "SA", "BV", "Group", "Ventures", "Holdings", "Solutions",
        "Innovations", "Analytics", "Manufacturing", "Diagnostics", "MedTech", "Healthcare"
    ]
    non_academic = False
    try:
        for author in (paper_data['MedlineCitation']['Article']['AuthorList']['Author'] if isinstance(
                paper_data['MedlineCitation']['Article']['AuthorList']['Author'], list) else [
                paper_data['MedlineCitation']['Article']['AuthorList']['Author']]):
            if 'AffiliationInfo' in author:
                affiliations = ", ".join(auth['Affiliation'] for auth in (
                    author['AffiliationInfo'] if isinstance(author['AffiliationInfo'], list) else [
                        author['AffiliationInfo']]))
                if any(keyword.lower() in affiliations.lower() for keyword in non_academic_keywords):
                    non_academic = True
                name = f"{author.get('LastName', '')} {author.get('ForeName', '')}"
                emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', affiliations)
                email_str = ", ".join(emails) if emails else "N/A"
                cleaned_affiliation = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '',affiliations).strip()

            authors_info.append({"name": name, "affiliation": cleaned_affiliation, "email": email_str})

    except Exception as e:
        print(f"Error extracting authors: {e}")
    if debug:
        print("Authors information extracted")
    return authors_info, non_academic


# Function to save papers to a CSV file
def save_to_csv(papers, filename, debug):
    """
    Save the list of papers to a CSV file.
    """
    if debug:
        print("Saving papers to CSV")
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")