import subprocess


def main():
    subprocess.run(["python", "scripts/generate_figures.py"])
    subprocess.run(["pdflatex", "main.tex"])
    subprocess.run(["pdflatex", "main.tex"])


if __name__ == "__main__":
    main()
