#!/bin/bash

####################################################################################
## 本脚本的作用
# 根据 core 目录下的 markdown 文件核心，生成最终的 md 文件。



####################################################################################
## 渲染函数，输入为 core 目录下的原始文件路径，使用 tool/render.py 进行渲染
function doRender() {
	local srcFile=$1

	(
		echo "#!/usr/local/bin/python3"
		echo "# coding=utf-8"
		echo 
		cat $srcFile
		echo
		awk '/#REMOVE-CONTENT-BEFORE-HERE/{p=1}p' tool/render.py
	) | python3 -
}

## 获取 core 目录下的所有文件，并进行渲染
find core -name '*.md' | grep -v 'demo.md' | while read srcFile; do
	dstFile=$(sed -e 's/core\/\(.*\)$/\1/g' <<< $srcFile)
	
	echo "render $dstFile from $srcFile"
	mkdir -p $(dirname $dstFile)
	doRender $srcFile > $dstFile
done