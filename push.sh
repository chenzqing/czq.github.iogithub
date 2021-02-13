git rm ./cards/*
mkdir cards
git add .
git commit -m "remove markdown"
git push

python game.py
git add .
git commit -m "remove markdown"
git push