# scripts/build_paper.py

import subprocess


def build():

    subprocess.run(["python", "scripts/sync_figures.py"])
    subprocess.run(["pdflatex", "main.tex"])
    subprocess.run(["pdflatex", "main.tex"])  # resolve refs


if __name__ == "__main__":
    build()
