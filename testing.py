import os
import asyncio
from autogen_core.components.models import OpenAIChatCompletionClient
from autogen_core.components.models import UserMessage
import config
# Retrieve the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client
model_client = OpenAIChatCompletionClient(
    model="gpt-4",  # Specify the model you intend to use
    api_key=api_key
)

async def generate_essay(topic):
    # Create a user message
    user_message = UserMessage(content=f"Write an essay about {topic}.", source="user")
    
    # Send the message to the model client and get the response
    response = await model_client.create(messages=[user_message])
    
    # Extract and return the generated essay
    essay = response.content
    return essay

if __name__ == "__main__":
    topic = "penguins"
    essay = asyncio.run(generate_essay(topic))
    print(essay)
