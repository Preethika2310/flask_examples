import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
from autogen_agentchat.ui import Console
import requests
load_dotenv()
 
async def get_weather(city:str)->str:
    """Get the weather for a given city."""
    try:
        API_KEY=os.getenv("OPEN_WEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response=requests.get(url,timeout=60)
        data=response.json()
        temp=data['main']['temp']
        description=data['weather'][0]['description']
        return f"{city}: {temp} !C, {description}"
    except Exception as e:
        return f"Error: {str(e)}"
async def get_weather_with_agent(city:str)-> str:
    """Get weather information using AI agent for a given city."""
    try:
        API_KEY=os.getenv("OPEN_WEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response=requests.get(url,timeout=60)
        data=response.json()
        temp=data['main']['temp']
        description=data['weather'][0]['description']
        return f"{city}: {temp} !C, {description}"
    except Exception as e:
        return f"Error: {str(e)}"
async def get_weather_with_agent(city:str)-> str:
    """Get weather information using AI Agent for a given City."""
    try:
        model_client = OpenAIChatCompletionClient(
            model = 'gpt-4o',
            api_key = os.getenv("OPENAI_API_KEY")
        )
        print("into weather agent in autogen")
        agent = AssistantAgent(
            name = "WeatherAgent",
            model_client = model_client,
            tools = [get_weather],
            system_message= """You are a helpful weather assistant. 
            Provide weather information concisely."""
        )
        # Run the agent to get weather information
        response = await agent.run(task=f"""
            What is weather in {city}? Provide a concise response.
            if the city is not valid, just respond with 'Invalid city'.
            """)
        await model_client.close()
        print("response", response)
        # Extract the responses content
        if hasattr(response, 'messages') and response.messages:
            return response.messages[-1].content
        elif hasattr(response,'content'):
            return response.content
        else:
            return str(response)
    except Exception as e:
        return f"Error getting with agent:{str(e)}"