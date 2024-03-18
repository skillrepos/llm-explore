sudo apt update && sudo apt upgrade -y
sudo apt install meson ninja-build ffmpeg fuse -y
wget https://github.com/libfuse/libfuse/releases/download/fuse-3.16.2/fuse-3.16.2.tar.gz
sudo tar xvf fuse-3.16.2.tar.gz
cd fuse-3.16.2
mkdir build
cd build
meson setup ..
sudo ninja install
sudo apt install libgconf-2-4 libatk1.0-0 libatk-bridge2.0-0 libgdk-pixbuf2.0-0 libgtk-3-0 libgbm-dev libnss3-dev libxss-dev libasound2 -y
wget https://releases.lmstudio.ai/linux/0.2.15/beta/LM_Studio-0.2.15-beta-1.AppImage
cd /workspaces/llm-explore
chmod +x LM_Studio-0.2.15-beta-1.AppImage
docker compose up -d
export DISPLAY=127.0.0.1:0
./LM_Studio-0.2.15-beta-1.AppImage

