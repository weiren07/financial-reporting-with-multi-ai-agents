from openai import OpenAI  # Import as per your specified setup
from config import OPENAI_API_KEY

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_essay(topic):
    # Define the prompt as specified
    prompt = f"Write an essay about {topic}."
    
    # Try to create a completion using the chat API
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-3.5-turbo" as needed
            temperature=0.7,
            max_tokens=500,
            messages=[
                {"role": "system", "content": "man"},
                {"role": "user", "content": prompt}
            ],
            top_p=1.0
        )
        
        # Extract the generated essay from the response
        essay = response.choices[0].message.content
        return essay

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
topic = "penguins"
essay = generate_essay(topic)
print(essay)
