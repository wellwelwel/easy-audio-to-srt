FROM python:3.10

WORKDIR /workspace

RUN apt-get update
RUN apt-get install -y ffmpeg
RUN pip install --upgrade pip
RUN pip install setuptools-rust
RUN pip install translate-toolkit
RUN pip install googletrans
RUN pip install -U openai-whisper
RUN python -c 'import whisper; whisper.load_model("turbo")'
