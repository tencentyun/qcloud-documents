本文为您详细介绍如何通过 PuTTY 实现密钥直连和单点登录资源。

## 准备工作

本文演示机器及相关准备工作，请参见概述文档 [准备工作](https://cloud.tencent.com/document/product/1025/38514#.E5.87.86.E5.A4.87.E5.B7.A5.E4.BD.9C) 章节。

## 操作步骤

### 步骤1：生成密钥对
1. 打开 PuTTY 安装目录，双击运行 puttygen.exe。
2. 打开后，选择密钥对类型及长度，选择 Generate 生成密钥对。
<img src="https://main.qcloudimg.com/raw/8f6073ef798ed32011db3e9cb048c668.png"  width="70%">
3. 生成密钥对后，可选择保存公钥和保存密钥（PuTTY 工具生成速度较慢，请耐心等候）。
<img src="https://main.qcloudimg.com/raw/e60edc9ee4a419b6cfb0657ca651878d.png"  width="70%">




### 步骤2：实现密钥直连登录
1. 在 PuTTY 安装目录下，双击运行 putty.exe。
2. 单击【Session】，配置登录 IP、端口。
3. 配置使用的私钥文件有两种方式。
 - 方式1：在 PuTTY 中，展开 Connection，选择【SSH】>【Auth】，配置使用的私钥文件。
 <img src="https://main.qcloudimg.com/raw/e0b3f575f35421d93807821542466a2e.png"  width="70%">
 - 方式2：运行 PuTTY 安装目录下 pageant.exe， 选择【Add Key】，将私钥导入该服务。
<img src="https://main.qcloudimg.com/raw/d63caf6d5ea167baf5b5aea06075a0c4.png"  width="70%"> 
>?pageant 程序导入的私钥需使用特定格式的文件，其他格式文件会出现错误，如需转换格式请参见 [格式转换](#step4)。
4. 至此，您就可以使用 Putty 实现密钥直连登录。

### 步骤3：实现密钥单点登录
>!目前堡垒机单点登录呼出的 PuTTY 工具版本为0.63，为单点登录控件（sso_client）内置的 putty.exe，单点登录控件中未安装 pageant.exe 及 puttygen.exe 等组件，需另行下载安装。（pageant.exe 版本选择推荐0.69）。

1. 打开单点登录控件安装目录下的 putty.exe。
2. 选择【Connection】>【SSH】>【Auth】，转发需要勾选的内容 Allow agent forwarding 及 Allow attempted changes of username in SSH-2，并保存为默认。
<img src="https://main.qcloudimg.com/raw/e1719013a5ed345bb6130eeb2a9b8093.png"  width="70%"> 
<img src="https://main.qcloudimg.com/raw/3f0c049283199868b9f03df8ef26bfa2.png"  width="70%"> 
3. 打开另行下载的 PuTTY 工具安装目录下的 pageant.exe，将私钥添加到 Private Key List 并保持服务开启后。
<img src="https://main.qcloudimg.com/raw/2a09d8581d52abaaefbbc2fd1e29e381.png"  width="70%"> 
4. 配置完成后即可进行 PuTTY 单点登录。打开浏览器，登录堡垒机。在登录界面，账号选择 tom，登录工具选择 PuTTY，单击【连接】，即可调用 PuTTY 实现单点登录。
<img src="https://main.qcloudimg.com/raw/c74d21cc7294cb622521b56c584ea864.png"  width="70%"> 


<span id="step4"></span>
#### 格式转换
使用 PuTTY 转换其他私钥文件格式为指定格式（如不存在格式错误请忽略）。

1. 在 PuTTY 安装目录下打开 puttygen.exe，并选择 load，单击【确定】。
<img src="https://main.qcloudimg.com/raw/23077f5db466b0cbe85ba41d0627572c.png"  width="70%"> 
2. 导入成功后，选择【Save private key】，导出为特定格式（.ppk格式），即可在 pageant.exe 服务中使用。
<img src="https://main.qcloudimg.com/raw/069c320946f0538dd915455ab708685c.png"  width="70%"> 

