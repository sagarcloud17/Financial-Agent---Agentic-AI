from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
from phi.model.openai import OpenAIChat
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True,company_info=True,income_statements=True,key_financial_ratios=True,technical_indicators=True,historical_prices=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response(input("Ask the question:"),stream=True)

