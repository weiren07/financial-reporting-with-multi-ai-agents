# agent_manager.py
from autogen import AssistantAgent, UserProxyAgent
from typing import Dict, Any
from src.utils import get_config_list
import src.prompt as prompt
class AgentManager:
    def __init__(self):
        self.config_list = get_config_list()
        self.agents = self.create_agents()

    def create_agents(self) -> Dict[str, Any]:
        user_proxy = UserProxyAgent(
            name="user_proxy",
            system_message = prompt.UserProxyAgent_prompt,
            human_input_mode="NEVER",
            code_execution_config={
                "last_n_messages": 3,
                "work_dir": "workspace",
                "use_docker": False
            }
        )

        fundamental_analyst = AssistantAgent(
            name="fundamental_analyst",
            system_message=prompt.fundamental_analyst_prompt,
            llm_config={"config_list": self.config_list}
        )

        technical_analyst = AssistantAgent(
            name="technical_analyst",
            system_message=prompt.technical_analyst_prompt,
            llm_config={"config_list": self.config_list}
        )

        funding_manager = AssistantAgent(
            name="funding_manager",
            system_message=prompt.funding_manager_prompt,
            llm_config={"config_list": self.config_list}
        )

        report_writer = AssistantAgent(
            name="report_writer",
            system_message = prompt.report_writer_prompt,
            llm_config={"config_list": self.config_list}
        )

        return {
            "user_proxy": user_proxy,
            "fundamental_analyst": fundamental_analyst,
            "technical_analyst": technical_analyst,
            "funding_manager": funding_manager,
            "report_writer": report_writer
        }

    def get_agent(self, name: str) -> Any:
        return self.agents.get(name)
