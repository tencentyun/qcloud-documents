#!/bin/bash

####################################################################################
## 本脚本的作用
# 根据 core 目录下的 markdown 文档核心，生成最终的客户端 API 文档。



####################################################################################
## 渲染文档，输入为 core 目录下的原始文件路径，使用 tool/render.py 进行渲染
function renderOneDoc() {
	local srcFile=$1

	(
		echo "#!/usr/local/bin/python3"
		echo "# coding=utf-8"
		echo 
		cat $srcFile
		echo
		awk '/^#REMOVE-CONTENT-BEFORE-HERE/{p=1}p' tool/render.py
	) | python3 - | grep -v '^## TO-BE-DEL:'
}

## 渲染一个数据结构
function renderOneDataStructure() {
  local name=$1
  
  echo "### $name[](id:$name)"
  cat "core-data-structure/$name.md" | grep -v '^;'
  echo
  echo
}

## 渲染文档
function renderDoc() {
  ## 获取 core 目录下的所有文件，并进行渲染
  find core -name '*.md' | grep -v 'demo.md' | while read srcFile; do
    dstFile=$(sed -e 's/core\/\(.*\)$/\1/g' <<< $srcFile)
    
    echo "render $dstFile from $srcFile"
    mkdir -p $(dirname $dstFile)
    renderOneDoc $srcFile > $dstFile
  done
}

## 渲染数据结构
function renderDataStructure () {
  echo "render data structure"

  find core-data-structure -name '*.md' \
    | grep -v 'demo.md' \
    | sed -e 's/^core-data-structure\/\(.*\)\.md/\1/g' \
    | sort \
    | while read name; do
      echo "<!-- 注意：本文档由 gen_client_api_from_core.sh 脚本自动生成，请勿手工修改 -->"
      echo "<!--     如有修改需求，请阅读 readme.md -->"
      renderOneDataStructure $name
    done > 数据结构.md
}

cd $(dirname $0)

renderDoc
renderDataStructure