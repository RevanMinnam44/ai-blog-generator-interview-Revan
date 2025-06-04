# ai-blog-generator-interview-Revan

This is a Python Flask application that generates SEO-optimized blog posts using OpenAI, based on a given keyword. It also includes a daily automation feature that generates and saves a blog post once per day using a scheduler.

How to Run

1. Set Up a Virtual Environment (Optional):
    python3 -m venv venv
    source venv/bin/activate

2. Install the necessary packages
    - Flask
    - openai
    - python-dotenv
    - apscheduler

3. Create an .env file and set up API key

4. Run the Flask App
    python app.py

5. Open the link on the browser: http://127.0.0.1:5050/generate?keyword=wireless+earbuds

The blog post will be:
	•	Returned as JSON
	•	Saved to the generated_posts/ folder

APScheduler is being used to auto-generate a blog post once per day

