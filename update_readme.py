import subprocess
import sys
from datetime import datetime

def run_tests():
    try:
        fechaHora = datetime.now()
        subprocess.check_call([sys.executable, "-m", "pytest", "-q", "-v"])
        return f"✅ {fechaHora} - Tests correctos"
    except subprocess.CalledProcessError:
        fechaHora = datetime.now()
        return f"❌ {fechaHora} - Tests fallidos"

def update_readme(status: str):
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines.append(status + "\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

def update_reportmd(lines):
    with open("report.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
    new_lines.append(status + "\n")

    with open("report.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
    update_reportmd(status)