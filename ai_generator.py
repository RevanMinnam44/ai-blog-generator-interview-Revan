#ai_generator.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog_post(keyword, seo_data):
    prompt = f"""
    Write a blog post about "{keyword}" optimized for SEO.
    Include:
    - Search volume: {seo_data['search_volume']}
    - Keyword difficulty: {seo_data['keyword_difficulty']}
    - CPC: ${seo_data['avg_cpc']}

    Use headings, bullet points, and affiliate link placeholders like {{AFF_LINK_1}}.
    Format in Markdown.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
