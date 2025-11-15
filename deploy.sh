#!/bin/bash

# GitHub에 랜딩페이지 업로드 스크립트

cd /Users/yonggeunkim/Documents/AIDP

echo "🚀 GitHub에 파일 업로드 시작..."

# Git 저장소 초기화 (이미 있으면 스킵)
if [ ! -d ".git" ]; then
    echo "📦 Git 저장소 초기화 중..."
    git init
fi

# 원격 저장소 설정
echo "🔗 원격 저장소 설정 중..."
git remote remove origin 2>/dev/null
git remote add origin git@github.com:kgk0429/mongsil.git

# 파일 추가
echo "📝 파일 추가 중..."
git add index.html styles.css script.js README.md .gitignore start_server.py

# 커밋
echo "💾 커밋 중..."
git commit -m "Initial commit: Add landing page for English kindergarten comparison service" || echo "⚠️  변경사항이 없거나 이미 커밋되었습니다."

# 브랜치 설정 및 푸시
echo "📤 GitHub에 푸시 중..."
git branch -M main
git push -u origin main

echo "✅ 완료! https://github.com/kgk0429/mongsil 에서 확인하세요."

