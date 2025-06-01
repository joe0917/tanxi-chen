#!/bin/bash
set -e
git init
git add .
git commit -m"修改更新"
git push origin master 
echo "Done!"
