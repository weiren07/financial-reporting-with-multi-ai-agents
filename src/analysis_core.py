import datetime
import os
from src.agent_manager import AgentManager
from src.stock_analyzer import StockAnalyzer

def run_stock_analysis(ticker:str)->tuple[str, str]:
    """
    Run the stock analysis and return the report and save the path
    """
    agent_manager = AgentManager()
    stock_analyzer = StockAnalyzer(agent_manager)
    report = stock_analyzer.analyze_stock(ticker)
    output_dir = "reports"
    os.makedirs(output_dir,exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"{ticker}_stock_report_{timestamp}.md")
    with open(output_file,"w",encoding="utf-8") as f:
        f.write(report)
    return report, output_file