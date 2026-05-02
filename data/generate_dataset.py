import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = BASE_DIR / "outputs"
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(parents=True, exist_ok=True)

def generate_text(sentiment):
    if sentiment == 'POSITIVE':
        templates = [
            "Just tried the new feature, it is incredibly {adj} and {adj2}!",
            "I absolutely love how {adj} the service is now.",
            "Wow, this is {adj}! My team is so happy.",
            "Great update, everything is running very {adj}.",
            "The best experience I've had so far. So {adj}."
        ]
        adjectives = ["efficient", "reliable", "fast", "intuitive", "smooth", "amazing", "great"]
    elif sentiment == 'NEGATIVE':
        templates = [
            "I'm experiencing terrible {issue} issues today.",
            "This is so {adj}, the app keeps throwing {issue} errors.",
            "Why is the service so {adj}? Fix the {issue}!",
            "Very disappointed with the recent update, too much {issue}.",
            "Constant {issue} and {issue}. Really {adj} experience."
        ]
        adjectives = ["slow", "complex", "frustrating", "terrible", "unreliable"]
        issues = ["latency", "error", "timeout", "bug", "crash"]
    else:
        templates = [
            "The system is currently {state}.",
            "Just reading through the latest {news}. It's {state}.",
            "Update released today. Status is {state}.",
            "I noticed the UI changed. It seems {state}.",
            "No major issues, running in {state} mode."
        ]
        state = ["normal", "average", "standard", "unchanged", "typical"]
    
    template = random.choice(templates)
    
    if sentiment == 'POSITIVE':
        return template.format(adj=random.choice(adjectives), adj2=random.choice(adjectives))
    elif sentiment == 'NEGATIVE':
        return template.format(issue=random.choice(issues), adj=random.choice(adjectives))
    else:
        return template.format(state=random.choice(state), news="documentation")

def main():
    # Generate 1000 posts
    # Positive (420), Negative (317), Neutral (263)
    sentiments = ['POSITIVE'] * 420 + ['NEGATIVE'] * 317 + ['NEUTRAL'] * 263
    random.shuffle(sentiments)
    
    data = []
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    
    for sentiment in sentiments:
        text = generate_text(sentiment)
        random_seconds = random.randint(0, 30 * 24 * 60 * 60)
        timestamp = start_date + timedelta(seconds=random_seconds)
        data.append({'text': text, 'sentiment': sentiment, 'timestamp': timestamp.isoformat()})
        
    df = pd.DataFrame(data)
    social_media_data_path = DATA_DIR / "social_media_data.csv"
    df.to_csv(str(social_media_data_path), index=False)
    
    print(f"Generated {social_media_data_path}")
    print(df.head())
    print(df['sentiment'].value_counts())
    
    # Generate timeline data
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    timeline_df = df.groupby(['date', 'sentiment']).size().unstack(fill_value=0).reset_index()
    # rename columns
    timeline_df = timeline_df.rename(columns={
        'POSITIVE': 'positive_count',
        'NEGATIVE': 'negative_count',
        'NEUTRAL': 'neutral_count'
    })
    
    timeline_data_path = DATA_DIR / "timeline_data.csv"
    timeline_df.to_csv(str(timeline_data_path), index=False)
    print(f"Generated {timeline_data_path}")
    print(timeline_df.head())

if __name__ == "__main__":
    main()