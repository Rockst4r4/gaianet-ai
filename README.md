# What is GaiaNet
Gaianet: Decentralized AI Agent Infrastructure Gaianet is a decentralized computing infrastructure designed to democratize the creation and deployment of AI agents. It allows users to develop AI agents that reflect their individual styles, values, knowledge, and expertise, moving away from traditional AI services often tied to specific corporations.
# System requirements
The system requirements for running a Gaianet node can vary based on the specific AI models and configurations used. However, general guidelines are available:
## General System Requirements:

Multiple sources suggest the following as general minimum and recommended specifications:

Minimum Requirements:
CPU: 4 cores
RAM: 8 GB
Storage: While one source suggests 200 GB SSD, another indicates 10 GB may be sufficient for specific, smaller models (like the Qwen2 0.5B Instruct model).
Recommended Requirements:
CPU: 8 cores
GPU: High-performance VGA
RAM: 24 GB
Storage: 200 GB SSD
### I personally ran this node on servers with graphics(RTX 6000)

# Install Guide
I ran it with two models , so if you have vRam more than 12Gb so lets run it with ## gemma-1.1-7b-it model.
# One line command for gemma-1.1-7b-it
```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y python3-pip pip build-essential libssl-dev libffi-dev python3-dev && curl -sSfL 'https://github.com/GaiaNet-AI/gaianet-node/releases/download/0.4.28/install.sh' | bash && source /root/.bashrc && gaianet init --config https://raw.githubusercontent.com/GaiaNet-AI/node-configs/main/gemma-1.1-7b-it/config.json && gaianet start && gaianet info 
```
Then go to [gaianet Dashboard](https://gaianet.ai/reward?invite_code=RlgVgI) , signup , then go to [node settings](https://www.gaianet.ai/setting/nodes) then add your node by Connect New Node , Enter your Node ID and Device ID (shown you when you done with One-line Command) And join!
# Join A Domain:
Enter Following Code in your terminal:
```bash
gaianet stop
gaianet config --domain gaia.domains
gaianet init
gaianet start
```
Click the three dots next to your active node and select Join Domain.,Click on Next Step then use this domain: "https://sense.gaia.domains"
# Chat With your Node:
to chatwith your node, you need to go to [Reward Page](https://www.gaianet.ai/reward-summary) , Do all tasks and Redem it to GaiaCredit to able to chat with your node
# Set Up a Chatbod for automation procces:
## Download Script:
```bash
curl -L -o gaia2.py https://raw.githubusercontent.com/Rockst4r4/gaianet-ai/refs/heads/main/gaia2.py
```
```bash
screen -S gaia
```
```bash
pip3 install requests
python3 gaia2.py
```
### Take A API Key [here](https://www.gaianet.ai/setting/gaia-api-keys) and paste it when it needed! when running command python3 gaia2.py
# HAVE FUN! 
Just everyday go to reward-summary page and redeme userpoints to gaianode to be able to chat with your node!
____________________________________________
# If you have Lower System or Without VGA:
It reccomended to run with Qwen2-0.5B-Instruct Model
# One-Line Command to run With Qwen2-0.5B Model!
```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y python3-pip pip build-essential libssl-dev libffi-dev python3-dev && curl -sSfL 'https://github.com/GaiaNet-AI/gaianet-node/releases/latest/download/install.sh' | bash && source /root/.bashrc && gaianet init --config https://raw.githubusercontent.com/GaiaNet-AI/node-configs/main/qwen2-0.5b-instruct/config.json
 && gaianet start && gaianet info
```
## then add your node exactly looks like previous Steps! and Add a Domain with qwen2-0.5b-instruct Models
# Chat with your own Node using bot
```
curl -L -o gaia1.py https://raw.githubusercontent.com/Rockst4r4/gaianet-ai/refs/heads/main/gaia2.py
```
### open screen
```
screen -S gaia
```
```
pip3 install requests
python3 gaia1.py
```
### Take A API Key [here](https://www.gaianet.ai/setting/gaia-api-keys) and paste it when it needed! when running command python3 gaia2.py
# HAVE FUN! 
Just everyday go to reward-summary page and redeme userpoints to gaianode to be able to chat with your node!

____________________________________________

# Lets Farm :) Im creating new Documents for farming this!




