# Career Sentinel Automation System

This project is an automated system designed to scrape job postings, analyze them using AI, and provide market intelligence for "Robotics Business Development" and "IT Project Manager" roles.

## Project Structure

- `scrapers/`: Contains scripts to scrape job postings.
  - `wanted_scraper.py`: Scrapes job postings from Wanted.co.kr.
- `analyzer/`: Contains AI logic for analyzing job postings.
  - `gemini_analyzer.py`: Uses Google Gemini API to analyze jobs based on a specific user profile.
- `market_intelligence/`: Scripts for curating market trends.
  - `trend_curator.py`: Curates latest trends from Robotics/IT news sources.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up Environment Variables:
   - `GEMINI_API_KEY`: Your Google Gemini API Key.

## Usage

### Job Scraping
Run the Wanted scraper to fetch latest jobs:
```bash
python scrapers/wanted_scraper.py
```

### AI Analysis
The analyzer module can be imported and used to generate reports for scraped jobs.
```python
from analyzer.gemini_analyzer import CareerSentinelAnalyzer
analyzer = CareerSentinelAnalyzer()
report = analyzer.analyze_job(job_data)
print(report)
```

### Market Intelligence
Generate a digest of latest trends:
```bash
python market_intelligence/trend_curator.py
```

## User Profile (Hardcoded for Analysis)
- 6 months of IT Business Development Intern experience.
- 3 months of Marketing Intern experience.
- Native-level English (Top-tier TOEIC/OPIc).
