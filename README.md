# Stock Market Prediction using Historical Data and Sentiment Analysis

![Stock_Market_Architecture](https://github.com/n1haldev/TDL-Project/assets/97780641/5bffe33e-c1dc-453a-8ef8-2637913ee8e5)

The model is going to take in data from two data pipelines namely the historical data pipeline and the stock market news data for sentiment analysis data pipeline. 

## To Code:
The programs to be written are:
1. VMD.py - Variation Mode decomposition decomposes the historical data and helps find hidden patterns. This can help the LSTM.py learn the trend, seasonal and cylic component better.
2. Scraper.py - This is a file that will either scrape textual data from a news website given the time or we can alternateively explore the use of APIs for better information retreival.
3. Combiner.py - The program combines the historical data and sentiment analysis data into a single date-time related dataset. This will help the model better understand not just the patterns of historical prices but also how emotions have effected the prices of stocks.
4. LSTM.py - The final model that will understand the dataset produced by the Combiner.py and make stock price predictions.

## Components Recycled
Existing Models that will be used:
1. Text Summarization Model - There are many models in huggingface and langchain that can be made use of to reduce the size of the textual data received by the Scraper.py. (Essentially Minimal loss compression)
2. RoBERTa Model - There are other models for sentiment analysis but I liked this model (based on complete whim tho). This will take in the summarized data and output the emotion in the aspect of stock market. (positive, negative, neutral)
