# Introduction | ElevenLabs Documentation | CloudRaven Enrichment

Source URL:

- https://elevenlabs.io/docs/api-reference/introduction

Dependency:

- ElevenLabs API

Collection scope:

- Collect voice and API entry points only.

What this page is useful for:

- Introduction | ElevenLabs Documentation Installation You can interact with the API through HTTP or Websocket requests from any language, via our official Python bindings or our official Node.js libraries.
- To install the official Python bindings, run the following command: $ pip install elevenlabs To install the official Node.js library, run the following command in your Node.js project directory: $ npm install @elevenlabs/elevenlabs-js Tracking generation costs Access response headers to retrieve generation metadata including character costs.
- Python JavaScript 1 from elevenlabs.client import ElevenLabs 2 3 client = ElevenLabs(api_key="your_api_key") 4 5 # Get raw response with headers 6 response = client.text_to_speech.with_raw_response.convert( 7 text="Hello, world!", 8 voice_id="voice_id" 9 ) 10 11 # Access character cost from headers 12 char_cost = response.headers.get("x-character-count") 13 request_id = response.headers.get("request-id") 14 audio_data = response.data The raw response provides access to: Response data - The actual API response content HTTP headers - Metadata including character costs and request IDs Login Login Community Blog Help Center API Pricing Sign up

CloudRaven applicability:

- Use this material when a CloudRaven workflow needs speech output, narrated artifacts, or voice-first assistance.

Prototype-to-production review:

- Best fit when voice adds utility, not just novelty.
- Review permissions, latency, and transcript handling before production use.

CloudRaven example paths:

- Generate narrated summaries for marketing or knowledge artifacts.
- Prototype a voice-enabled support or intake experience.

Suggested retrieval tags:

- `voice`
- `audio`
- `speech`

Local artifact references:

- Extracted page: `knowledgebase/store/extracted/elevenlabs-api/docs-api-reference-introduction-c6790d59c8.md`
- Raw HTML: `knowledgebase/store/raw_html/elevenlabs-api/docs-api-reference-introduction-c6790d59c8.html`
