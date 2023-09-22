# VoiceAI

This is a basic demo of an AI voice assistant. It uses an [LLM](https://huggingface.co/databricks/dolly-v2-3b) to generate resonses to voice prompts.

## How it works

VoiceAI first takes microphone input and converts it into a text prompt using Google's speech-to-text. This prompt is then used by the LLM to generate a text response. Using text-to-speech, the response is "said."

## How to use

Make sure you have Python 3 installed and the following dependencies:

- PyTorch
- Transformers
- SpeechRecognition
- Google TTS
- Playsound

Then run it with `python3 main.py`. Once everything has been initialized (which takes a while, especially the first time), it will prompt you to press enter to begin. Say aloud any prompt you like and wait for a response. Once you get a response, say something else to get another. To quit, say "exit."