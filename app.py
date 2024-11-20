# app.py
from agent_manager import AgentManager
from stock_analyzer import StockAnalyzer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

class StockAnalysisApp:
    def __init__(self):
        self.agent_manager = AgentManager()
        self.stock_analyzer = StockAnalyzer(self.agent_manager)
        self.console = Console()

    def run(self):
        ticker = input("Enter the company ticker symbol: ").upper()
        self.console.print(f"\n[bold green]Analyzing {ticker}...[/bold green]\n")

        report = self.stock_analyzer.analyze_stock(ticker)
        self.console.print("=====================", style="bold blue")
        
        # Display the report with Markdown formatting for better styling
        markdown_report = Markdown(report)
        self.console.print(Panel(markdown_report, title="[bold yellow]Stock Analysis Report[/bold yellow]", border_style="cyan"))

        self.console.print("=====================", style="bold blue")

if __name__ == "__main__":
    from utils import logger  # Ensure logger is imported for logging
    try:
        app = StockAnalysisApp()
        app.run()
    except ValueError as ve:
        print(f"Configuration Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
