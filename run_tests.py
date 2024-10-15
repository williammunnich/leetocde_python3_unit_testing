import os
import subprocess
import sys

# Define the path to the virtual environment
venv_path = os.path.join(os.getcwd(), 'myenv')

# Activate the virtual environment (for Unix/Mac)
activate_script = os.path.join(venv_path, 'bin', 'activate')

def activate_virtualenv():
    """
    Activate the virtual environment by sourcing the activation script.
    """
    if not os.path.exists(venv_path):
        print("Virtual environment not found. Please create a virtual environment first.")
        sys.exit(1)
    
    print("Activating virtual environment...")
    # Activating virtual environment on Unix/Mac using source
    os.system(f"source {activate_script}")
    print("Virtual environment activated.")

def check_and_install_requirements():
    """
    Check and install requirements from requirements.txt.
    """
    if os.path.exists('requirements.txt'):
        print("Installing requirements from requirements.txt...")
        # Install the requirements
        os.system(f"{os.path.join(venv_path, 'bin', 'pip')} install -r requirements.txt")
        print("Requirements installed.")
    else:
        print("No requirements.txt file found. Skipping dependency installation.")

def run_unit_tests(test_type):
    """
    Run the specified unit tests based on user input.
    """
    if test_type == '1':
        print("Running all tests with verbosity...")
        os.system(f"{os.path.join(venv_path, 'bin', 'python')} -m unittest -v unit_test.py")
    elif test_type == '2':
        print("Running all tests without verbosity...")
        os.system(f"{os.path.join(venv_path, 'bin', 'python')} -m unittest unit_test.py")
    elif test_type == '3':
        specific_test = input("Enter the specific test name (e.g., TestMathOperations.test_add): ")
        print(f"Running specific test: {specific_test}")
        os.system(f"{os.path.join(venv_path, 'bin', 'python')} -m unittest -v unit_test.{specific_test}")
    else:
        print("Invalid option selected.")

def main():
    # Step 1: Activate virtual environment
    activate_virtualenv()

    # Step 2: Check and install requirements
    check_and_install_requirements()

    # Step 3: Ask user what type of unit test to run
    print("\nWhat type of unit test would you like to run?")
    print("1. Run all tests with verbosity")
    print("2. Run all tests without verbosity")
    print("3. Run a specific test")

    test_type = input("Enter the number corresponding to your choice: ")

    # Step 4: Run the selected unit test
    run_unit_tests(test_type)

if __name__ == "__main__":
    main()
