sudo apt update && sudo apt upgrade -y
sudo apt install fuse ffmpeg pciutils -y
wget https://releases.lmstudio.ai/linux/0.2.12/beta/LM_Studio-0.2.14-beta-1.AppImage
chmod +x LM_Studio-0.2.14-beta-1.AppImage
docker compose up -d
export DISPLAY=127.0.0.1:0
./LM_Studio-0.2.14-beta-1.AppImage
