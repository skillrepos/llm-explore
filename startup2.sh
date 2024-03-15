sudo apt update && sudo apt upgrade -y
sudo apt install fuse ffmpeg pciutils -y
wget https://github.com/janhq/jan/releases/download/v0.4.7/jan-linux-x86_64-0.4.7.AppImage 
chmod +x jan-linux-x86_64-0.4.7.AppImage
docker compose up -d
export DISPLAY=127.0.0.1:0
./jan-linux-x86_64-0.4.7.AppImage
