from subprocess import run, PIPE
import sys
import platform


def run_c_version():
    print("Running C version...")
    # Get GCC version
    gcc_version = run(["gcc", "--version"], stdout=PIPE, text=True).stdout.splitlines()[
        0
    ]
    print(f"GCC Version: {gcc_version}")

    # Compile the C code
    run(["gcc", "c_version.c", "-o", "c_version"])

    # Run the C code
    run(["./c_version"])

    # Remove the compiled C code
    run(["rm", "c_version"])


def run_python_version():
    print("Running Python version...")
    # Get Python version
    python_version = sys.version.replace("\n", " ")
    print(f"Python Version: {python_version}")

    # Run the Python code
    run(["python3", "python_version.py"])


if __name__ == "__main__":
    # Print system information
    print(f"Operating System: {platform.platform()}")

    run_c_version()
    print("\n\n")
    run_python_version()
