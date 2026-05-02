import subprocess


def main():
    subprocess.run(["python", "scripts/generate_figures.py"], check=True)
    subprocess.run(["pdflatex", "main.tex"], check=True)
    subprocess.run(["pdflatex", "main.tex"], check=True)


if __name__ == "__main__":
    main()
