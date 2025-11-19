"""
Quick verification script to check if everything is ready for deployment
"""

import os
import sys

print("=" * 60)
print("DEPLOYMENT READINESS CHECK")
print("=" * 60)
print()

required_files = [
    'app.py',
    'sentiment_trader_analysis.py',
    'requirements.txt',
    'README.md',
    'fear_greed_index.csv',
    'historical_data.csv',
    '.gitignore'
]

optional_files = [
    'ANALYSIS_REPORT.md',
    'SUBMISSION_GUIDE.md',
    'DEPLOYMENT_GUIDE.md',
    'QUICK_START.md'
]

print("Checking required files...")
print("-" * 60)

all_good = True
for file in required_files:
    if os.path.exists(file):
        print(f"[OK] {file}")
    else:
        print(f"[MISSING] {file} - MISSING!")
        all_good = False

print()
print("Checking optional files...")
print("-" * 60)

for file in optional_files:
    if os.path.exists(file):
        print(f"[OK] {file}")
    else:
        print(f"[OPTIONAL] {file} - Optional, not required")

print()
print("Checking Python packages...")
print("-" * 60)

try:
    import streamlit
    print(f"[OK] streamlit ({streamlit.__version__})")
except ImportError:
    print("[MISSING] streamlit - NOT INSTALLED")
    all_good = False

try:
    import pandas
    print(f"[OK] pandas ({pandas.__version__})")
except ImportError:
    print("[MISSING] pandas - NOT INSTALLED")
    all_good = False

try:
    import numpy
    print(f"[OK] numpy ({numpy.__version__})")
except ImportError:
    print("[MISSING] numpy - NOT INSTALLED")
    all_good = False

try:
    import matplotlib
    print(f"[OK] matplotlib ({matplotlib.__version__})")
except ImportError:
    print("[MISSING] matplotlib - NOT INSTALLED")
    all_good = False

try:
    import seaborn
    print(f"[OK] seaborn ({seaborn.__version__})")
except ImportError:
    print("[MISSING] seaborn - NOT INSTALLED")
    all_good = False

print()
print("=" * 60)
if all_good:
    print("[SUCCESS] ALL CHECKS PASSED! You're ready to deploy!")
    print()
    print("Next steps:")
    print("1. Create GitHub repository")
    print("2. Upload all files")
    print("3. Deploy to Streamlit Cloud")
    print("4. See DEPLOYMENT_GUIDE.md for detailed steps")
else:
    print("[WARNING] SOME ISSUES FOUND - Please fix them before deploying")
    print()
    print("To install missing packages, run:")
    print("  pip install -r requirements.txt")
print("=" * 60)

