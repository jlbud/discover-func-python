p=`pwd`
echo "this path [$p] start exec"
git pull
git add ./
git commit -m "update cake.sh"
git push
exit