from pubmedpapersfetcher.pubmed_fetcher import search_pubmed, fetch_paper_details, save_to_csv
from pubmedpapersfetcher.llm_query_processor import process_query_with_llm, build_pubmed_query
import click


@click.command()
@click.argument('query')
@click.option('-f', '--file', help="Output file name to save results. If not provided, results will be printed to the console.")
@click.option('-d', '--debug', is_flag=True, help="Print debug information during execution.")
def get_papers_list(query, debug, file):

    # Search and fetch papers
    llm_query = process_query_with_llm(query, debug)
    pubmed_query = build_pubmed_query(llm_query, debug)
    pubmed_ids = search_pubmed(pubmed_query, debug)
    papers = fetch_paper_details(pubmed_ids, debug)

    if file:
        # Save to CSV
        save_to_csv(papers, file, debug)
    else:
        # Print to console
        for paper in papers:
            print(paper)


if __name__ == "__main__":
    get_papers_list(query, debug, file)
