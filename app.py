# app.py

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from src.analysis_core import run_stock_analysis
from src.utils import logger 
class StockAnalysisApp:
    def __init__(self):
        self.console = Console()

    def run(self):
        ticker = input("Enter the company ticker symbol: ").upper()
        self.console.print(f"\n[bold green]Analyzing {ticker}...[/bold green]\n")

        report, output_file = run_stock_analysis(ticker)
        self.console.print("=====================", style="bold blue")
        
        # Display the report with Markdown formatting for better styling
        markdown_report = Markdown(report)
        self.console.print(Panel(markdown_report, title="[bold yellow]Stock Analysis Report[/bold yellow]", border_style="cyan"))

        self.console.print("=====================", style="bold blue")
        markdown_report = Markdown(report)
        self.console.print(Panel(markdown_report, title="[bold yellow]Stock Analysis Report[/bold yellow]", border_style="cyan"))
        self.console.print("=====================", style="bold blue")
        self.console.print(f"\n[bold blue]Report saved to:[/bold blue] {output_file}")
if __name__ == "__main__":
     # Ensure logger is imported for logging
    try:
        app = StockAnalysisApp()
        app.run()
    except ValueError as ve:
        print(f"Configuration Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
