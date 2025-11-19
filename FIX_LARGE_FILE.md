# 🔧 Fix: Large File Upload Issue

## Problem
`historical_data.csv` is **45.32 MB**, which exceeds GitHub's 25MB web upload limit.

## ✅ Solution Options

### **Option 1: Use Git Command Line (RECOMMENDED)** ⭐

Git command line can handle files up to 100MB, so this is the easiest solution!

#### Step 1: Install Git (if not installed)
1. Download: https://git-scm.com/download/win
2. Install with default settings
3. Restart your terminal

#### Step 2: Upload using Git
Open PowerShell or Command Prompt in your project folder and run:

```bash
# Navigate to your project
cd "C:\Users\olive\Desktop\crypto assign"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Trader Behavior Insights"

# Add your GitHub repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/trader-behavior-insights.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note**: You'll be asked for your GitHub username and password (use a Personal Access Token, not password)

---

### **Option 2: Use Git LFS (Large File Storage)**

For files over 100MB, use Git LFS:

```bash
# Install Git LFS
git lfs install

# Track CSV files
git lfs track "*.csv"

# Add files
git add .gitattributes
git add .
git commit -m "Initial commit with LFS"
git push -u origin main
```

---

### **Option 3: Compress the CSV File**

Create a compressed version:

```bash
# Create a zip file
Compress-Archive -Path historical_data.csv -DestinationPath historical_data.zip
```

Then upload the zip file and modify the code to unzip it.

---

### **Option 4: Sample the Data (Quick Fix)**

If you just need to demonstrate the app works, create a smaller sample:

```python
# Run this Python script to create a smaller sample
import pandas as pd

# Read the large file
df = pd.read_csv('historical_data.csv')

# Take a sample (e.g., 50,000 rows)
df_sample = df.sample(n=50000, random_state=42)

# Save smaller file
df_sample.to_csv('historical_data_sample.csv', index=False)
```

Then use `historical_data_sample.csv` instead.

---

### **Option 5: Load from URL (Advanced)**

Host the CSV file elsewhere (Google Drive, Dropbox, etc.) and load it in the app.

---

## 🎯 RECOMMENDED: Use Git Command Line

**This is the best solution because:**
- ✅ Handles files up to 100MB
- ✅ No file size reduction needed
- ✅ Professional approach
- ✅ Works with Streamlit Cloud

### Quick Git Setup Guide:

1. **Install Git**: https://git-scm.com/download/win
2. **Create GitHub Personal Access Token**:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select scope: `repo` (full control)
   - Copy the token

3. **Run these commands**:
```bash
cd "C:\Users\olive\Desktop\crypto assign"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/trader-behavior-insights.git
git push -u origin main
```

When asked for password, paste your **Personal Access Token** (not your GitHub password).

---

## 🚀 After Uploading

Once files are on GitHub:
1. Go to Streamlit Cloud: https://share.streamlit.io
2. Deploy your app
3. It will automatically have access to all files including the large CSV!

---

## Need Help?

If you get stuck, let me know which step you're on and I'll help!

