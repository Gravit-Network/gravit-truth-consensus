import shutil
import subprocess


def main():
    if shutil.which("pdflatex") is None:
        raise RuntimeError(
            "pdflatex is not installed or not on PATH. "
            "Install a TeX distribution like texlive and retry."
        )

    subprocess.run(["python", "scripts/generate_figures.py"], check=True)
    subprocess.run(["pdflatex", "main.tex"], check=True)
    subprocess.run(["pdflatex", "main.tex"], check=True)


if __name__ == "__main__":
    main()
