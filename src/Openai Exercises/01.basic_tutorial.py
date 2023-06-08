import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
old_api_base = openai.api_base
openai.api_base = "http://100.98.81.104:8000/v1"

name = "Greg"
race = "Dwarf"
class_name = "Protection Warrior"
image_style = "Ancient Painting"

prompt = f"""

USER: Give me a brief backstory to an original fantasy character. They are named {name}, their race is {race} and their class is {class_name}.

BOT: 
"""
response = openai.Completion.create(
    model="vicuna-13b-v1.1-8bit", prompt=prompt, temperature=0.5, max_tokens=200
)

print(response["choices"][0]["text"])


character_description = response["choices"][0]["text"]

original_prompt = f"""

Character Description: 

```
{character_description}
```
A short description of the character described above. It doesn't include anything about the characters motivations, goals, or anything other than what they look like and the setting they're in:


"""
response2 = openai.Completion.create(
    model="vicuna-13b-v1.1-8bit",
    prompt=original_prompt,
    temperature=0.5,
    max_tokens=200,
)

print(response2["choices"][0]["text"])

openai.api_base = old_api_base

response = openai.Image.create(
    prompt=response2["choices"][0]["text"] + f". In the style of a {image_style}",
    n=1,
    size="1024x1024",
)

print(response["data"][0]["url"])
