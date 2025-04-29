# Kokoro_TTS

A local implementation of the Kokoro Text-to-Speech model, featuring dynamic module loading, automatic dependency management, and a web interface.

## Features

- Local text-to-speech synthesis using the Kokoro-82M model
- Multiple voice support with easy voice selection (31 voices available)

## Prerequisites

- Python
- FFmpeg (optional, for MP3/AAC conversion)
- CUDA-compatible GPU (optional, for faster generation)
- Git (for version control and package management)

## Installation

1. Create a Python virtual environment:

```
python -m venv venv
.\venv\Scripts\activate
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
### Command Line Interface

Run the program:
```bash
python tts_kokoro.py
```

## Available Voices

The system includes 31 different voices across various categories:

### American English Voices
- Female (af_*):
  - af_alloy: Alloy - Clear and professional
  - af_aoede: Aoede - Smooth and melodic
  - af_bella: Bella - Warm and friendly
  - af_jessica: Jessica - Natural and engaging
  - af_kore: Kore - Bright and energetic
  - af_nicole: Nicole - Professional and articulate
  - af_nova: Nova - Modern and dynamic
  - af_river: River - Soft and flowing
  - af_sarah: Sarah - Casual and approachable
  - af_sky: Sky - Light and airy

- Male (am_*):
  - am_adam: Adam - Strong and confident
  - am_echo: Echo - Resonant and clear
  - am_eric: Eric - Professional and authoritative
  - am_fenrir: Fenrir - Deep and powerful
  - am_liam: Liam - Friendly and conversational
  - am_michael: Michael - Warm and trustworthy
  - am_onyx: Onyx - Rich and sophisticated
  - am_puck: Puck - Playful and energetic

### British English Voices
- Female (bf_*):
  - bf_alice: Alice - Refined and elegant
  - bf_emma: Emma - Warm and professional
  - bf_isabella: Isabella - Sophisticated and clear
  - bf_lily: Lily - Sweet and gentle

- Male (bm_*):
  - bm_daniel: Daniel - Polished and professional
  - bm_fable: Fable - Storytelling and engaging
  - bm_george: George - Classic British accent
  - bm_lewis: Lewis - Modern British accent

### Special Voices
- French Female (ff_*):
  - ff_siwis: Siwis - French accent

- High-pitched Voices:
  - Female (hf_*):
    - hf_alpha: Alpha - Higher female pitch
    - hf_beta: Beta - Alternative high female pitch
  - Male (hm_*):
    - hm_omega: Omega - Higher male pitch
    - hm_psi: Psi - Alternative high male pitch


## Model Information

The project uses the latest Kokoro model from Hugging Face:
- Repository: [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- Model file: `kokoro-v1_0.pth`
      (Download using `https://huggingface.co/hexgrad/Kokoro-82M/blob/main/kokoro-v1_0.pth` )
- Sample rate: 24kHz
- Voice files: Located in the `voices/` directory (downloaded automatically)
- Available voices: 31 voices across multiple categories
- Languages: American English ('a'), British English ('b')
- Model size: 82M parameters

