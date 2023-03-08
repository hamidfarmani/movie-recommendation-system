# Movie Recommendation System

This is a simple movie recommendation system app that suggests 10 movies based on the user's input. The app is built using Gradio and OpenAI's GPT-3.5 language model.

## Code walkthrough

I have created a YouTube video in Persian, explaining this. You can watch it here:
[![](https://markdown-videos.deta.dev/youtube/YGsUtaEO9Ls)](https://youtu.be/YGsUtaEO9Ls)

## Usage

To use the app, simply enter the name of a movie that you have watched in the input field and click on "Submit". The system will suggest 10 movies based on the input.

## Requirements

The app requires the following dependencies:

- Gradio
- OpenAI API Key
- GPT-3.5 Turbo Language Model

## Installation

To install the dependencies, run the following commands in your terminal:

```
pip install gradio
pip install openai
```

or

```
pip install -r requirements.txt
```

## Setup

Before using the app, you need to set up your OpenAI API key. You can do this by creating an account on OpenAI, and then generating an API key from the dashboard.

Once you have generated your API key, update the config.py file with your API key as follows:

```
OPEN_AI_API_KEY = "your_api_key_here"
```

# Launching the app

To launch the app, run the following command in your terminal:

```
python app.py
```

This will launch the app in your default web browser.

## Limitations

Please note that the movie recommendation system is based on the GPT-3.5 language model, which may not always provide accurate results. Also, the app is currently limited to suggesting only 10 movies per input.

## Credits

The app was built by Hamid Farmani using Gradio and OpenAI's GPT-3.5 Turbo language model.
