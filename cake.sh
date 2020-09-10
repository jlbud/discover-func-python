p=`pwd`
echo "this path [$p] start exec"
git pull
git add ./
git commit -m "add cake.sh"
git push
