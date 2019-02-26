## 启动时在windows服务器上运行命令

当您在腾讯云上启动windows服务器时，可以选择将用户的数据以文本的方式传递到服务器里面。当您传递的文本是一个标准 PowerShell 格式的脚本时，该脚本将在服务器首次启动的时候被执行。您可以把您想要传递的文本信息通过 base64 编码之后作为 RunInstances 接口的 UserData 参数来传递您的文本，或者在创建云服务器时通过自定义数据的方式传递您的文本。

当您传递的文本是一个标准PowerShell格式的脚本时，并希望服务器在首次启动时能够正确执行该脚本，需注意以下事项：

* 传递的文本应该应该经过 base64 编码，有关 base64 编码的更多信息，请参阅 [http://tools.ietf.org/html/rfc464](http://tools.ietf.org/html/rfc464)。
* 使用 PowerShell 标签指定 Windows PowerShell 脚本，例如：
```
<powershell>
"Hello Tencent Cloud." | Out-File .\tencentcloud.txt
</powershell>
```

* 在启动时添加这些任务会增加启动服务器所需的时间。您应多等待几分钟让这些任务完成，然后测试用户脚本是否已成功完成。

示例展示：通过传递PowerShell格式的脚本，在服务器首次启动时，输出"Hello Tencent Cloud"到指定文件。

1. 编写PowerShell脚本：
```
<powershell>
"Hello Tencent Cloud." | Out-File .\tencentcloud.txt
</powershell>
```
2. 使用Base64编码PowerShell脚本：

```
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Script)
$EncodedText =[Convert]::ToBase64String($Bytes)

# 编码之后可得到的结果：
PABwAG8AdwBlAHIAcwBoAGUAbABsAD4AIAAiAEgAZQBsAGwAbwAgAFQAZQBuAGMAZQBuAHQAIABDAGwAbwB1AGQALgAiACAAfAAgAE8AdQB0AC0ARgBpAGwAZQAgAC4AXAB0AGUAbgBjAGUAbgB0AGMAbABvAHUAZAAuAHQAeAB0ACAAPAAvAHAAbwB3AGUAcgBzAGgAZQBsAGwAPgA=
```

3. 把编码之后的结果赋值给 RunInstances 的 UserData 参数，以下是一个带UserData参数的服务器创建请求参数示例:

```
https://cvm.tencentcloudapi.com/?Action=RunInstances
  &Version=2017-03-12
  &Placement.Zone=ap-guangzhou-2
  &ImageId=img-pmqg1cw7
  &UserData=PABwAG8AdwBlAHIAcwBoAGUAbABsAD4AIAAiAEgAZQBsAGwAbwAgAFQAZQBuAGMAZQBuAHQAIABDAGwAbwB1AGQALgAiACAAfAAgAE8AdQB0AC0ARgBpAGwAZQAgAC4AXAB0AGUAbgBjAGUAbgB0AGMAbABvAHUAZAAuAHQAeAB0ACAAPAAvAHAAbwB3AGUAcgBzAGgAZQBsAGwAPgA=
  &<公共请求参数>
```







