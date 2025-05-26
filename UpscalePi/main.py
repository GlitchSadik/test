# main.py
import subprocess
import sys

def run_script(script_path):
    print(f"Running {script_path} ...")
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error in {script_path}:\n{result.stderr}")
        sys.exit(1)  # Stop everything if an error occurs

def main():
    scripts_in_order = [
        'scripts/load_docs.py',
        'scripts/chunk_docs.py',
        'scripts/embed_docs.py',
        'scripts/query_agent.py'  # Replace with your real script names
    ]

    for script in scripts_in_order:
        run_script(script)

if __name__ == "__main__":
    main()
