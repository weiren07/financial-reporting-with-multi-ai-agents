# stock_analyzer.py
import autogen
from typing import Dict, Any
from agent_manager import AgentManager
from stock_data_fetcher import StockDataFetcher
from utils import logger  # Assuming you've set up logging as previously suggested

class StockAnalyzer:
    def __init__(self, agent_manager: AgentManager):
        self.agent_manager = agent_manager

    def analyze_stock(self, ticker: str) -> str:
        try:
            logger.info(f"Starting analysis for ticker: {ticker}")
            # Fetch stock data
            data_fetcher = StockDataFetcher(ticker)
            stock_data = data_fetcher.fetch_all_data()

            # Prepare initial message
            initial_message = self._prepare_initial_message(ticker, stock_data)

            # Create group chat including all agents
            groupchat = autogen.GroupChat(
                agents=[
                    self.agent_manager.get_agent("user_proxy"),
                    self.agent_manager.get_agent("fundamental_analyst"),
                    self.agent_manager.get_agent("technical_analyst"),
                    self.agent_manager.get_agent("funding_manager"),
                    self.agent_manager.get_agent("report_writer"),  # Ensure report_writer is included
                ],
                 speaker_selection_method="round_robin",
                messages=[],
                max_round=5 # Increased to accommodate all agents
            )

            # Create manager
            manager = autogen.GroupChatManager(
                groupchat=groupchat,
                llm_config={"config_list": self.agent_manager.config_list}
            )

            # Initiate chat
            response = self.agent_manager.get_agent("user_proxy").initiate_chat(
                manager,
                message=initial_message,
                silent=False
            )

            # Process chat history
            chat_history = groupchat.messages
            logger.info(f"Chat history: {chat_history}")  # Log chat history for debugging
            report = self._generate_report(chat_history)

            logger.info(f"Successfully analyzed ticker: {ticker}")
            return report

        except Exception as e:
            logger.error(f"Error during analysis: {e}")
            return f"An error occurred during analysis: {str(e)}\nPlease check your OpenAI API key and configuration."

    def _prepare_initial_message(self, ticker: str, data: Dict[str, Any]) -> str:
        return f"""
        Please analyze **{ticker}** ({data['name']}) with the following data:

        ### Basic Information
        - **Company:** {data['name']}
        - **Sector:** {data['sector']}
        - **Industry:** {data['industry']}

        ### Financial Metrics
        - **Market Cap:** ${data['market_cap']:,.2f}
        - **P/E Ratio:** {data['pe_ratio']}
        - **ROE:** {data['roe']}
        - **Debt/Equity:** {data['debt_to_equity']}
        - **Current Ratio:** {data['current_ratio']}
        - **Quick Ratio:** {data['quick_ratio']}
        - **EBITDA:** ${data['ebitda']:,.2f}

        ### Technical Indicators
        - **Current Price:** ${data['technical_indicators']['current_price']}
        - **50-day SMA:** ${data['technical_indicators']['sma_50']}
        - **200-day SMA:** ${data['technical_indicators']['sma_200']}
        - **RSI (14):** {data['technical_indicators']['rsi']}
        - **Trend:** {data['technical_indicators']['trend']}

        Please provide a comprehensive analysis of this stock based on the above metrics.
        """

    def _generate_report(self, chat_history: list) -> str:
        """
        Generate a final report from the chat history.
        """
        report_sections = []
        for msg in chat_history:
            sender = msg.get('name')  # Use 'name' instead of 'sender'
            content = msg.get('content', '').strip()

            if not sender:
                logger.warning("Encountered a message with no sender. Skipping.")
                continue

            if sender == "user_proxy":
                continue  # Skip messages from the user proxy

            if not isinstance(sender, str):
                logger.error(f"Invalid sender type: {sender} (type: {type(sender)})")
                continue

            try:
                sender_name = sender.replace('_', ' ').capitalize()
            except AttributeError:
                logger.error(f"Cannot process sender: {sender}")
                continue

            if content:
                section = f"### {sender_name}\n\n{content}"
                report_sections.append(section)
            else:
                logger.warning(f"No content from {sender_name}")

        if not report_sections:
            logger.warning("No analysis available from agents.")
            return "No analysis available from agents."

        report = "\n\n".join(report_sections)
        return report
