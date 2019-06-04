## 操作场景

用户在创建云服务器时，您可以通过指定**自定义数据**配置实例。当服务器**首次启动**时，自定义数据将以文本的方式传递到云服务器中，并执行该文本。如果您一次购买多台云服务器，自定义数据会在所有的云服务器首次启动时运行。
本文以 Windows 云服务器首次启动时，通过传递 PowerShell 格式的脚本，实现输出 "Hello Tencent Cloud" 为例。

## 注意事项

* 支持自定义数据的Windows操作系统包括：
 * Windows Server 2016 数据中心版64位中文版
 * Windows Server 2012 R2 数据中心版64位英文版
* 仅限首次启动云服务器时，通过传递文本执行命令。
* 传递的文本必须经过 Base64 编码。
* 在启动时，执行自定义数据中指定的任务会增加启动服务器所需的时间。建议您等待几分钟，并在任务完成后，测试任务是否已成功执行。
* 本示例中，请使用 PowerShell 标签指定 Windows PowerShell 脚本，例如 &lt;powershell&gt;&lt;/powershell&gt; 标签。

## 操作步骤

>! 请在 Linux 环境下执行以下操作。
>

### 编写 PowerShell 脚本

参考以下内容，创建一个名称为 “script_text” 的 PowerShell 脚本文件。
```
<powershell>
"Hello Tencent Cloud." | Out-File .\tencentcloud.txt
</powershell>
```

<span id="Base64Script"></span>
### 使用 Base64 编码脚本文件

执行以下命令，对脚本进行 Base64 编码操作。
```
base64 script_text
```
进行 Base64 编码操作后，返回以下信息：
```
PHBvd2Vyc2hlbGw+CiJIZWxsbyBUZW5jZW50IENsb3VkLiIgfCBPdXQtRmlsZSAuXHRlbmNlbnRjbG91ZC50eHQKPC9wb3dlcnNoZWxsPgo=
```

### 传递文本

我们提供多种启动实例的方式，主要分为以下两种情况。请根据您的实际情况进行选择：
- [通过官网或控制台传递](#Consoletrans)
- [通过 API 传递](#APItrans)

<span id="Consoletrans"></span>
#### 通过官网或控制台传递

1. 通过腾讯云官网或控制台创建云服务器。
2. 在**4.设置安全组和主机**界面中，选择**高级设置**，并在 “自定义数据” 中填写您 [使用 Base64 编码脚本文件](#Base64Script) 返回的编码结果。如下图所示：
![Alt text](https://main.qcloudimg.com/raw/3dda15f7521d338300ca0c3f4ad35e8e.png)
3. 按照界面信息逐步操作，完成创建并启动云服务器。

<span id="APItrans"></span>
#### 通过 API 传递

当您通过 API 创建云服务器时，可以将 [使用 Base64 编码脚本文件](#Base64Script) 中返回的编码结果赋值给 RunInstances 接口的 UserData 参数，以此来传递文本。以创建一个带 UserData 参数的云服务器的请求参数为例：
```
https://cvm.tencentcloudapi.com/?Action=RunInstances
  &Version=2017-03-12
  &Placement.Zone=ap-guangzhou-2
  &ImageId=img-pmqg1cw7
  &UserData=PHBvd2Vyc2hlbGw+CiJIZWxsbyBUZW5jZW50IENsb3VkLiIgfCBPdXQtRmlsZSAuXHRlbmNlbnRjbG91ZC50eHQKPC9wb3dlcnNoZWxsPgo=
  &<公共请求参数>
```
