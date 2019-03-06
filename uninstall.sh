pip3 uninstall ltdict
git rm -r dist
git rm -r build
git rm -r ltdict.egg-info
rm -r dist
rm -r build
rm -r ltdict.egg-info
git add .
git commit -m "remove old build"

