## 开发准备
### 预备知识
一般来说 COS 服务的整体架构可以如下图所示：
![](http://mc.qcloudimg.com/static/img/b1e187a9ec129ffc766c07a733ef4dd6/image.jpg)
其中 CAM 权限系统和 COS 对象存储是腾讯云提供给开发者的两大服务模块，分别用于用户鉴权和存储文件。而用户服务端和用户客户端需要用户自己去搭建，本文介绍如何基于 COS Android SDK 来快速搭建应用传输服务。

## 快速体验

### 环境要求

- 一台安装了 python3 环境的机器
- 一台 Android 4.0 (api level 15)及以上版本的手机。

### 搭建服务端

#### 安装 cossign

cossign 目前只支持 python3，它可以给您提供临时秘钥服务，您可以直接使用 pip 进行安装。

```
pip3 install cossign
```

#### 运行 cossign

安装后，您可以运行如下命令启动临时秘钥服务（您可以不指定端口号，默认为 5000）：

```
cossign --secret_id your_secret_id --secret_key your_secret_key --port 5000
```
> 密钥信息可以在 [云 API 密钥控制台](https://console.cloud.tencent.com/cam/capi) 查询。

#### 测试服务

运行成功后，您可以直接 curl 如下地址：

```
http://your_server_ip:5000/sign
```
若返回如下信息，则说明服务已经成功运行。
```
{
 "code":0,
 "message":"",
 "codeDesc":"Success",
 "data":{
  "credentials":{
   "sessionToken":"634aa09dccc3274045ba413ec081c1df64007f0a30001",
   "tmpSecretId":"AKIDwxHZGTUvXAfcbLaOedJUQuwBXWUXG4m3",
   "tmpSecretKey":"kriDdZsOuuF9zrZPlSAVVG0Sg4RXZu6M"},
  "expiredTime":1530515889}
 }
```
若没有返回上述信息，请在参考文末的 [常见问题](#FAQ) 部分。

### 搭建客户端

#### 下载并安装 APK

您可以扫描二维码直接下载 apk 文件：

![](http://tac-resource-do-not-remove-1253653367.cosgz.myqcloud.com/1532524409.png) 

#### 配置基本信息

您必须在 app 中配置您的 appid、服务端的地址和端口号（默认为 5000），才能正确的使用我们的服务：

选择【右上角的菜单栏】-> 点击【配置参数】



[项目 GitHub 地址](https://github.com/tencentyun/qcloud-sdk-android-samples/tree/master/QCloudCosQuickStart)。

<a id="FAQ"></a>
## 常见问题

搭建临时密钥的过程中可能会出错，如果出现了对应的错误，可以参考以下的信息：
1. **问题：**运行安装命令`pip3 install flask`提示`comment not found pip3`。
**分析：**因为没有安装 Python3，或安装了 Python3 但 path 没有设置正确。
**解决方案：**可根据系统对应寻找 Python3 安装方式进行安装，或检查 path 设置。

2. **问题：**服务运行起来以后，获取临时密钥时提示`URLError: urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed`错误。
**解决方案：**该问题常见于 MAC OS X 系统，安装 certifi 模块即可，具体操作方式可参考 [Stack Overflow FAQ](https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error/42334357#42334357)。
