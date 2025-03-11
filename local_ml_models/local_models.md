download tookit to run model on nvidia GPU

CUDA version by running nvcc --version in your terminal.
check the driver version by running nvidia-smi

Command for Enabling GPU below: for cuda 12.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

Running model locally with ollama
ollama run llama2
ollama serve - to exponse http port

Cutomize llama model using Modelfile
ollama create mario -f ./Modelfile



