import subprocess
import sys

def run(script):
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

def main():
    print("🚀 Starting Data Pipeline\n")
    run("load_raw_data.py")
    run("preprocess_data.py")
    run("load_clean_data.py")
    run("analysis.py")
    print("\n✅ Pipeline Finished Successfully")

if __name__ == "__main__":
    main()
