from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
import torch
from models import build_model
import soundfile as sf
from pathlib import Path
import numpy
from io import BytesIO
from enum import Enum

# --- CONFIGURATIONS ---
MODEL_PATH = Path("kokoro-v1_0.pth").absolute()
VOICE_DIR = Path("voices")
SAMPLE_RATE = 24000
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

app = FastAPI()
kokoro_model= build_model(MODEL_PATH, DEVICE)

class KokoroVoice(str, Enum):
    af_alloy = "af_alloy"
    af_aoede = "af_aoede"
    af_bella = "af_bella"
    af_heart = "af_heart"
    af_jessica = "af_jessica"
    af_kore = "af_kore"
    af_nicole = "af_nicole"
    af_nova = "af_nova"
    af_river = "af_river"
    af_sarah = "af_sarah"
    af_sky = "af_sky"
    am_adam = "am_adam"
    am_echo = "am_echo"
    am_eric = "am_eric"
    am_fenrir = "am_fenrir"
    am_liam = "am_liam"
    am_michael = "am_michael"
    am_onyx = "am_onyx"
    am_puck = "am_puck"
    am_santa = "am_santa"
    bf_alice = "bf_alice"
    bf_emma = "bf_emma"
    bf_isabella = "bf_isabella"
    bf_lily = "bf_lily"
    bm_daniel = "bm_daniel"
    bm_fable = "bm_fable"
    bm_george = "bm_george"
    bm_lewis = "bm_lewis"
    ef_dora = "ef_dora"
    em_alex = "em_alex"
    em_santa = "em_santa"
    ff_siwis = "ff_siwis"
    hf_alpha = "hf_alpha"
    hf_beta = "hf_beta"
    hm_omega = "hm_omega"
    hm_psi = "hm_psi"
    if_sara = "if_sara"
    im_nicola = "im_nicola"
    jf_alpha = "jf_alpha"
    jf_gongitsune = "jf_gongitsune"
    jf_nezumi = "jf_nezumi"
    jf_tebukuro = "jf_tebukuro"
    jm_kumo = "jm_kumo"
    pf_dora = "pf_dora"
    pm_alex = "pm_alex"
    pm_santa = "pm_santa"
    zf_xiaobei = "zf_xiaobei"
    zf_xiaoni = "zf_xiaoni"
    zf_xiaoxiao = "zf_xiaoxiao"
    zf_xiaoyi = "zf_xiaoyi"
    zm_yunjian = "zm_yunjian"
    zm_yunxi = "zm_yunxi"
    zm_yunxia = "zm_yunxia"
    zm_yunyang = "zm_yunyang"

# 🗣️ Text-to-Speech Endpoint
@app.get("/tts")
def run_tts(text: str = Query(..., min_length=1, description="text to synthesize"),
                   voice: KokoroVoice = Query(..., description="Select a kokoro voice")
    ):
    voice_path =VOICE_DIR / f"{voice.value}.pt"
    generator = kokoro_model(text, voice=voice_path)

    audio_segments = []
    for _, _, audio in generator:
        if audio is not None:
            audio_tensor = audio if isinstance(audio, torch.Tensor) else torch.tensor(audio)
            audio_segments.append(audio_tensor)

    if not audio_segments:
        return  {"error": "No audio generated"}
        

    final_audio = torch.cat(audio_segments, dim=0).numpy()
    buffer = BytesIO()
    
    sf.write(buffer, final_audio, SAMPLE_RATE, format='WAV')
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="audio/wav")
