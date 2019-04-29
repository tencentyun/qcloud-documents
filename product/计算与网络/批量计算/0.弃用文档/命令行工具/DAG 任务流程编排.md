远程映射是 Batch 对存储使用相关的辅助功能，能够将 COS、CFS 等远程存储映射到本地的文件夹上

### 1. 前置准备
请根据 [前置准备](https://cloud.tencent.com/document/product/599/10548) 里的说明完成准备，并了解如何配置自定义信息里的通用部分。

### 2. 上传输入数据文件
number.txt 的内容如下
```
1
2
3
4
5
6
7
8
9
```

将文件上传到前置准备里创建的 input 文件夹里

![](https://mc.qcloudimg.com/static/img/02738c821f14ed132fef76c466c79d08/COS_5.png)

### 3. 查看和修改 Demo
使用编辑器打开 3_StoreMapping.py 文件
```
# custom (Change to your info)
imageId = "img-m4q71qnf"
Application = {
    "DeliveryForm": "PACKAGE",
    "Command": "python ./codepkg/countnum.py",
    "PackagePath": "http://batchdemo-1251783334.cosgz.myqcloud.com/codepkg/codepkg.tgz"
}
secretId_COS = "your secretId"
secretKey_COS = "your secretKey"
StdoutRedirectPath = "your cos path"
StderrRedirectPath = "your cos path"
InputMapping = {
    "SourcePath": "your input remote path",
    "DestinationPath": "/data/input/"
}
OutputMapping = {
    "SourcePath": "/data/output/",
    "DestinationPath": "your output remote path"
}
```
与 2_RemoteCodePkg.py 相比，自定义部分中修改如下
* Application 的 Command 改为执行 countnum.py 
* InputMapping：输入映射，SourcePath 远程存储地址（修改为前置准备里 input 文件夹的地址），DestinationPath 本地目录（暂不修改）
* OutputMapping 输出映射，SourcePath 本地目录（暂不修改），DestinationPath 远程存储地址（修改为前置准备里 output 文件夹的地址）

countnum.py 的内容如下
```
import os

inputfile = "/data/input/number.txt"
outputfile = "/data/output/result.txt"

def readFile(filename):
    total = 0
    fopen = open(filename, 'r')
    for eachLine in fopen:
        total += int(eachLine)
    fopen.close()
    print "total = ",total
    fwrite = open(outputfile, 'w')
    fwrite.write(str(total))
    fwrite.close()

print("Local input file is ",inputfile)
readFile(inputfile)
```
打开文件 input/number.txt，并把每一行的数字相加，然后把结果写到 output/Result.txt 里

### 4. 提交作业
Demo 里已经通过 Python脚本 + Batch 内测版本命令行工具的形式封装了提交作业流程，所以只需要按照下面的示例执行 Python 脚本即可
```
$ python 3_StoreMapping.py
{
    "Response": {
        "RequestId": "d069ce2f-abfc-451f-81fd-9327dbf5cf39",
        "JobId": "job-clump52n"
    }
}
```

如果返回 JobId 字段则代表提交成功，没有则检查返回值排查错误，也可以加入 [用户反馈](https://cloud.tencent.com/document/product/599/10806) 里的沟通群向管理员咨询。

### 5. 查看状态
参考 [1_简单开始](https://cloud.tencent.com/document/product/599/10551) 同名章节

### 6. 查看结果
Batch 会将输出数据从本地目录拷贝到远程存储目录，3_StoreMapping.py 的执行结果保存在了 result.txt 里，这个文件将自动同步到 COS 上
![pic](https://mc.qcloudimg.com/static/img/aee7138e589378eea48851dd1649b711/COS_6.png)
```
45
```
