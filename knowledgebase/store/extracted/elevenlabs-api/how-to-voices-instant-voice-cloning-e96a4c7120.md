# Instant Voice Cloning quickstart | ElevenLabs Documentation

Source URL:

- https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/instant-voice-cloning

Dependency:

- ElevenLabs API

Collected at:

- 2026-04-15T19:44:34.232970+00:00

Direct links in scope:

- https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning
- https://elevenlabs.io/docs/eleven-api/concepts/voice-cloning
- https://elevenlabs.io/docs/eleven-api/quickstart
- https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/professional-voice-cloning
- https://elevenlabs.io/docs/overview/intro
- https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/instant-voice-cloning

Captured summary:

- Instant Voice Cloning quickstart | ElevenLabs Documentation This guide will show you how to create an Instant Voice Clone using the Clone Voice API.
- To create an Instant Voice Clone via the dashboard, refer to the Instant Voice Clone product guide.
- For an in-depth explanation of how IVC and PVC work under the hood and when to choose each, see Voice cloning: how it works .
- Using the Instant Voice Clone API This guide assumes you have set up your API key and SDK .
- Complete the quickstart first if you haven’t.

Extracted text:

Instant Voice Cloning quickstart | ElevenLabs Documentation

This guide will show you how to create an Instant Voice Clone using the Clone Voice API. To create an Instant Voice Clone via the dashboard, refer to the

Instant Voice Clone

product guide.

For an in-depth explanation of how IVC and PVC work under the hood and when to choose each, see

Voice cloning: how it works

.

Using the Instant Voice Clone API

This guide assumes you have

set up your API key and SDK

. Complete the quickstart first if you haven’t.

1

Make the API request

Create a new file named

example.py

or

example.mts

, depending on your language of choice and add the following code:

Python

TypeScript

1

# example.py

2

import os

3

from dotenv import load_dotenv

4

from elevenlabs.client import ElevenLabs

5

from io import BytesIO

6

7

load_dotenv()

8

9

elevenlabs = ElevenLabs(

10

api_key=os.getenv("ELEVENLABS_API_KEY"),

11

)

12

13

voice = elevenlabs.voices.ivc.create(

14

name="My Voice Clone",

15

# Replace with the paths to your audio files.

16

# The more files you add, the better the clone will be.

17

files=[BytesIO(open("/path/to/your/audio/file.mp3", "rb").read())]

18

)

19

20

print(voice.voice_id)

2

Execute the code

Python

TypeScript

1

python example.py

You should see the voice ID printed to the console.

Next steps

Professional voice cloning

Create a higher-quality clone by fine-tuning a model on your voice samples.

Voice cloning: how it works

Understand the technical differences between IVC and PVC and when to choose each.

Login

Login

Community

Blog

Help Center

API Pricing

Sign up
