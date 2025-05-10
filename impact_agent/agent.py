import sys
import os 
sys.path.append(os.path.abspath(os.path.join(__name__, "..")))
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor , create_react_agent
from langchain_core.prompts import PromptTemplate
from data_layer.crud import get_summaries
from data_layer.session import session


@tool
def get_all_summaries(topic: str):
    return get_summaries(session, name)


tools = [get_all_summaries]
llm = ChatGoogleGenerativeAI(
        model='gemini-2.0-flash',
        temperature=1,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        )
prompt = PromptTemplate.from_template(
'''
You are a topic expert on {topic}. 
Use {tools} to get latest summaries of news relating to you field of expertise and give a detailed analysis and future impact of the news

Example:
    topic:- India and Pakistan tension
    output of past summaries:- 1. 26 tourists killed in pehlgam
                               2. India takes responsive action by dropping missiles in Pok terrorist camps
                               3. Pakistan call it act of war and send our drone strikes
    impact:- Tensions are rising and war might be imminent between the two nuclear nations

'''
)


agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_exec = AgentExecutor(agent=agent, tools=tools, verbose=True)

