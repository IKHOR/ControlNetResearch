Checkout the original ControlNet repo [here](https://github.com/lllyasviel/ControlNet/tree/main)!

## Initial set up

1. Open runpod with template: runpod/pytorch:2.0.1-py3.10-cuda11.8.0-devel 
    1. MAKE SURE to set container disk to at least 40-50 GB
2. Git clone in this ControlNetResearch repo 
3. Install Anaconda to create conda environment necessary to run ControlNet modules
    1. `wget https://repo.anaconda.com/archive/Anaconda3-2023.07-2-Linux-x86_64.sh`
    2. `bash Anaconda3-2023.07-2-Linux-x86_64.sh`
    3. `source ~/.bashrc`
4. Set up conda environment
    1. `conda env create -f environment.yaml`
    2. `conda activate control`
5. Run this to install the rest of the dependencies
    1. `pip install -r requirements.txt` 
    2. `apt update`
    3. `apt install libjpeg-dev libpng-dev`
    4. install whatever remaining dependencies come up 
    

## ControlNet Training

Follow this [tutorial](https://github.com/lllyasviel/ControlNet/blob/main/docs/train.md).
