import json
import requests
import boto3
import pg8000

from datetime import datetime

# -----------------------------
# CONFIGURATION
# -----------------------------

NEWS_API_KEY = "c48f64f1a14c429eabdf375dd53ab6ad"

S3_BUCKET = "news-pipeline-raw-news-sreelakshmi"

DB_HOST = "news-pipeline-db.c1iccwg44xf2.ap-south-1.rds.amazonaws.com"

DB_NAME = "postgres"

DB_USER = "postgres"

DB_PASSWORD = "NewsPipeline123"

DB_PORT = "5432"


# -----------------------------
# MAIN LAMBDA FUNCTION
# -----------------------------

def lambda_handler(event, context):

    try:

        # NEWS API URL
        url = (
            f"https://newsapi.org/v2/top-headlines"
            f"?country=us&apiKey={NEWS_API_KEY}"
        )

        # FETCH NEWS
        response = requests.get(url)

        data = response.json()

        articles = data.get("articles", [])

        processed_articles = []

        # PROCESS ARTICLES
        for article in articles:

            processed_articles.append({

                "source":
                    article.get("source", {}).get("name"),

                "author":
                    article.get("author"),

                "title":
                    article.get("title"),

                "description":
                    article.get("description"),

                "url":
                    article.get("url"),

                "published_at":
                    article.get("publishedAt"),

                "content":
                    article.get("content"),

                "sentiment":
                    "neutral"
            })

        # CONNECT TO POSTGRESQL
        conn = pg8000.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=int(DB_PORT)
        )

        cursor = conn.cursor()

        # INSERT ARTICLES
        for article in processed_articles:

            cursor.execute(
                """
                INSERT INTO news_articles (
                    source,
                    author,
                    title,
                    description,
                    url,
                    published_at,
                    content,
                    sentiment
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    article["source"],
                    article["author"],
                    article["title"],
                    article["description"],
                    article["url"],
                    article["published_at"],
                    article["content"],
                    article["sentiment"]
                )
            )

        conn.commit()

        cursor.close()
        conn.close()

        # CREATE JSON FILE
        file_name = (
            f"news_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        # S3 CLIENT
        s3 = boto3.client("s3")

        # UPLOAD TO S3
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=file_name,
            Body=json.dumps(processed_articles)
        )

        return {
            "statusCode": 200,
            "body": json.dumps(
                "News stored successfully"
            )
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "body": json.dumps(
                str(e)
            )
        }