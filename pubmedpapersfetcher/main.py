from pubmedpapersfetcher.pubmed_fetcher import search_pubmed, fetch_paper_details, save_to_csv
from pubmedpapersfetcher.llm_query_processor import process_query_with_llm, build_pubmed_query
import click
from typing import Optional


@click.command()
@click.argument('query')
@click.option('-f', '--file', help="Output file name to save results. If not provided, results will be printed to the console.")
@click.option('-d', '--debug', is_flag=True, help="Print debug information during execution.")
def get_papers_list(query: str, debug: bool, file: Optional[str]):
    """
    Main function to fetch PubMed papers based on a natural language query and output results.

    Args:
    - query (str): The natural language query to search PubMed.
    - debug (bool): Flag to print debug information during execution.
    - file (Optional[str]): The file name to save results to. If None, results will be printed to the console.

    Function Flow:
    - Processes the query using an LLM to extract structured search parameters.
    - Builds a PubMed query based on these parameters.
    - Fetches PubMed IDs and details for each paper.
    - Saves the result to a CSV or prints the details to the console.
    """
    # Search and fetch papers based on user query
    llm_query = process_query_with_llm(query, debug)
    pubmed_query = build_pubmed_query(llm_query, debug)
    pubmed_ids = search_pubmed(pubmed_query, debug)
    papers = fetch_paper_details(pubmed_ids, debug)

    # Output results: Save to file or print to console
    if file:
        # Save the papers data to a CSV file
        save_to_csv(papers, file, debug)
    else:
        # Print paper details to console
        for paper in papers:
            print(paper)


if __name__ == "__main__":
    get_papers_list(query, debug, file)
