## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0是云 API 3.0平台的配套工具。目前已经支持 CVM、VPC、CBS 等产品，后续所有的云服务产品都会陆续接入。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
本文主要介绍适用于 Node.js 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 Node.js 开发者快速掌握如何调试和接入腾讯云产品 API。

## 支持3.0版本的云产品列表

SDK 3.0支持全部 API 3.0下的云产品，本列表可能滞后于实际代码，如有疑问请咨询具体的云产品。

<table>
  <tr>
<td><a href="https://cloud.tencent.com/document/api/213/15689">云服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/386/18637">黑石物理服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/362/15634">云硬盘</a></td>
<td><a href="https://cloud.tencent.com/document/api/457/31853">容器服务</a></td>
<td><a href="https://cloud.tencent.com/document/api/377/20423">弹性伸缩</a></td>
</tr>
<tr>
  <td><a href="https://cloud.tencent.com/document/api/583/17235">云函数</a></td>
  <td><a href="https://cloud.tencent.com/document/api/599/15880">批量计算</a></td>
  <td><a href="https://cloud.tencent.com/document/api/214/30667">负载均衡</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15755">私有网络</a></td>
 <td><a href="https://cloud.tencent.com/document/api/216/18404">专线接入</a></td>
  </tr>
  <tr>
 <td><a href="https://cloud.tencent.com/document/api/236/15830">云数据库 MySQL</a></td>
 <td><a href="https://cloud.tencent.com/document/api/239/20002">云数据库 Redis</a></td>
 <td><a href="https://cloud.tencent.com/document/api/240/31797">云数据库 MongoDB</a></td>
    <td><a href="https://cloud.tencent.com/document/api/237/16144">云数据库 MariaDB</a></td>
<td><a href="https://cloud.tencent.com/document/api/557/16124">分布式数据库 TDSQL</a></td>
 </tr>
  <tr>
 <td><a href="https://cloud.tencent.com/document/api/238/19927">云数据库 SQL Server</a></td>
  <td><a href="https://cloud.tencent.com/document/api/409/16761">云数据库 PostgreSQL</a></td>
   <td><a href="https://cloud.tencent.com/document/api/596/39648">游戏数据库 TcaplusDB</a></td>
   <td><a href="https://cloud.tencent.com/document/api/1130/39547">数据库智能管家 DBbrain</a></td>
  <td><a href="https://cloud.tencent.com/document/api/571/18122">数据传输服务</a></td>
   </tr>
   <tr>     
   <td><a href="https://cloud.tencent.com/document/api/228/30974">内容分发网络</a></td>
   <td><a href="https://cloud.tencent.com/document/api/597/40823">消息队列 CKafka</a></td>
   <td><a href="https://cloud.tencent.com/document/api/400/37386"> SSL 证书</a></td>
<td><a href="https://cloud.tencent.com/document/api/296/19825">主机安全</a></td>
  <td><a href="https://cloud.tencent.com/document/api/692/16733">漏洞扫描服务</a></td>
   </tr>
   <tr>
   <td><a href="https://cloud.tencent.com/document/api/283/17742">移动应用安全</a></td>
   <td><a href="https://cloud.tencent.com/document/api/266/31753">云点播</a></td>
     <td><a href="https://cloud.tencent.com/document/api/267/20456">云直播</a></td>
 <td><a href="https://cloud.tencent.com/document/api/647/37078">实时音视频</a></td>
<td><a href="https://cloud.tencent.com/document/api/589/33971">弹性 MapReduce</a></td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/270/35293">腾讯云搜</a></td>
<td><a href="https://cloud.tencent.com/document/api/271/35484">自然语言处理</a></td>
 <td><a href="https://cloud.tencent.com/document/api/551/15612">机器翻译</a></td>
<td><a href="https://cloud.tencent.com/document/api/656/18281">金融联络机器人</a></td>
<td><a href="https://cloud.tencent.com/document/api/607/35364">游戏多媒体引擎</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/884/19310">智聆口语评测</a></td>
<td><a href="https://cloud.tencent.com/document/api/382/38764">短信</a></td>
<td><a href="https://cloud.tencent.com/document/api/636/33864">物联卡</a></td>
<td><a href="https://cloud.tencent.com/document/api/634/19469">物联网通信</a></td>
<td><a href="https://cloud.tencent.com/document/api/663/19455">TBaaS</a></td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/248/30343">云监控</a></td>
<td><a href="https://cloud.tencent.com/document/api/598/33155">访问管理</a></td>
<td><a href="https://cloud.tencent.com/document/api/651/35307">标签</a></td>
<td><a href="https://cloud.tencent.com/document/api/850/38719">企业组织</a></td>
<td><a href="https://cloud.tencent.com/document/api/573/34403">密钥管理系统</a></td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/629/35332">云审计</a></td>
<td><a href="https://cloud.tencent.com/document/api/659/18591">迁移服务平台</a></td>
 <td><a href="https://cloud.tencent.com/document/api/555/19170">计费相关</a></td>
 <td><a href="https://cloud.tencent.com/document/api/563/16034">渠道合作伙伴</a></td>
<td><a href="https://cloud.tencent.com/document/api/1141/41605">容器镜像服务</a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/1172/40697">人脸试妆</a></td>
<td><a href="https://cloud.tencent.com/document/api/1140/40506">凭据管理系统</a></td>
<td><a href="https://cloud.tencent.com/document/api/1122/40639">企业收付平台</a></td>
<td><a href="https://cloud.tencent.com/document/api/1127/40301">营销号码安全</a></td>
<td><a href="https://cloud.tencent.com/document/api/1156/40338">腾讯云剪</a></td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/1155/40100">正版曲库直通车</a></td>
<td><a href="https://cloud.tencent.com/document/api/1137/40049">互动白板</a></td>
<td><a href="https://cloud.tencent.com/document/api/1120/37543">智能钛弹性模型服务</a></td>
<td><a href="https://cloud.tencent.com/document/api/1105/37347">云 HDFS</a></td>
<td><a href="https://cloud.tencent.com/document/api/1110/36917">验证码</a></td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/242/38884">域名注册</a></td>
<td><a href="https://cloud.tencent.com/document/api/280/40881">云拨测</a></td>
<td><a href="https://cloud.tencent.com/document/api/1093/35637">语音识别</a></td>
<td><a href="https://cloud.tencent.com/document/api/1064/35622">业务风险情报</a></td>
<td><a href="https://cloud.tencent.com/document/api/1086/35602">物联网设备身份认证</a></td> 
</tr>
 <tr>
<td><a href="https://cloud.tencent.com/document/api/1081/34958"> 物联网开发平台</a></td>
<td><a href="https://cloud.tencent.com/document/api/1078/35028">小程序 · 云直播</a></td>
<td><a href="https://cloud.tencent.com/document/api/1073/37986">语音合成</a></td>
<td><a href="https://cloud.tencent.com/document/api/1060/37428"> 腾讯智能对话平台</a></td>
<td><a href="https://cloud.tencent.com/document/api/856/33899">数据安全审计 </a></td>
  </tr>
  <tr>
   <td><a href="https://cloud.tencent.com/document/api/649/36037">腾讯微服务平台 TSF</a></td>
   <td><a href="https://cloud.tencent.com/document/api/862/37569">视频处理</a></td>
   <td><a href="https://cloud.tencent.com/document/api/639/41452">云加密机</a></td>
   <td><a href="https://cloud.tencent.com/document/api/876/34809">云开发</a></td>
   <td><a href="https://cloud.tencent.com/document/api/608/36932">全球应用加速</a></td>  
	 </tr>
  <tr>
<td><a href="https://cloud.tencent.com/document/api/582/38145">文件存储</a></td>
  <td><a href="https://cloud.tencent.com/document/api/1007/31320">人脸核身-云智慧眼</a></td>
<td><a href="https://cloud.tencent.com/document/api/1021/39215">DDoS 高防包</a></td>
   <td><a href="https://cloud.tencent.com/document/api/1013/31737">威胁情报云查</a></td>
  <td><a href="https://cloud.tencent.com/document/api/1004/30607">数学作业批改</a></td>
	  </tr>
  <tr>
  <td><a href="https://cloud.tencent.com/document/api/1076/35201">英文作业批改</a></td>   
	<td><a href="https://cloud.tencent.com/document/api/670/31052">人脸融合</a></td>
    <td><a href="https://cloud.tencent.com/document/api/867/32770">人脸识别</a></td>
   <td><a href="https://cloud.tencent.com/document/api/866/33515">文字识别</a></td>
   <td><a href="https://cloud.tencent.com/document/api/865/35462">图像分析</a></td>
   </tr>
  <tr>
   <td><a href="https://cloud.tencent.com/document/api/1000/30698">数字版权管理</a></td>
  <td><a href="https://cloud.tencent.com/document/api/845/30620">Elasticsearch Service</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
     </tr>
  </table>


## API Explorer
[API Explorer](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、 SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度，推荐使用。

## 依赖环境

- Node.js 7.10.1 版本及以上。
- 登录 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应云产品。
- 在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 获取调用地址（endpoint），endpoint 一般格式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各云产品说明。

## 获取安装

### 通过 npm 安装（推荐）
[npm](https://www.npmjs.com/) 是 Node.js 的包管理工具。

1. 执行以下安装命令：
```
npm install tencentcloud-sdk-nodejs --save
```
2. 在您的代码中引用对应模块代码，可参考 [示例](#example)。

### 通过源码包安装
1. 前往 [GitHub 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-nodejs) 或者 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-nodejs/tencentcloud-sdk-nodejs.zip)，下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 在您的代码中引用对应模块代码，可参考 [示例](#example)。

<span id="example"></span>
## 示例
本文以云服务器查询可用区接口为例，更多示例请参考 [examples 目录](https://github.com/TencentCloud/tencentcloud-sdk-nodejs/tree/master/examples)。

```js
const tencentcloud = require("../../../../tencentcloud-sdk-nodejs");

// 导入对应产品模块的 client models
const CvmClient = tencentcloud.cvm.v20170312.Client;
const models = tencentcloud.cvm.v20170312.Models;

const Credential = tencentcloud.common.Credential;

// 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
let cred = new Credential("secretId", "secretKey");

// 实例化要请求产品（以 CVM 为例）的 client 对象
let client = new CvmClient(cred, "ap-shanghai");

// 实例化一个请求对象
let req = new models.DescribeZonesRequest();

// 通过 client 对象调用想要访问的接口，需要传入请求对象以及响应回调函数
client.DescribeZones(req, function(errMsg, response) {
    // 请求异常返回，打印异常信息
    if (errMsg) {
        console.log(errMsg);
        return;
    }
    // 请求正常返回，打印 response 对象
    console.log(response.to_json_string());
});
```


## 旧版 SDK
我们推荐使用新版 Node.js SDK，如果需要使用旧版 SDK，请前往 [GitHub 仓库](https://github.com/CFETeam/qcloudapi-sdk) 下载。
