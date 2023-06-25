### Ubuntu 20.04
- Choose this Linux version when creating your EC2 instance.

### CUDA 11.8
- This is the latest CUDA version that Pytorch support.
> See the [Pytorch Install Guide](https://pytorch.org/get-started/locally/)
- Follow [this](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_network) to add nvidia apt repository.
- `apt install cuda=11.8.0-1`

### cuDNN
- Download a `*.deb` file from [here](https://developer.nvidia.com/rdp/cudnn-download).
- You need to sign up Nvidia Developer account and choose the correct version, for `CUDA 11.8` and `Ubuntu 20.04`.
- Use `scp` to upload the `deb` file on EC2. And run `deb -i cudnn-local-repo-ubuntu2004-8.9.2.26_1.0-1_amd64.deb` to install it.

### Pytorch
- Install [Mamba](https://mamba.readthedocs.io/en/latest/installation.html) and create a Conda virtual environment.
- Install Pytorch with [this instructions](https://pytorch.org/get-started/locally/), choosing correct options then it gives you this command to run `conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia`

### Verify Installation
- Run `minimum_cnn_inference.py` and it should output the following if eveything is good:
```
TODO
```
