# PowerShell Script to Upload Files to GitHub (Handles Large Files)
# Run this script after creating your GitHub repository

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GitHub Upload Script for Large Files" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
try {
    $gitVersion = git --version
    Write-Host "[OK] Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "Step 1: Initialize Git repository..." -ForegroundColor Yellow
git init

Write-Host ""
Write-Host "Step 2: Adding all files..." -ForegroundColor Yellow
git add .

Write-Host ""
Write-Host "Step 3: Creating initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit - Trader Behavior Insights"

Write-Host ""
Write-Host "Step 4: Setting branch to main..." -ForegroundColor Yellow
git branch -M main

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Go to GitHub and create a new repository" -ForegroundColor White
Write-Host "2. Copy the repository URL (e.g., https://github.com/YOUR_USERNAME/trader-behavior-insights.git)" -ForegroundColor White
Write-Host "3. Run this command (replace with your URL):" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/trader-behavior-insights.git" -ForegroundColor Green
Write-Host "   git push -u origin main" -ForegroundColor Green
Write-Host ""
Write-Host "4. When asked for credentials:" -ForegroundColor White
Write-Host "   - Username: Your GitHub username" -ForegroundColor White
Write-Host "   - Password: Use a Personal Access Token (not your password)" -ForegroundColor White
Write-Host "   - Get token from: https://github.com/settings/tokens" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan

