# ⚡ Quick Deploy - 5 Minutes!

## Fastest Way to Deploy (Streamlit Cloud)

### Step 1: Create GitHub Repo (2 minutes)
1. Go to https://github.com/new
2. Name: `trader-insights` (or any name)
3. Make it **Public**
4. Click **Create repository**

### Step 2: Upload Files (2 minutes)
**Easiest way - use GitHub web:**
1. In your new repo, click **"uploading an existing file"**
2. Drag ALL these files:
   ```
   app.py
   sentiment_trader_analysis.py
   requirements.txt
   README.md
   fear_greed_index.csv
   historical_data.csv
   .gitignore
   ```
3. Click **"Commit changes"**

### Step 3: Deploy (1 minute)
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click **"New app"**
4. Select your repo
5. Main file: `app.py`
6. Click **"Deploy"**
7. Wait 1 minute
8. **DONE!** 🎉

### Step 4: Get Your Link
Your app will be at: `https://your-app-name.streamlit.app`

**That's it! Share this link in your email!**

---

## Need Help?

Run this to check if everything is ready:
```bash
python verify_setup.py
```

See `DEPLOYMENT_GUIDE.md` for detailed instructions.

