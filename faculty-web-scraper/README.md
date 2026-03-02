# TTDS Assignment 1 — Faculty Web Scraper

A web scraper that extracts faculty information (name, designation, email, research interests) from a university Faculty of IT & Computer Science website and exports the data to CSV.

## Tech Stack

- **Python** — requests, BeautifulSoup4, pandas

## Project Structure

```
├── scrapper.py        # Web scraper — fetches and parses faculty profiles
├── faculty_info.csv   # Scraped output data
└── documentation.docx # Assignment documentation
```

## How It Works

1. Fetches the faculty listing page from the university website
2. Finds all `<h4>` tags with faculty designations (Professor, Associate/Assistant Professor)
3. For each relevant faculty member, visits their profile page
4. Extracts name, designation, email, and research interests
5. Saves all data to `faculty_info.csv`

## Running

```bash
pip install requests beautifulsoup4 pandas
python scrapper.py
```
