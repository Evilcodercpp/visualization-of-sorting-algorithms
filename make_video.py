import os
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

def make_video(frames_dir="frames", output="sort.mp4", fps=10):
    frames = [os.path.join(frames_dir, f) for f in sorted(os.listdir(frames_dir)) if f.endswith(".png")]
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(output, codec="libx264")

if __name__ == "__main__":
    make_video()
