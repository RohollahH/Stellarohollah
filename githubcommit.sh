#!/bin/bash

#cd linuxopg
git add *
git config --global user.email ""
git config --global user.name ""
echo Navn til commiten?
read commit
git commit -m $commit
git push
