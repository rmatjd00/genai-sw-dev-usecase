import google.generativeai as genai
import os
import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class UserProfile:
    experience_bd: str = "6 months of IT Business Development Intern experience"
    experience_mkt: str = "3 months of Marketing Intern experience"
    language: str = "Native-level English (Top-tier TOEIC/OPIc)"

class CareerSentinelAnalyzer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API Key not found. Please set GEMINI_API_KEY environment variable.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.user_profile = UserProfile()

    def analyze_job(self, job_data: Dict) -> str:
        """
        Analyzes a single job posting and generates a report based on the user's profile.
        """
        
        prompt = self._construct_prompt(job_data)
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error analyzing job: {e}"

    def _construct_prompt(self, job_data: Dict) -> str:
        """
        Constructs the prompt for Gemini based on the system blueprint.
        """
        job_content = f"""
        Job Title: {job_data.get('title')}
        Company: {job_data.get('company')}
        Main Tasks: {job_data.get('main_tasks')}
        Requirements: {job_data.get('requirements')}
        Preferred Points: {job_data.get('preferred')}
        """

        user_context = f"""
        My Profile:
        - {self.user_profile.experience_bd}
        - {self.user_profile.experience_mkt}
        - {self.user_profile.language}
        """

        required_structure = """
        Please analyze the job posting against my profile and provide a report in the following STRICT format:

        1. Job Summary: Max 3 sentences.
        2. Success Strategy: Strengths, Weaknesses, and Focus Points based on my profile.
        3. ATS & Interview: Top 5 keywords for the resume + 1 predicted Interview Q&A.
        4. Company Info: Recent news snapshot (simulate or retrieve based on company name knowledge) + 1 English Resume Bullet Point for this specific role.
        """

        return f"""
        You are the 'Career Sentinel' AI.
        
        Target Job:
        {job_content}

        {user_context}

        {required_structure}
        """

if __name__ == "__main__":
    # Mock usage
    analyzer = CareerSentinelAnalyzer(api_key="DUMMY_KEY_FOR_TESTING")
    
    mock_job = {
        "title": "Robotics Business Development Manager",
        "company": "Future Robotics",
        "main_tasks": "Expand market share in SE Asia...",
        "requirements": "3+ years exp, English fluency...",
        "preferred": "Robotics background..."
    }
    
    # Note: This will fail without a real API key in execution, 
    # but serves as the implementation structure.
    try:
        print(analyzer._construct_prompt(mock_job))
        print("\n[NOTE: Run with valid API key to see generation]")
    except Exception as e:
        print(e)
