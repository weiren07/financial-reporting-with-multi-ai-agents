# main.py
from agents.fundamental_analyst import get_raw_fundamentals, analyze_fundamentals
from agents.technical_analyst import analyze_technical_indicators
from agents.funding_manager import analyze_funding

def generate_full_report(ticker):
    # Fetch raw data for use by different agents
    raw_fundamental_data = get_raw_fundamentals(ticker)
    
    # Generate each type of analysis
    fundamentals_analysis = analyze_fundamentals(raw_fundamental_data)  # Pass the raw data dictionary here
    technical_analysis = analyze_technical_indicators(ticker)
    funding_analysis = analyze_funding(raw_fundamental_data)

    # Combine all analyses into a final report
    report = f"""
    === Stock Analysis Report for {ticker.upper()} ===

    **Fundamental Analysis**
    {fundamentals_analysis}

    **Technical Analysis**
    {technical_analysis}

    **Funding Analysis**
    {funding_analysis}

    === End of Report ===
    """
    return report

# Run the main program
if __name__ == "__main__":
    ticker = input("Enter the company ticker symbol: ").upper()
    report = generate_full_report(ticker)
    print(report)
