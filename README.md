# 🎙️ Easy Audio to SRT

Easily convert audio files into SRT subtitles for free and using AI locally (no token required).

---

## Usage

```sh
# Transcribing audio files (Portuguese)
sh transcribe <file>.wav

# Translating srt files to English
sh translate <file>.srt
```

---

## Requirements

- [**Docker**](https://www.docker.com/get-started/)
- [**WSL**](https://learn.microsoft.com/pt-br/windows/wsl/install) (for **Windows** users)

> [!IMPORTANT]
>
> - The **Docker** image is pre-configured to use the largest **OpenAI** model available (turbo). For lighter models, check the [available models](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages) and change it in the [./Dockerfile](./Dockerfile) before executing the scripts.
> - Change the primary language (`pt`) in the [./docker-compose.yml](./docker-compose.yml) `transcribe` command.
> - Change the output translation language (`en`) in the [./translate_srt.py](./translate_srt.py) file.

---

## Links

- 📘 [**Whisper** (**OpenAI**) documentation](https://github.com/openai/whisper)
- 📘 [**Googletrans** documentation](https://github.com/ssut/py-googletrans)
