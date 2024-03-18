sudo apt update && sudo apt upgrade -y
sudo apt install meson ninja-build ffmpeg fuse pciutils -y
wget https://github.com/libfuse/libfuse/releases/download/fuse-3.16.2/fuse-3.16.2.tar.gz
sudo tar xvf fuse-3.16.2.tar.gz
cd fuse-3.16.2
mkdir build
cd build
meson setup ..
sudo ninja install
sudo apt install libgconf-2-4 libatk1.0-0 libatk-bridge2.0-0 libgdk-pixbuf2.0-0 libgtk-3-0 libgbm-dev libnss3-dev libxss-dev libasound2 -y
cd /workspaces/llm-explore
rm -rf fuse-3.16.2
rm fuse-3.16.2.tar.gz
wget https://releases.lmstudio.ai/linux/0.2.15/beta/LM_Studio-0.2.15-beta-1.AppImage
mv LM_Studio-0.2.15-beta-1.AppImage LM_Studio.AppImage
chmod +x LM_Studio.AppImage
docker compose up -d
chmod +x startLMStudio.sh

