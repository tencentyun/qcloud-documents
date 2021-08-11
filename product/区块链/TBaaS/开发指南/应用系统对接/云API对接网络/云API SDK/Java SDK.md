## 简介

欢迎使用腾讯云 TBaaS 产品开发者工具套件（SDK）3.0，SDK3.0 是云 API3.0 平台的配套工具。为方便 Java 开发者调试和接入腾讯云 TBaaS 产品 API，这里向您介绍适用于 Java 的腾讯云 TBaaS 产品开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 TBaaS 产品 Java SDK 并开始调用。

## 依赖环境

1.	依赖环境：JDK 7版本及以上。
2.	通过腾讯云控制台开通 TBaaS 产品。
3.	获取 [SecretID、SecretKey](https://console.cloud.tencent.com/cam/capi) 以及调用地址（tbaas.tencentcloudapi.com）。

## 获取安装

安装 Java SDK 和第一次使用云 API 之前，用户需要在腾讯云控制台上申请并获取安全凭证。安全凭证包括 SecretID 和 SecretKey。 SecretID 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 通过 Maven 安装（推荐）

Java SDK 推荐通过 Maven 安装。Maven 是 Java 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。关于 Maven 详细介绍可参考 [Maven 官网](https://maven.apache.org/)。
1.	前往 [Maven 官网](https://maven.apache.org/) 下载对应系统的 Maven 安装包，并进行安装。
2.	在 Maven pom.xml 添加以下内容，为您的项目添加 Maven 依赖项。
```
<dependency>
	<groupId>com.tencentcloudapi</groupId>
	<artifactId>tencentcloud-sdk-java</artifactId>
	<version>3.0.1</version>
</dependency>
```
>? &lt;version&gt; 标签中的版本号为参考示例，请在 Maven 仓库上找到最新的版本进行填写。
>
3.	引用方法可参考 [示例](#JavaSDK.sample)。

### 通过源码包安装

1.	前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-java) 下载源码压缩包。
2.	将获取到的源码包解压缩到您项目合适的位置。
3.	将 vendor 目录下的 jar 包拷贝到 Java 可找到的路径中。
4.	引用方法可参考 [示例](#JavaSDK.sample)。

## 接口列表

| 接口名称 | 接口功能 |
|---------|---------|
| Invoke | 新增交易（支持同步模式和异步模式） |
| Query | 查询交易 |
| GetInvokeTx | 查询 Invoke 异步调用结果 |
| GetBlockList | 查询区块列表 |
| GetBlockTransactionListForUser | 获取区块内的交易列表 |
| GetClusterSummary | 获取区块链网络概要 |
| GetLatesdTransactionList | 获取最新交易列表 |
| GetTransactionDetailForUser | 获取交易详情 |
| ApplyUserCert | 申请用户证书 |
| DownloadUserCert | 下载用户证书 |
| SrvInvoke | trustsql 服务统一接口 |
| BlockByNumberHandler | 按块高查询区块信息 |
| DeployDynamicContractHandler | 动态部署合约 |
| GetBlockListHandler | 查询区块列表 |
| GetTransByHashHandler | 根据交易哈希查询交易信息 |
| GetTransListHandler | 查询交易列表 |
| SendTransactionHandler | 发送交易 |
| TransByDynamicContractHandler | 根据动态部署的合约发送交易 |

[](id:JavaSDK.sample)
## 示例

以新增交易（Invoke）接口为例：
```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
// 导入对应产品模块的client
import com.tencentcloudapi.tbaas.v20180416.TbaasClient;
// 导入要请求接口对应的request response类
import com.tencentcloudapi.tbaas.v20180416.models.InvokeRequest;
import com.tencentcloudapi.tbaas.v20180416.models.InvokeResponse;

public class InvokeTransaction
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey
            Credential cred = new Credential("secretId", "secretKey");
            // 设置访问域名
            // SDK会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务，
            // 则必须手动指定域名，例如云服务器的上海金融区域名： tbaas.ap-shanghai-fsi.tencentcloudapi.com
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("tbaas.tencentcloudapi.com");
            // 实例化Tbaas的client对象
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);
            // 第二个参数是地域信息，根据资源所属地域填写相应的地域信息，例如广州地域的资源可以直接填写字符串ap-guangzhou，或者引用预设的常量
            TbaasClient client = new TbaasClient(cred, "ap-guangzhou", clientProfile);
            // 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
            String params = "{\"Module\":\"transaction\",\"Operation\":\"invoke\",\"ClusterId\":\"251005746ctestenv\",\"ChaincodeName\":\"pettycc1\",\"ChannelName\":\"pettyc1\",\"Peers\":[{\"PeerName\":\"peer0.pettycorg.ctestenv\",\"OrgName\":\"pettycOrg\"}],\"FuncName\":\"invoke\",\"Args\":[\"a\",\"b\",\"10\"],\"AsyncFlag\":0,\"GroupName\":\"pettycOrg\"}";
            InvokeRequest req = InvokeRequest.fromJsonString(params, InvokeRequest.class);
            // 通过client对象调用想要访问的接口，需要传入请求对象
            InvokeResponse resp = client.Invoke(req);
            // 输出json格式的字符串回包
            System.out.println(InvokeResponse.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
                System.out.println(e.toString());
        }
    }
}

```
