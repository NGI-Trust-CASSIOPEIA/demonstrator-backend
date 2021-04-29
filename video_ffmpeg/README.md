# Video FFMPEG

## Configurations - FFMPEG

Add the following lines on configuration file: `configuration.yaml`

```
ffmpeg:
  ffmpeg_bin: /usr/bin/ffmpeg
camera:
  - platform: ffmpeg
    name: camera
    input: rtsp://10.0.12.43:8554/camera

```

## Start stream

Run the following command: `ffmpeg -re -stream_loop -1 -i 17_04_2021_17h.mp4 -c copy -f rtsp rtsp://10.0.12.43:8554/camera`

Run in background: `ffmpeg -re -stream_loop -1 -i 17_04_2021_17h.mp4 -c copy -f rtsp rtsp://10.0.12.43:8554/camera </dev/null >/dev/null 2>/tmp/stream01.log &`

## Using VLC

Open vlc as network stream (media) on `udp://@10.0.12.43:1234`