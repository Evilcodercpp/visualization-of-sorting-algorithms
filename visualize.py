import matplotlib.pyplot as plt
import os

def read_steps(filename="data/steps.txt"):
    with open(filename) as f:
        steps = [list(map(int, line.split())) for line in f]
    return steps

def generate_frames(steps, outdir="frames"):
    os.makedirs(outdir, exist_ok=True)
    for i, step in enumerate(steps):
        plt.figure(figsize=(6,4))
        plt.bar(range(len(step)), step, color="skyblue")
        plt.title(f"Step {i}")
        plt.savefig(f"{outdir}/frame{i:04d}.png")
        plt.close()

if __name__ == "__main__":
    steps = read_steps()
    generate_frames(steps)
