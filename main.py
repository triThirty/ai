from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits.github.toolkit import GitHubToolkit
from langchain.utilities.github import GitHubAPIWrapper
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.tools import Tool

from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True, temperature=0)

github = GitHubAPIWrapper()
toolkit = GitHubToolkit.from_github_api_wrapper(github)
tools = toolkit.get_tools()

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


output = agent.run("""You are Python expert, please find bugs in the bug.py, and show what the bug is. Don't create branch or PR, just check the bug and return the bug information. Think step by step. 
		   """)