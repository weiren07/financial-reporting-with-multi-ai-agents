# agents/technical_analyst.py
import yfinance as yf
from utils import get_openai_client

def analyze_technical_indicators(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")

    # Calculate technical indicators
    hist['SMA_50'] = hist['Close'].rolling(window=50).mean()
    hist['SMA_200'] = hist['Close'].rolling(window=200).mean()
    latest = hist.iloc[-1]
    indicators = {
        'current_price': latest['Close'],
        'sma_50': latest['SMA_50'],
        'sma_200': latest['SMA_200'],
        'trend': "upward" if latest['SMA_50'] > latest['SMA_200'] else "downward"
    }

    # Generate an analysis using OpenAI
    client = get_openai_client()
    prompt = f"Analyze the technical indicators of {ticker}: the current price is {indicators['current_price']}, the 50-day SMA is {indicators['sma_50']}, the 200-day SMA is {indicators['sma_200']}, indicating a {indicators['trend']} trend."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_tokens=300,
        messages=[
            {"role": "system", "content": "You are a technical analyst specializing in stock trends."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
