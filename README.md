# Stock Analysis Application

An intelligent stock analysis tool that leverages multiple AI agents to provide comprehensive market insights. The application combines fundamental analysis, technical analysis, and financial health metrics to deliver detailed stock reports.

## 🌟 Features

- **Multi-Agent Analysis**: Utilizes specialized AI agents for different aspects of stock analysis
  - Fundamental Analysis Agent
  - Technical Analysis Agent
  - Financial Health Agent
  - Report Writing Agent

- **Comprehensive Data Analysis**
  - Real-time stock data fetching
  - Technical indicators (SMA, RSI, MACD, Bollinger Bands)
  - Fundamental metrics (P/E ratio, ROE, Debt/Equity)
  - Financial health assessment

- **Analysis Types**
  - Comprehensive Analysis (All metrics)
  - Fundamental Analysis (Business metrics and financials)
  - Technical Analysis (Price action and indicators)

- **User-Friendly Interface**
  - Progress tracking during analysis
  - Rich text formatting for reports
  - Interactive analysis type selection
  - Clear error messaging

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Internet connection for real-time data fetching

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/weiren07/AI-agent.git
cd stock-analysis-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create .env file
touch .env

# Add your OpenAI API key to config.py or inside .env
echo "OPENAI_API_KEY=your_api_key_here" >> .env
```

## 📊 Usage

1. Run the application:
```bash
python app.py
```

2. Enter a stock ticker symbol when prompted

3. Select analysis type:
   - Comprehensive Analysis (1)
   - Fundamental Analysis (2)
   - Technical Analysis (3)

4. Review the generated report

## 📁 Project Structure

```
stock-analysis-app/
├── app.py                 # Main application entry point
├── stock_analyzer.py      # Core analysis logic
├── stock_data_fetcher.py  # Stock data retrieval
├── agent_manager.py       # AI agent management
├── utils.py              # Utility functions
├── requirements.txt      # Project dependencies
├── .env                 # Environment variables
├── config.py            # storing open ai key
└── README.md            # Project documentation
```

## 🚀 Key Components

### StockAnalyzer
Orchestrates the analysis process by:
- Managing AI agents
- Processing stock data
- Generating comprehensive reports

### StockDataFetcher
Handles data retrieval including:
- Real-time stock data
- Technical indicators
- Financial metrics

### AgentManager
Manages AI agents for:
- Fundamental analysis
- Technical analysis
- Financial health assessment
- Report writing

## 📈 Analysis Metrics

### Technical Indicators
- Simple Moving Averages (50 & 200 day)
- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)
- Bollinger Bands
- Volume Analysis

### Fundamental Metrics
- Price-to-Earnings (P/E) Ratio
- Return on Equity (ROE)
- Debt-to-Equity Ratio
- Current Ratio
- Quick Ratio
- EBITDA

### Financial Health Metrics
- Market Capitalization
- Liquidity Ratios
- Debt Levels
- Cash Flow Analysis

## 🛡️ Error Handling

The application includes robust error handling for:
- Invalid ticker symbols
- API connection issues
- Data retrieval failures
- Analysis processing errors

## 🔧 Configuration

Configure the application through environment variables:
```env
OPENAI_API_KEY=your_api_key_here
LOG_LEVEL=INFO
DATA_CACHE_DURATION=3600
```

## 📝 Logging

Logs are stored in `app.log` and include:
- Analysis requests
- Error messages
- Performance metrics
- Agent interactions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for GPT models
- [yfinance](https://github.com/ranaroussi/yfinance) for stock data
- [Rich](https://github.com/Textualize/rich) for terminal formatting
- [AutoGen](https://github.com/microsoft/autogen) for agent framework

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Always conduct your own research and consult with financial advisors before making investment decisions.