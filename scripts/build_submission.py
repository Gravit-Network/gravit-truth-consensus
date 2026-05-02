import os
import subprocess


def build():

    print("Generating figures...")
    subprocess.run(["python", "scripts/build_figures.py"])

    print("Compiling LaTeX...")
    subprocess.run(["pdflatex", "main.tex"])
    subprocess.run(["pdflatex", "main.tex"])


if __name__ == "__main__":
    build()
