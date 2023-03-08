import gradio as gr
import openai, config
openai.api_key=config.OPEN_AI_API_KEY
messages=[{"role": "system", "content": "You are a movie recommendation system. Based on user input, suggest 10 movies."}]

def suggestMovie(watchedMovie):
    messages.append({"role":"user", "content": watchedMovie})
    response=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    gptSuggestion=response["choices"][0]["message"]
    messages.append(gptSuggestion)

    result=""
    for message in messages:
        if message["role"] != "system":
            result += message["role"] + ": " + message["content"] + "\n\n"
    return result

gr.Interface(fn=suggestMovie, inputs="text", outputs="text").launch()