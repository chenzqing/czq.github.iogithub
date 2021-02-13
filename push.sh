git rm ./cards/*
git commit -m "remove markdown"
git push
mkdir cards

python game.py
git add .
git commit -m "remove markdown"
git push