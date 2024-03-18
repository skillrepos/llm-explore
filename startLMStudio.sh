wget https://releases.lmstudio.ai/linux/0.2.15/beta/LM_Studio-0.2.15-beta-1.AppImage
mv LM_Studio-0.2.15-beta-1.AppImage LM_Studio.AppImage
chmod +x LM_Studio.AppImage
docker compose up -d
chmod +x startLMStudio.sh
export DISPLAY=127.0.0.1:0
./LM_Studio.AppImage &
