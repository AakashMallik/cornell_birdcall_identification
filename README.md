# Cornell Birdcall Identification 🐦

<img src="./docs/img/header.png">
Competition Link : https://www.kaggle.com/c/birdsong-recognition/

## Setup
```
apt-get update
apt-get install libgtk2.0-dev
apt-get install libsndfile1

pip install --upgrade torch torchvision
pip install --user wandb easydict blessed tensorboard pandas sklearn matplotlib seaborn pretrainedmodels efficientnet_pytorch transformers albumentations librosa inquirer


git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```

## Bashrc update
Add this at the end of **.bashrc**

```
export PATH="$PATH:/root/.local/bin"
```

## Login
```
wandb login
```
