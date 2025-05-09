import requests
import random
import time
import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

# Configuration
BASE_URL = "https://pornhub.gaia.domains"
MODEL = "Qwen2-0.5B-Instruct"
MAX_RETRIES = 100  # Essentially infinite retries
RETRY_DELAY = 5  # Seconds between retries
QUESTION_DELAY = 1  # Seconds between successful questions

QUESTIONS = [
    # Core No-Code
    "What is no-code?",
    "Why use no-code for websites?",
    "Which no-code tools are popular for websites?",
    "What to look for in a no-code platform?",
    "How to start a no-code website?",
    "How to add pages in no-code?",
    "How to customize a no-code site's look?",
    "Can no-code integrate with other services?",
    "How to make a no-code site mobile-friendly?",
    "How to launch a site with no-code?",
    "Can no-code handle e-commerce?",
    "What are no-code platform limitations?",
    "How to manage SEO on a no-code site?",
    "Can I use custom domains with no-code?",
    "How to secure a no-code website?",
    "How to publish a site with no-code?",
    "How to add payments with no-code?",
    "How to optimize speed in no-code?",
    "How to add Google Maps with no-code?",
    "How to ensure site accessibility with no-code?",

    # AI & Automation
    "How is AI used in no-code platforms?",
    "Can AI generate full websites in no-code tools?",
    "Can no-code tools use AI to create content?",
    "How to automate workflows with no-code?",
    "What AI integrations work with no-code platforms?",
    "Can you connect ChatGPT with no-code tools?",
    "How to build a chatbot using no-code?",
    "Can no-code use natural language commands?",
    "What are the benefits of AI-powered no-code tools?",
    "How to do sentiment analysis using no-code + AI?",

    # Business Use Cases
    "Can no-code help startups build MVPs?",
    "How to use no-code for business automation?",
    "Can no-code be used to build SaaS platforms?",
    "How can small businesses benefit from no-code?",
    "How to use no-code for inventory management?",
    "Can no-code build internal business dashboards?",
    "How to automate customer support with no-code?",
    "Can no-code tools replace Excel automation?",
    "How to collect and process leads using no-code?",
    "What are enterprise use cases for no-code?",

    # App Building
    "How to use no-code for app development?",
    "What kinds of apps can no-code make?",
    "Which no-code platforms are best for apps?",
    "How to pick a no-code app platform?",
    "How to manage data in no-code apps?",
    "How to authenticate users in no-code apps?",
    "How to secure no-code apps?",
    "How to integrate APIs in no-code apps?",
    "Can no-code apps send push notifications?",
    "How to deploy no-code mobile apps?",

    # Low-Code vs. No-Code
    "What is the difference between low-code and no-code?",
    "When should you choose low-code over no-code?",
    "Can developers extend no-code tools with code?",
    "What skills help in low-code development?",
    "What are the limitations of low-code solutions?",

    # Design & UX
    "How to ensure good UX in no-code designs?",
    "What are common UX mistakes in no-code tools?",
    "Can you use design systems in no-code?",
    "How to test UX in no-code platforms?",
    "How to customize fonts with no-code tools?",
    "How to personalize UI in no-code apps?",

    # Team Collaboration & Project Management
    "Can teams collaborate on no-code projects?",
    "How to manage roles in no-code apps?",
    "How to assign tasks in no-code workflows?",
    "What are best practices for team-based no-code work?",
    "How to maintain a shared no-code codebase?",

    # Marketing & Analytics
    "How to integrate analytics in no-code?",
    "How to use no-code for email marketing?",
    "How to build landing pages with no-code?",
    "Can no-code help with A/B testing?",
    "How to connect no-code to Google Analytics?",
    "How to use CRM tools with no-code apps?",

    # Industry Use Cases
    "Can no-code be used in education?",
    "How to use no-code for healthcare tools?",
    "Can no-code make legal service platforms?",
    "How to build fintech tools with no-code?",
    "Are there no-code platforms for real estate?",
    "How to build nonprofit websites with no-code?",
    "Can no-code create event registration apps?",

    # Maintenance & Scaling
    "What happens when a no-code app grows?",
    "How to backup no-code projects?",
    "How to refactor a no-code workflow?",
    "How to export data from no-code platforms?",
    "Can no-code apps scale to thousands of users?",
    "What are strategies for optimizing performance in no-code?",
    "Can you migrate from no-code to custom code later?",
    "How to handle large datasets in no-code tools?",
    "How to prevent data loss in no-code apps?",

    # Miscellaneous
    "Where to learn about no-code development?",
    "How to build a portfolio site with no-code?",
    "What are examples of successful no-code products?",
    "Can you freelance using no-code tools?",
    "How to troubleshoot common no-code errors?",
    "What support options do no-code platforms offer?",
]

def chat_with_ai(api_key: str, question: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    messages = [
        {"role": "user", "content": question}
    ]

    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    for attempt in range(MAX_RETRIES):
        try:
            logging.info(f"Attempt {attempt+1} for question: {question[:50]}...")
            response = requests.post(
                f"{BASE_URL}/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]

            logging.warning(f"API Error ({response.status_code}): {response.text}")
            time.sleep(RETRY_DELAY)

        except Exception as e:
            logging.error(f"Request failed: {str(e)}")
            time.sleep(RETRY_DELAY)

    raise Exception("Max retries exceeded")

def run_bot(api_key: str):
    while True:  # Outer loop to repeat the questions indefinitely
        random.shuffle(QUESTIONS)
        logging.info(f"Starting chatbot with {len(QUESTIONS)} questions in random order")

        for i, question in enumerate(QUESTIONS, 1):
            logging.info(f"\nProcessing question {i}/{len(QUESTIONS)}")
            logging.info(f"Question: {question}")

            start_time = time.time()
            try:
                response = chat_with_ai(api_key, question)
                elapsed = time.time() - start_time

                # Print the entire response
                print(f"Answer to '{question[:50]}...':\n{response}")

                logging.info(f"Received full response in {elapsed:.2f}s")
                logging.info(f"Response length: {len(response)} characters")

                # Ensure the script waits for the full response before proceeding
                time.sleep(QUESTION_DELAY)  # Wait before asking next question

            except Exception as e:
                logging.error(f"Failed to process question: {str(e)}")
                continue

def main():
    print("Title: GaiaAI Chatbot")
    print("Twitter: https://x.com/0xMoei")
    api_key = input("Enter your API key: ")
    run_bot(api_key)

if __name__ == "__main__":
    main()
