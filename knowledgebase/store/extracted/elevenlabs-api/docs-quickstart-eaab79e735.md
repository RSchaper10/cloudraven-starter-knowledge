# ElevenAPI quickstart | ElevenLabs Documentation

Source URL:

- https://elevenlabs.io/docs/quickstart

Dependency:

- ElevenLabs API

Collected at:

- 2026-04-15T19:44:29.554380+00:00

Direct links in scope:

- https://elevenlabs.io/docs/eleven-api/guides/cookbooks
- https://elevenlabs.io/docs/api-reference/authentication
- https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming
- https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/instant-voice-cloning
- https://elevenlabs.io/docs/overview/intro
- https://elevenlabs.io/docs/eleven-api/quickstart

Captured summary:

- ElevenAPI quickstart | ElevenLabs Documentation By the end of this guide you will have a working script that sends a text string to the ElevenLabs API and plays the returned audio through your speakers.
- You will learn how to authenticate with an API key, install the SDK, and make your first text-to-speech request.
- For guides covering other capabilities — streaming, voice cloning, speech-to-text — see the Tutorials section.
- Use the ElevenLabs text-to-speech skill to generate speech from your AI coding assistant: $ npx skills add elevenlabs/skills --skill text-to-speech Using the Text to Speech API 1 Create an API key Create an API key in the dashboard here , which you’ll use to securely access the API .
- Store the key as a managed secret and pass it to the SDKs either as a environment variable via an .env file, or directly in your app’s configuration depending on your preference.

Extracted text:

ElevenAPI quickstart | ElevenLabs Documentation

By the end of this guide you will have a working script that sends a text string to the ElevenLabs API and plays the returned audio through your speakers. You will learn how to authenticate with an API key, install the SDK, and make your first text-to-speech request.

For guides covering other capabilities — streaming, voice cloning, speech-to-text — see the

Tutorials

section.

Use the

ElevenLabs text-to-speech skill

to generate speech from your AI coding assistant:

$

npx skills add elevenlabs/skills --skill text-to-speech

Using the Text to Speech API

1

Create an API key

Create an API key in the dashboard here

, which you’ll use to securely

access the API

.

Store the key as a managed secret and pass it to the SDKs either as a environment variable via an

.env

file, or directly in your app’s configuration depending on your preference.

.env

1

ELEVENLABS_API_KEY=<your_api_key_here>

2

Install the SDK

We’ll also use the

dotenv

library to load our API key from an environment variable.

Python

TypeScript

1

pip install elevenlabs

2

pip install python-dotenv

To play the audio through your speakers, you may be prompted to install

MPV

and/or

ffmpeg

.

3

Make your first request

Create a new file named

example.py

or

example.mts

, depending on your language of choice and add the following code:

Python

TypeScript

1

from dotenv import load_dotenv

2

from elevenlabs.client import ElevenLabs

3

from elevenlabs.play import play

4

import os

5

6

load_dotenv()

7

8

elevenlabs = ElevenLabs(

9

api_key=os.getenv("ELEVENLABS_API_KEY"),

10

)

11

12

audio = elevenlabs.text_to_speech.convert(

13

text="The first move is what sets everything in motion.",

14

voice_id="JBFqnCBsd6RMkjVDRZzb", # "George" - browse voices at elevenlabs.io/app/voice-library

15

model_id="eleven_v3",

16

output_format="mp3_44100_128",

17

)

18

19

play(audio)

4

Run the code

Python

TypeScript

1

python example.py

You should hear the audio play through your speakers.

Next steps

Stream audio

Reduce latency by streaming audio as it generates rather than waiting for the complete file

Browse voices

Explore 10,000+ voices and swap the example voice ID for one that fits your use case

Clone a voice

Create a custom voice from a short audio recording

Login

Login

Community

Blog

Help Center

API Pricing

Sign up
