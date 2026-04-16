# Streaming text to speech | ElevenLabs Documentation

Source URL:

- https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming

Dependency:

- ElevenLabs API

Collected at:

- 2026-04-15T19:44:33.445092+00:00

Direct links in scope:

- https://elevenlabs.io/docs/eleven-api/quickstart
- https://elevenlabs.io/docs/eleven-api/concepts/audio-streaming
- https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts
- https://elevenlabs.io/docs/eleven-api/concepts/latency
- https://elevenlabs.io/docs/overview/intro
- https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/streaming

Captured summary:

- Streaming text to speech | ElevenLabs Documentation This guide covers three approaches: generating speech as a file, streaming the audio response directly, and optionally uploading generated audio to an AWS S3 bucket to share via a signed URL.
- This guide assumes you have set up your API key and SDK .
- Complete the quickstart first if you haven’t.
- The optional S3 upload section also requires an AWS account with access to S3.
- Curious why streaming works the way it does?

Extracted text:

Streaming text to speech | ElevenLabs Documentation

This guide covers three approaches: generating speech as a file, streaming the audio response directly, and optionally uploading generated audio to an AWS S3 bucket to share via a signed URL.

This guide assumes you have

set up your API key and SDK

. Complete the quickstart first if you haven’t. The optional S3 upload section also requires an AWS account with access to S3.

Curious why streaming works the way it does?

Understanding audio streaming

explains the protocol, buffering, and latency tradeoffs in depth.

Convert text to speech (file)

To convert text to speech and save it as a file, we’ll use the

convert

method of the ElevenLabs SDK and then it locally as a

.mp3

file.

Python

TypeScript

1

import os

2

import uuid

3

from dotenv import load_dotenv

4

from elevenlabs import VoiceSettings

5

from elevenlabs.client import ElevenLabs

6

7

load_dotenv()

8

9

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

10

elevenlabs = ElevenLabs(

11

api_key=ELEVENLABS_API_KEY,

12

)

13

14

15

def text_to_speech_file(text: str) -> str:

16

# Calling the text_to_speech conversion API with detailed parameters

17

response = elevenlabs.text_to_speech.convert(

18

voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice

19

output_format="mp3_22050_32",

20

text=text,

21

model_id="eleven_flash_v2_5", # use the flash model for low latency

22

# Optional voice settings that allow you to customize the output

23

voice_settings=VoiceSettings(

24

stability=0.0,

25

similarity_boost=1.0,

26

style=0.0,

27

use_speaker_boost=True,

28

speed=1.0,

29

),

30

)

31

32

# uncomment the line below to play the audio back

33

# play(response)

34

35

# Generating a unique file name for the output MP3 file

36

save_file_path = f"{uuid.uuid4()}.mp3"

37

38

# Writing the audio to a file

39

with open(save_file_path, "wb") as f:

40

for chunk in response:

41

if chunk:

42

f.write(chunk)

43

44

print(f"{save_file_path}: A new audio file was saved successfully!")

45

46

# Return the path of the saved audio file

47

return save_file_path

You can then run this function with:

Python

TypeScript

1

text_to_speech_file("Hello World")

Convert text to speech (streaming)

If you prefer to stream the audio directly without saving it to a file, you can use our streaming feature.

Python

TypeScript

1

import os

2

from typing import IO

3

from io import BytesIO

4

from dotenv import load_dotenv

5

from elevenlabs import VoiceSettings

6

from elevenlabs.client import ElevenLabs

7

8

load_dotenv()

9

10

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

11

elevenlabs = ElevenLabs(

12

api_key=ELEVENLABS_API_KEY,

13

)

14

15

16

def text_to_speech_stream(text: str) -> IO[bytes]:

17

# Perform the text-to-speech conversion

18

response = elevenlabs.text_to_speech.stream(

19

voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice

20

output_format="mp3_22050_32",

21

text=text,

22

model_id="eleven_multilingual_v2",

23

# Optional voice settings that allow you to customize the output

24

voice_settings=VoiceSettings(

25

stability=0.0,

26

similarity_boost=1.0,

27

style=0.0,

28

use_speaker_boost=True,

29

speed=1.0,

30

),

31

)

32

33

# Create a BytesIO object to hold the audio data in memory

34

audio_stream = BytesIO()

35

36

# Write each chunk of audio data to the stream

37

for chunk in response:

38

if chunk:

39

audio_stream.write(chunk)

40

41

# Reset stream position to the beginning

42

audio_stream.seek(0)

43

44

# Return the stream for further use

45

return audio_stream

You can then run this function with:

Python

TypeScript

1

text_to_speech_stream("This is James")

Bonus - Uploading to AWS S3 and getting a secure sharing link

Once your audio data is created as either a file or a stream you might want to share this with your users. One way to do this is to upload it to an AWS S3 bucket and generate a secure sharing link.

Creating your AWS credentials

To upload the data to S3 you’ll need to add your AWS access key ID, secret access key and AWS region name to your

.env

file. Follow these steps to find the credentials:

Log in to your AWS Management Console: Navigate to the AWS home page and sign in with your account.

AWS Console Login

Access the IAM (Identity and Access Management) Dashboard: You can find IAM under “Security, Identity, & Compliance” on the services menu. The IAM dashboard manages access to your AWS services securely.

AWS IAM Dashboard

Create a New User (if necessary): On the IAM dashboard, select “Users” and then “Add user”. Enter a user name.

Add AWS IAM User

Set the permissions: attach policies directly to the user according to the access level you wish to grant. For S3 uploads, you can use the AmazonS3FullAccess policy. However, it’s best practice to grant least privilege, or the minimal permissions necessary to perform a task. You might want to create a custom policy that specifically allows only the necessary actions on your S3 bucket.

Set Permission for AWS IAM User

Review and create the user: Review your settings and create the user. Upon creation, you’ll be presented with an access key ID and a secret access key. Be sure to download and securely save these credentials; the secret access key cannot be retrieved again after this step.

AWS Access Secret Key

Get AWS region name: ex. us-east-1

AWS Region Name

If you do not have an AWS S3 bucket, you will need to create a new one by following these steps:

Access the S3 dashboard: You can find S3 under “Storage” on the services menu.

AWS S3 Dashboard

Create a new bucket: On the S3 dashboard, click the “Create bucket” button.

Click Create Bucket Button

Enter a bucket name and click on the “Create bucket” button. You can leave the other bucket options as default. The newly added bucket will appear in the list.

Enter a New S3 Bucket Name

S3 Bucket List

Installing the AWS SDK and adding the credentials

Install

boto3

for interacting with AWS services using

pip

and

npm

.

Python

TypeScript

$

pip install boto3

Then add the environment variables to

.env

file like so:

AWS_ACCESS_KEY_ID=your_aws_access_key_id_here

AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key_here

AWS_REGION_NAME=your_aws_region_name_here

AWS_S3_BUCKET_NAME=your_s3_bucket_name_here

Uploading to AWS S3 and generating the signed URL

Add the following functions to upload the audio stream to S3 and generate a signed URL.

s3_uploader.py (Python)

s3_uploader.ts (TypeScript)

1

import os

2

import boto3

3

import uuid

4

5

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")

6

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

7

AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")

8

AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")

9

10

session = boto3.Session(

11

aws_access_key_id=AWS_ACCESS_KEY_ID,

12

aws_secret_access_key=AWS_SECRET_ACCESS_KEY,

13

region_name=AWS_REGION_NAME,

14

)

15

s3 = session.client("s3")

16

17

18

def generate_presigned_url(s3_file_name: str) -> str:

19

signed_url = s3.generate_presigned_url(

20

"get_object",

21

Params={"Bucket": AWS_S3_BUCKET_NAME, "Key": s3_file_name},

22

ExpiresIn=3600,

23

) # URL expires in 1 hour

24

return signed_url

25

26

27

def upload_audiostream_to_s3(audio_stream) -> str:

28

s3_file_name = f"{uuid.uuid4()}.mp3" # Generates a unique file name using UUID

29

s3.upload_fileobj(audio_stream, AWS_S3_BUCKET_NAME, s3_file_name)

30

31

return s3_file_name

You can then call uploading function with the audio stream from the text.

Python

TypeScript

1

s3_file_name = upload_audiostream_to_s3(audio_stream)

After uploading the audio file to S3, generate a signed URL to share access to the file. This URL will be time-limited, meaning it will expire after a certain period, making it secure for temporary sharing.

You can now generate a URL from a file with:

Python

TypeScript

1

signed_url = generate_presigned_url(s3_file_name)

2

print(f"Signed URL to access the file: {signed_url}")

If you want to use the file multiple times, you should store the s3 file path in your database and then regenerate the signed URL each time you need rather than saving the signed URL directly as it will expire.

Putting it all together

To put it all together, you can use the following script:

main.py (Python)

index.ts (Typescript)

1

import os

2

3

from dotenv import load_dotenv

4

5

load_dotenv()

6

7

from text_to_speech_stream import text_to_speech_stream

8

from s3_uploader import upload_audiostream_to_s3, generate_presigned_url

9

10

11

def main():

12

text = "This is James"

13

14

audio_stream = text_to_speech_stream(text)

15

s3_file_name = upload_audiostream_to_s3(audio_stream)

16

signed_url = generate_presigned_url(s3_file_name)

17

18

print(f"Signed URL to access the file: {signed_url}")

19

20

21

if __name__ == "__main__":

22

main()

Conclusion

You now know how to convert text into speech and generate a signed URL to share the audio file. This functionality opens up numerous opportunities for creating and sharing content dynamically.

Here are some examples of what you could build with this.

Educational Podcasts

: Create personalized educational content that can be accessed by students on demand. Teachers can convert their lessons into audio format, upload them to S3, and share the links with students for a more engaging learning experience outside the traditional classroom setting.

Accessibility Features for Websites

: Enhance website accessibility by offering text content in audio format. This can make information on websites more accessible to individuals with visual impairments or those who prefer auditory learning.

Automated Customer Support Messages

: Produce automated and personalized audio messages for customer support, such as FAQs or order updates. This can provide a more engaging customer experience compared to traditional text emails.

Audio Books and Narration

: Convert entire books or short stories into audio format, offering a new way for audiences to enjoy literature. Authors and publishers can diversify their content offerings and reach audiences who prefer listening over reading.

Language Learning Tools

: Develop language learning aids that provide learners with audio lessons and exercises. This makes it possible to practice pronunciation and listening skills in a targeted way.

Next steps

WebSocket streaming

Use WebSockets to stream text to speech in real time as it is generated by an LLM.

Understanding latency

Learn what contributes to latency and how to minimise time-to-first-audio.

Login

Login

Community

Blog

Help Center

API Pricing

Sign up
