from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get environment variables
USERNAME = os.getenv('UNAME')
PASSWORD = os.getenv('PW')

async def main():
    agent = Agent(
        task=f"Go to comunio.de, click login, login with username {USERNAME} and password {PASSWORD}, click on my team and return all the players of my team",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
