# Social Media Sentiment Analysis Engine

## Overview

The Social Media Sentiment Analysis Engine is a professional-grade end-to-end machine learning project designed to analyze and visualize public opinion from social media data. It demonstrates the complete lifecycle of sentiment analytics, from synthetic data generation and NLP preprocessing to model training and high-fidelity interactive dashboard deployment.

## Problem Statement

Understanding customer sentiment across social platforms is critical for modern businesses to protect brand reputation and improve service delivery. Manually monitoring thousands of posts is impossible. This project provides an automated, predictive platform to categorize sentiment and identify key trends, allowing marketing and support teams to respond in real-time.

## Use Cases

- Brand Monitoring: Track how users feel about new product launches or updates.
- Crisis Management: Identify spikes in negative sentiment to address issues before they escalate.
- Customer Insights: Extract top positive and negative keywords to understand what users value most.

## Tech Stack

- Languages: Python 3.11
- Machine Learning: Scikit-learn (Logistic Regression, Naive Bayes, Random Forest)
- Natural Language Processing: NLTK (Tokenization, Stopword Removal, Regex Cleaning)
- Data Manipulation: Pandas, NumPy
- Visualizations: Plotly, Matplotlib, Seaborn, WordCloud
- UI & Dashboard: Streamlit

## Screenshots

### Sentiment Distribution Over Time

The dashboard provides a temporal view of how sentiment trends fluctuate over a 30-day period.

### Model Confusion Matrix

![Confusion Matrix](outputs/confusion_matrix.png)

### Model Comparison Analysis

![Model Comparison](outputs/model_comparison.png)

### Real-Time Text Analysis

The engine allows users to input custom text fragments to receive instant sentiment predictions with confidence scores.

## Demo Video

[![Watch Demo](https://img.youtube.com/vi/1wW4YbmwawY/0.jpg)](https://youtu.be/1wW4YbmwawY)

Click the image above to watch the full system walkthrough.

## Architecture

```text
Social-Media-Sentiment-Analysis/
├── app/                        # Dashboard application layer
│   └── dashboard.py            # Streamlit interactive UI
├── data/                       # Dataset management
│   ├── generate_dataset.py     # Synthetic data generation engine
│   ├── social_media_data.csv   # Raw generated data
│   ├── cleaned_data.csv        # Preprocessed NLP data
│   └── timeline_data.csv       # Time-series sentiment data
├── models/                     # Serialized ML artifacts
│   ├── sentiment_model.pkl     # Best performing classifier
│   └── vectorizer.pkl          # TF-IDF vectorizer artifact
├── outputs/                    # Exported reports and visualizations
│   ├── classification_report.txt
│   ├── confusion_matrix.png
│   ├── model_comparison.png
│   └── sample_predictions.csv
├── src/                        # Core processing logic
│   ├── preprocess.py           # NLP cleaning pipeline
│   ├── train_model.py          # Model selection and training
│   ├── predict.py              # Inference and sample generation
│   └── utils.py                # Regex and NLTK utilities
├── main.py                     # Pipeline orchestration script
├── requirements.txt            # Dependency specification
└── README.md                   # Project documentation
```

## How to Run

1. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

2. Execute the Data Pipeline

   ```bash
   python main.py
   ```

   This automatically generates data, performs NLP preprocessing, trains multiple models, auto-selects the best performer, and exports all plots to the outputs folder.

3. Launch the Interactive Dashboard

   ```bash
   streamlit run app/dashboard.py
   ```

## Outputs

- Processed Data: data/cleaned_data.csv (Tokenized and cleaned text).
- Static Artifacts: Available in outputs/ (Confusion Matrix, Model Comparison, Accuracy Reports).
- Interactive UI: A professional dark-themed dashboard accessible locally on port 8501.

## Future Improvements

- Integrate live API streams from X (formerly Twitter) and Reddit.
- Implement Transformer-based models (BERT/RoBERTa) for deeper semantic understanding.
- Add multi-language support for global sentiment tracking.
