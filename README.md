# PubMed Paper Fetcher CLI Tool

This is a command-line interface (CLI) tool to fetch research papers from the PubMed database based on user queries. The tool processes natural language queries using an LLM, constructs search parameters, and retrieves relevant papers from PubMed. The results are saved to a CSV file.

---

## 🚀 Features
- Uses PubMed API to search and fetch papers.
- Processes natural language queries using an LLM.
- Identifies papers with non-academic authors affiliated with biotech or pharmaceutical companies.
- Outputs results to a CSV file.
- Includes CLI options for file output and debug mode.

---

## 🧑‍💻 Installation
### Prerequisites
- Python 3.8+
- Poetry
- Git

### Clone the Repository
```bash
git clone https://github.com/Devil-1412/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### Install Dependencies
```bash
poetry install
```

---

## 🔧 Usage
Run the CLI tool using the following command:
```bash
poetry run get-papers-list "Your search query"
```

### CLI Options
| Option          | Description                                   | Example                              |
|-----------------|-----------------------------------------------|--------------------------------------|
| `--file` / `-f` | Specify the filename to save the results.      | `--file results.csv`                 |
| `--debug` / `-d`| Enable debug mode to print extra information. | `--debug`                            |

### Example Commands
```bash
# Basic usage
poetry run get-papers-list "AI in healthcare"

# Save results to a custom CSV file
poetry run get-papers-list "COVID-19 vaccine development" --file custom_results.csv

# Enable debug mode
poetry run get-papers-list "Machine learning in biotech" --debug
```

---

## 📂 Project Structure
```plaintext
PubMedPapersFetcher/
├── pubmedpapersfetcher/         # Main package folder (matches the package name)
│   ├── __init__.py              # Makes it a package
│   ├── main.py                  # CLI entry point
│   ├── pubmed_fetcher.py        # PubMed API interaction module
│   ├── llm_query_processor.py   # LLM processing module
├── pyproject.toml               # Poetry configuration file
├── README.md                    # Project documentation
├── LICENSE.txt                  # License for the code
├── poetry.lock                  # Locks exact versions of dependencies
```

---

## 🗂 How the Code is Organized
- **`pubmedpapersfetcher/`**: Main package containing all core modules of the project.
- **`__init__.py`**: Makes the folder a Python package, allowing imports between modules.
- **`main.py`**: The entry point for the CLI tool that ties everything together and provides the command-line interface.
- **`pubmed_fetcher.py`**: Contains functions to interact with the PubMed API, including search and fetch operations.
- **`llm_query_processor.py`**: Contains the function to process user queries using an LLM and extract structured search parameters.
- **`poetry.lock`**: Locks the exact versions of dependencies to ensure consistency across environments.
- **`pyproject.toml`**: Poetry configuration file that manages dependencies and packaging.
- **`README.md`**: Project documentation, including setup instructions and usage examples.

---

## 🔧 Instructions to Install Dependencies and Execute the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pubmed-paper-fetcher.git
   cd pubmed-paper-fetcher
   ```
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
3. Run the CLI tool:
   ```bash
   poetry run get-papers-list "Your search query"
   ```

---

## 🛠 Tools and Libraries Used
The following tools and libraries were used to build this program:

- **PubMed E-utilities API**: Used to fetch research papers from the PubMed database. Documentation: https://www.ncbi.nlm.nih.gov/books/NBK25499/
- **OpenAI API**: Used to process natural language queries and extract structured search parameters. Documentation: https://platform.openai.com
- **Click**: A Python package for creating CLI applications. Documentation: https://click.palletsprojects.com
- **Poetry**: Used for dependency management and packaging. Documentation: https://python-poetry.org
- **Requests**: A simple HTTP library for Python to make API requests. Documentation: https://docs.python-requests.org
- **xmltodict**: Used to parse XML responses from the PubMed API. Documentation: https://github.com/martinblech/xmltodict
- **Pandas**: Used to save the fetched data to a CSV file. Documentation: https://pandas.pydata.org

---

## ✅ Requirements
- Python 3.8+
- Poetry

---

## 📋 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing
1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

---

## 📧 Contact
For any questions or issues, please contact:
- **Pushpam Agrawal**
- **Email**: pushpam160803@gmail.com
- **GitHub**: [https://github.com/Devil-1412](https://github.com/Devil-1412)

