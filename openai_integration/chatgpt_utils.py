import openai

def chatgpt_response(prompt, event_data):
    system_prompt = """
    You are an assistant that helps users find events based on their preferences.
    The available events are:
    {}
    Respond to the user's query with the best event suggestions.
    """.format(event_data.to_string())

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=system_prompt + "\nUser: " + prompt + "\nAssistant:",
        max_tokens=150
    )
    return response.choices[0].text.strip()
