## 现象描述

- **现象1**：<span id="FaultPhenomenon1"></span>
 - 使用公司网络进行上传时，传输正常；使用家庭网络进行上传时，传输缓慢（低于8Mbps）。
 - 使用手机4G网络进行上传时，传输正常；使用公司网络进行上传时，传输缓慢（低于8Mbps）。
- **现象2**：<span id="FaultPhenomenon2"></span>使用自定义域名进行上传时，传输缓慢。

## 可能原因

- 针对现象1：
 1. 如果您在不同的网络环境下访问 COS 的速率不同，可能和当前网络运营商及网络环境有关。
 2. 如果您在不同的网络环境下访问 COS 的速率不同，可能因跨境访问导致。
- 针对现象2：自定义域名 CNAME 到其他产品再转回到 COS，如内容分发网络（Content Delivery Network，CDN）、云服务器（Cloud Virtual Machine，CVM）、安全高防产品。

## 解决思路

- 如果您遇到 [现象1](#FaultPhenomenon1) 的情况，则可以通过检查客户端网络环境的方式自行处理。操作详情请参见 [排查客户端网络](#SearchTheClientNetwork)。
- 如果您遇到 [现象2](#FaultPhenomenon2) 的情况，则可以通过修改自定义域名解析的方式减少传输中转链路，提高传输效率。操作详情请参见 [修改自定义域名解析](#ModifyCustomDomainNameResolution)。

## 处理步骤

<span id="SearchTheClientNetwork"></span>
### 排查客户端网络

1. 执行以下命令，确认 IP 地址运营商与客户端网络运营商是否相符。
```
ping COS 的访问域名
```
例如：
```
ping examplebucket-1250000000.cos.ap-beijing.mqcloud.com
```
 - 是，请执行 [步骤3](#step03)。
 - 否，请执行 [步骤2](#step02)。
2. <span id="step02"></span>以 Chrome 浏览器为例，检查浏览器是否设置了代理。
    1. 打开 Chrome 浏览器，单击右上角的 <img src="https://main.qcloudimg.com/raw/41a048f92c3d6160faff7e211bacce76.png"/> > **设置**，打开设置页面。
    2. 单击**高级**，在“系统”栏中选择**在您计算机的代理设置**，打开操作系统的设置窗口。
    ![](https://main.qcloudimg.com/raw/debb2af04d7ee52d9013b940efa48abc.png)
    检查是否设置了代理。
     - 是，关闭代理。
     - 否，请执行 [步骤3](#step03)。
3. <span id="step03"></span>检查所用的 Wi-Fi 路由器是否存在限速。
 - 是，请根据实际需求，酌情放行。
 - 否，请执行 [步骤4](#step04)。
4. <span id="step04"></span>检查当前网络上传 COS 的传输性能。
以 COS 的 COSCMD 工具为例，测试一个20MB对象的上传和下载性能。
```
coscmd probe -n 1 -s 20
```
返回类似如下结果，分别得出平均速率（Average），最低速率（Min），最高速率（Max）。
![](https://main.qcloudimg.com/raw/2fcecb96df04acc6b0c32c120ccb3c39.png)
5. 通过浏览器访问 [测速网](https://www.speedtest.cn/)，并结合 [步骤4](#step04) 检查客户端的网络带宽占用率是否达到上限。
 - 如果步骤4的速率低于客户端带宽速率，请 [联系我们](https://cloud.tencent.com/document/product/436/37708)。
 - 如果步骤4的速率等于客户端带宽速率，且未达到运营商承诺的带宽，请联系运营商客服。
 - 如果步骤4的速率等于客户端带宽速率，且达到了运营商承诺的带宽，请执行 [步骤6](#step06)。
6. <span id="step06"></span>检查是否存在国内客户端访问海外节点 bucket，或者存在海外客户端访问国内节点 bucket。
 - 是，建议使用 COS 的全球加速功能。详情请参阅 [腾讯云COS全球加速让全球用户加速访问](https://cloud.tencent.com/developer/article/1667036) 和 [利用COS全球加速的高效率传输实践](https://cloud.tencent.com/developer/article/1768085)。
 - 否，请 [联系我们](https://cloud.tencent.com/document/product/436/37708)。

<span id="ModifyCustomDomainNameResolution"></span>
### 修改自定义域名解析

1. 检查自定义域名解析是否为 COS 域名。
 - 是，请 [联系我们](https://cloud.tencent.com/document/product/436/37708)。
 常见的 COS 域名如下：
```
XXX.cos.ap-beijing.myqcloud.com  （COS 默认域名）
XXX.cos.accelerate.myqcloud.com （COS 全球加速域名）
XXX.cos-website.ap-beijing.myqcloud.com（COS 静态页域名）
XXX.picbj.myqcloud.com（COS 数据万象默认域名）
```
 - 否，请执行 [步骤2](#2_step02)。
常见的非 COS 域名如下： 
```
XXX.file.myqcloud.com 或 XXX.cdn.dnsv1.com（腾讯云 CDN 默认域名）
XXX.w.kunlungr.com（aliyunCDN 默认域名）
```
2. <span id="2_step02"></span>将自定义域名的 CNAME 解析到所需的 COS 域名中，并进行数据上传。
例如 `upload.mydomain.com  cname XXX.cos.ap-beijing.myqcloud.com`，具体操作请参见 [开启自定义源站域名](https://cloud.tencent.com/document/product/436/36638)。
3. 修改客户端的默认 COS 域名。
以 C# 代码为例：
```
CosXmlConfig config = new CosXmlConfig.Builder()
.SetConnectionTimeoutMs(60000) //设置连接超时时间，单位 毫秒 ，默认 45000ms
.SetReadWriteTimeoutMs(40000) //设置读写超时时间，单位 毫秒 ，默认 45000ms
.IsHttps(true) //设置默认 https 请求 
.SetAppid(appid) //设置腾讯云账户的账户标识 APPID
.SetRegion(region) //设置一个默认的存储桶地域
.SetHost("XXXXXX.com") //输入自定义域名
.SetDebugLog(true) .Build(); //创建 CosXmlConfig 对象
```
其他 SDK 调用请参见 [SDK 概览](https://cloud.tencent.com/document/product/436/6474)。
