p=`pwd`
echo "this path [$p] start exec"
git pull
git diff
git add ./
git commit -m "update time.py"
git push