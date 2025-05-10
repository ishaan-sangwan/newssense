from newsapi import NewsApiClient
from datetime import timedelta, date
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate


@tool
def get_news(keyword):
    current_date = date.today() - timedelta(days=4)
    news = NewsApiClient(api_key='80e08f9fb934402a9c06ef29bcaa2f63')
    top_headlines = news.get_everything(
            q=keyword,
            language='en',
            sort_by='publishedAt',
            from_param=str(current_date)
            )
    return top_headlines


tools = [get_news]

llm = ChatGoogleGenerativeAI(
        model='gemini-2.0-flash',
        temperature=1,
        max_tokens=None,
        timeout=None,
        max_retires=2,
        )

prompt = PromptTemplate.from_template(
    ''' 
You are an internet jounralist tasked with getting recent news on topic.

```
    {topic}
```

Summarize all these news headlines into 300 words with brief dexcription of 
all different types of news available to it.

You have these tools at your dispensation:

```
{tools}
```

IMPORTANT:
1. Ensure everything in summary is accurate and from the context fetched.

    '''
        )

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_exec = AgentExecutor(agent=agent, tools=tools, verbose=True)

