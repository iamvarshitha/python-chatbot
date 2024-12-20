
import openai;

openai.api_key = "sk-proj-5Qx==paste your key"

def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input= input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break

        response = chat_gpt(user_input)
        print("Chat with intelligent varshitha : ",response)