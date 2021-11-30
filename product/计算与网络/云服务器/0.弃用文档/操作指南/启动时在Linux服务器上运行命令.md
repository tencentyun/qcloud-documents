## 1. 启动时在Linux服务器上运行命令

当您在腾讯云上创建Linux时，可以选择将用户的数据以文本的方式传递到服务器里面。当您传递的文本是一个标准 Shell 格式的脚本时，该脚本将在服务器首次启动的时候被执行。您可以把您想要传递的文本信息通过 base64 编码之后作为 RunInstances 接口的 UserData 参数来传递您的文本，或者在创建云服务器时通过自定义数据的方式传递您的文本。腾讯云服务器将通过开源软件cloud-init执行您的脚本，有关cloud-init的更多内容，请参阅[cloud-init官方网站](https://cloud-init.io/)。

当您传递的文本是一个标准Shell格式的脚本时，并希望服务器在首次启动时能够正确执行该脚本，需注意以下事项：

* 传递的文本应该应该经过 base64 编码（注：请在 Linux 环境下进行编码，防止格式不兼容），有关 base64 编码的更多信息，请参阅 [http://tools.ietf.org/html/rfc464](http://tools.ietf.org/html/rfc464)。
* 用户数据 Shell 脚本必须以 #! 字符以及指向要读取脚本的解释器的路径 (通常为 /bin/bash) 开头。
* 作为用户数据输入的脚本是作为 root 用户执行的，因此在脚本中不使用 sudo 命令。请注意，您创建的任何文件都将归 root 所有；如果您需要非根用户具有文件访问权，应在脚本中相应地修改权限。
* 在启动时添加这些任务会增加启动服务器所需的时间。您应多等待几分钟让这些任务完成，然后测试用户脚本是否已成功完成。

示例展示：通过传递Shell格式的脚本，在服务器首次启动时，输出"Hello Tencent Cloud"。Cloud-init 输出日志文件 (/var/log/cloud-init-output.log)将捕获控制台输出。

1. 编写Shell脚本：
```
#!/bin/bash
echo "Hello Tencent Cloud."
```
Shell 脚本首行须为 #! 字符以及指向要读取脚本的解释器的路径 (通常为 /bin/bash) 。有关 Shell 脚本的更多介绍，请参阅 Linux 文档项目 (tldp.org) 的 [BASH 编程方法](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)。

2. 使用base64编码脚本文件（注：请在 Linux 环境下进行编码，防止格式不兼容）:

假设，第一步创建的脚本文件为script_text, 在linux环境下，可以使用base64命令编码文件, 如下：
```
# 对脚本进行base64编码操作
base64 script_text

# 编码之后可得到的结果：
IyEvYmluL2Jhc2gKCmVjaG8gIldlbGNvbWUgVG8gVGVuY2VudCBDbG91ZC4iCg==

# 对返回的结果进行base64解码，以验证是否为需要执行的命令
echo "IyEvYmluL2Jhc2gKZWNobyAiSGVsbG8gVGVuY2VudCBDbG91ZC4iCg==" | base64 -d
```

3. 把编码之后的结果赋值给 RunInstances 的 UserData 参数，以下是一个带UserData参数的服务器创建请求参数示例:

```
https://cvm.tencentcloudapi.com/?Action=RunInstances
  &Version=2017-03-12
  &Placement.Zone=ap-guangzhou-2
  &ImageId=img-pmqg1cw7
  &UserData=IyEvYmluL2Jhc2gKCmVjaG8gIldlbGNvbWUgVG8gVGVuY2VudCBDbG91ZC4iCg==
  &<公共请求参数>
```





