# stock_data_fetcher.py
import yfinance as yf
import pandas as pd
from typing import Dict, Any

class StockDataFetcher:
    def __init__(self, ticker: str):
        self.ticker = ticker.upper()
        self.stock = yf.Ticker(self.ticker)
        self.hist = self.stock.history(period="1y")

    @staticmethod
    def calculate_rsi(data: pd.DataFrame, periods: int = 14) -> pd.Series:
        """Calculate RSI"""
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
        rs = gain / loss
        print(rs)
        return 100 - (100 / (1 + rs))

    def analyze_technical_indicators(self) -> Dict[str, Any]:
        """Calculate technical indicators like SMA and RSI"""
        self.hist['SMA_50'] = self.hist['Close'].rolling(window=50).mean()
        self.hist['SMA_200'] = self.hist['Close'].rolling(window=200).mean()
        self.hist['RSI'] = self.calculate_rsi(self.hist)

        latest = self.hist.iloc[-1]
        trend = "Bullish" if latest['SMA_50'] > latest['SMA_200'] else "Bearish"

        return {
            'current_price': round(latest['Close'], 2),
            'sma_50': round(latest['SMA_50'], 2),
            'sma_200': round(latest['SMA_200'], 2),
            'rsi': round(latest['RSI'], 2),
            'trend': trend
        }

    def get_basic_info(self) -> Dict[str, Any]:
        """Fetch basic stock information"""
        stock_info = self.stock.info
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
            'ebitda': stock_info.get('ebitda', 'N/A')
        }

    def fetch_all_data(self) -> Dict[str, Any]:
        """Fetch all relevant stock data"""
        basic_info = self.get_basic_info()
        technical_indicators = self.analyze_technical_indicators()
        basic_info['technical_indicators'] = technical_indicators
        return basic_info

if __name__ =="__main__":
    amd_fetcher = StockDataFetcher("AMD")
    
    # Fetch all data
    print(amd_fetcher.analyze_technical_indicators())