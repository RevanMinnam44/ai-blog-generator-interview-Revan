from flask import Flask, request, jsonify
from seo_fetcher import fetch_seo_metrics
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
import re
import datetime
import os

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()


@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Missing keyword'}), 400

    seo_data = fetch_seo_metrics(keyword)
    blog_post = generate_blog_post(keyword, seo_data)

    # Clean filename from keyword
    safe_keyword = re.sub(r'\W+', '_', keyword.lower())
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"blog_{safe_keyword}_{timestamp}.md"

    # Ensure output directory exists
    output_dir = "generated_posts"
    os.makedirs(output_dir, exist_ok=True)

    # Write the file
    with open(os.path.join(output_dir, filename), "w") as f:
        f.write(blog_post)

    return jsonify({
        'keyword': keyword,
        'seo': seo_data,
        'post': blog_post
    }), 200


@app.route('/')
def home():
    return 'API is running!'

def daily_blog_task():
    from seo_fetcher import fetch_seo_metrics
    from ai_generator import generate_blog_post
    import os, re, datetime

    keyword = "wireless earbuds"
    seo_data = fetch_seo_metrics(keyword)
    blog_post = generate_blog_post(keyword, seo_data)

    # Save post
    safe_keyword = re.sub(r'\W+', '_', keyword.lower())
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"blog_{safe_keyword}_{timestamp}.md"

    output_dir = "generated_posts"
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        f.write(blog_post)

    print(f"[Scheduler] Generated blog post: {filepath}")

scheduler.add_job(daily_blog_task, 'interval', days=1)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
