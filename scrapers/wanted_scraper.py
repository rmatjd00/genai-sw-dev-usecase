import requests
from bs4 import BeautifulSoup
import time
import json

class WantedScraper:
    def __init__(self):
        self.base_url = "https://www.wanted.co.kr"
        self.api_url = "https://www.wanted.co.kr/api/v4/jobs"
        # Search queries based on user request
        self.search_keywords = ['Robotics Business Development', 'IT Project Manager']

    def fetch_jobs(self, limit=10):
        """
        Fetches job postings from Wanted.co.kr
        Note: Wanted uses an API for their frontend, which is easier to scrape than HTML.
        """
        all_jobs = []
        
        for keyword in self.search_keywords:
            print(f"Searching for: {keyword}")
            # This is a simplified representation of the Wanted API call
            # In a real scenario, you might need to handle pagination, tags, etc.
            params = {
                'country': 'kr',
                'tag_type_ids': '', 
                'job_sort': 'company.response_rate_order',
                'locations': 'all',
                'years': '-1', # All experience levels
                'limit': limit,
                'query': keyword
            }
            
            try:
                response = requests.get(self.api_url, params=params, timeout=30)
                if response.status_code == 200:
                    data = response.json()
                    jobs = data.get('data', [])
                    for job in jobs:
                        job_details = self.get_job_details(job['id'])
                        if job_details:
                            all_jobs.append(job_details)
                else:
                    print(f"Failed to fetch jobs for {keyword}: {response.status_code}")
            except Exception as e:
                print(f"Error fetching jobs for {keyword}: {e}")
                
            time.sleep(1) # Be polite
            
        return all_jobs

    def get_job_details(self, job_id):
        """
        Fetches detailed information for a specific job ID
        """
        url = f"{self.api_url}/{job_id}"
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                data = response.json()
                job = data.get('job', {})
                company = job.get('company', {})
                
                return {
                    'id': job.get('id'),
                    'title': job.get('position'),
                    'company': company.get('name'),
                    'company_industry': company.get('industry_name'),
                    'description': job.get('detail', {}).get('intro'),
                    'requirements': job.get('detail', {}).get('requirements'),
                    'preferred': job.get('detail', {}).get('preferred_points'),
                    'main_tasks': job.get('detail', {}).get('main_tasks'),
                    'link': f"{self.base_url}/wd/{job_id}",
                    'platform': 'Wanted'
                }
        except Exception as e:
            print(f"Error fetching details for job {job_id}: {e}")
        return None

if __name__ == "__main__":
    scraper = WantedScraper()
    jobs = scraper.fetch_jobs(limit=2)
    print(json.dumps(jobs, indent=2, ensure_ascii=False))
