# agents/fundamental_analyst.py
import yfinance as yf
from utils import get_openai_client

def get_raw_fundamentals(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    # Extract raw fundamental data needed for analysis
    return {
        'name': stock_info.get('longName', 'N/A'),
        'sector': stock_info.get('sector', 'N/A'),
        'industry': stock_info.get('industry', 'N/A'),
        'market_cap': stock_info.get('marketCap', 'N/A'),
        'pe_ratio': stock_info.get('trailingPE', 'N/A'),
        'roe': stock_info.get('returnOnEquity', 'N/A'),
        'debt_to_equity': stock_info.get('debtToEquity', 'N/A'),
        'current_ratio': stock_info.get('currentRatio', 'N/A'),
        'quick_ratio': stock_info.get('quickRatio', 'N/A'),
        'ebitda': stock_info.get('ebitda', 'N/A'),
    }

def analyze_fundamentals(fundamental_data):
    client = get_openai_client()
    prompt = f"Analyze the fundamentals of {fundamental_data['name']} in the {fundamental_data['sector']} sector with a market cap of {fundamental_data['market_cap']}, P/E ratio of {fundamental_data['pe_ratio']}, and ROE of {fundamental_data['roe']}."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_tokens=300,
        messages=[
            {"role": "system", "content": "You are a financial analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
