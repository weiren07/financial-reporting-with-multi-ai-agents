# app.py
from agent_manager import AgentManager
from stock_analyzer import StockAnalyzer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
import datetime
import os
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
        output_dir = "reports"
        os.makedirs(output_dir,exist_ok = True)#ensure the dictionary exist
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(output_dir, f"{ticker}_stock_report_{timestamp}.md")
        with open(output_file, "w", encoding="utf-8") as f:
                f.write(report)
        self.console.print(f"\n[bold blue]Report saved to:[/bold blue] {output_file}")
if __name__ == "__main__":
    from utils import logger  # Ensure logger is imported for logging
    try:
        app = StockAnalysisApp()
        app.run()
    except ValueError as ve:
        print(f"Configuration Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
