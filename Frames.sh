

for file in *.mp4; do ffmpeg -i "$file" $1"${file%.mp4}"%04d.png -vf -fps=1/$2 -hide_banner; done

# Parse videos and generate frames in a directory

