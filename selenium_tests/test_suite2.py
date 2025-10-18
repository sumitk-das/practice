import os
import glob
import pytest

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# Get all test files in the tests directory
test_files = glob.glob("tests/test_*.py")

# Filter out unwanted test files
filtered_test_files = [f for f in test_files if f != "tests/test_e2e_flow.py"]

# Set number of workers equal to number of test files
num_workers = len(filtered_test_files)

# Optional: Cap workers to available CPU cores
import multiprocessing
cpu_cores = multiprocessing.cpu_count()
if num_workers > cpu_cores:
    num_workers = cpu_cores

# Run all test files in one parallel pytest run
pytest.main([
    *filtered_test_files,
    "-n", str(num_workers),
    "--html=reports/report.html",
    "--self-contained-html",
    "--disable-warnings"  # Disable warning output
])