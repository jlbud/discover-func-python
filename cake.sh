p=`pwd`
echo "this path [$p] start exec"
git pull
git diff
git exit
git add ./
git commit -m "update flask web"
git push