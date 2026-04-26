#!/usr/bin/env python3
import subprocess
from datetime import datetime

def get_twitch_m3u8(channel):
    try:
        result = subprocess.run(
            ['yt-dlp', '-g', f'https://www.twitch.tv/{channel}'],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        return None
    except:
        return None

def generate_m3u():
    with open('channels.txt', 'r') as f:
        channels = [line.strip() for line in f if line.strip()]
    
    playlist = ["#EXTM3U", f"# Aggiornato: {datetime.now()}"]
    
    for channel in channels:
        print(f"📺 Elaboro: {channel}")
        url = get_twitch_m3u8(channel)
        if url:
            playlist.append(f"#EXTINF:-1, ✅ {channel} (Twitch)")
            playlist.append(url)
        else:
            playlist.append(f"#EXTINF:-1, ❌ OFFLINE - {channel}")
            playlist.append("#OFFLINE")
    
    with open('playlist.m3u', 'w') as f:
        f.write('\n'.join(playlist))
    print("✅ Playlist creata!")

if __name__ == "__main__":
    generate_m3u()
