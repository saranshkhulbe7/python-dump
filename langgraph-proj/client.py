from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import asyncio
import os

_ = load_dotenv(find_dotenv())

openai_api_key = os.environ["OPENAI_API_KEY"]


async def main():
    client = MultiServerMCPClient(
        {
            "math-io": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "math-shttp": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
        }
    )
    tools = await client.get_tools()
    chat_model = ChatOpenAI(model="gpt-4o-mini")
    agent = create_agent(model=chat_model, tools=tools)
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (10 / 0) x 12 ?"}]}
    )
    print("Math response:", math_response["messages"][-1].content)


asyncio.run(main())
