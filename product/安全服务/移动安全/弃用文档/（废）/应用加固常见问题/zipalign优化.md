## zipalign优化
Zipalign优化是对Apk文件进行存档对齐，确保所有的未压缩数据都从文件的开始位置以指定的对齐方式排列。尤其是.apk压缩包中的图片资源和未加工处理的相关文件，对齐的方式是以4字节对齐。

## zipalign优化有什么好处
Zipalign优化能够减少应用程序的RAM内存资源消耗。目前Google Play要求必须使用zipalign优化的安装包，其他应用市场暂无要求。

## 我是否需要选择zipalign优化
您可以结合实际情况来自主选择是否zipalign优化。通常除上架Google Play外，无需做zipalign优化。