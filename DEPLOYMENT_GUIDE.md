# 🚀 Deployment Guide - Streamlit App

## Option 1: Streamlit Cloud (FREE & EASIEST) ⭐ Recommended

### Step 1: Create GitHub Account (if you don't have one)
1. Go to https://github.com
2. Sign up for a free account
3. Verify your email

### Step 2: Create GitHub Repository
1. Click the **"+"** icon in top right → **"New repository"**
2. Repository name: `trader-behavior-insights` (or any name you like)
3. Description: `Bitcoin Market Sentiment vs Trader Performance Analysis`
4. Make it **Public** (required for free Streamlit Cloud)
5. **DO NOT** initialize with README (we already have files)
6. Click **"Create repository"**

### Step 3: Upload Files to GitHub

**Option A: Using GitHub Web Interface**
1. In your new repository, click **"uploading an existing file"**
2. Drag and drop ALL these files:
   - `app.py`
   - `sentiment_trader_analysis.py`
   - `requirements.txt`
   - `README.md`
   - `ANALYSIS_REPORT.md`
   - `fear_greed_index.csv`
   - `historical_data.csv`
   - `.gitignore`
3. Scroll down, add commit message: "Initial commit - Trader Behavior Insights"
4. Click **"Commit changes"**

**Option B: Using Git Command Line** (if you have Git installed)
```bash
# Navigate to your project folder
cd "C:\Users\olive\Desktop\crypto assign"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Trader Behavior Insights"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/trader-behavior-insights.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 4: Deploy to Streamlit Cloud
1. Go to https://share.streamlit.io
2. Click **"Sign in"** → Sign in with **GitHub**
3. Click **"New app"**
4. Fill in:
   - **Repository**: Select your repository (`trader-behavior-insights`)
   - **Branch**: `main` (or `master`)
   - **Main file path**: `app.py`
   - **App URL**: Will be auto-generated (e.g., `your-app-name.streamlit.app`)
5. Click **"Deploy"**
6. Wait 1-2 minutes for deployment
7. Your app will be live! 🎉

### Step 5: Share Your App
- Your app URL will be: `https://your-app-name.streamlit.app`
- Share this link in your email submission!

---

## Option 2: Heroku (Alternative)

### Prerequisites
1. Heroku account: https://heroku.com
2. Heroku CLI installed: https://devcenter.heroku.com/articles/heroku-cli

### Steps
1. Create `Procfile` (I'll create this for you)
2. Create `setup.sh` (I'll create this for you)
3. Login to Heroku: `heroku login`
4. Create app: `heroku create your-app-name`
5. Deploy: `git push heroku main`

---

## Option 3: Local Demo (No Deployment)

If you can't deploy, you can:
1. Record a screen capture video of the app running
2. Upload to YouTube (unlisted) or Loom
3. Share the video link in your email

---

## Quick Checklist

- [ ] GitHub account created
- [ ] Repository created
- [ ] All files uploaded to GitHub
- [ ] Streamlit Cloud account created
- [ ] App deployed on Streamlit Cloud
- [ ] App URL obtained
- [ ] Tested the live app
- [ ] Ready to share in email!

---

## Troubleshooting

### If deployment fails:
1. Check that `requirements.txt` has all dependencies
2. Ensure `app.py` is in the root directory
3. Check that data files (`*.csv`) are included
4. Look at deployment logs in Streamlit Cloud

### If app doesn't load:
1. Check the logs in Streamlit Cloud dashboard
2. Ensure all CSV files are in the repository
3. Verify Python version compatibility

---

## Need Help?

If you get stuck at any step, let me know and I'll help you troubleshoot!

