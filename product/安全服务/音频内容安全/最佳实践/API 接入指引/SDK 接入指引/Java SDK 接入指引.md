## 支持环境
- JDK 7版本及以上。
- 调用地址：`ams.tencentcloudapi.com`。
>!API 支持就近地域接入，本产品就近地域接入的域名为 ams.tencentcloudapi.com，也支持指定地域域名访问，例如：广州地域的域名为 ams.ap-guangzhou.tencentcloudapi.com。详细请参考 [文本内容安全-请求结构](https://cloud.tencent.com/document/product/1219/53261)。
>

## 安装 SDK
### 方式1：通过 Maven 安装（推荐）
Maven 是 Java 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。
1. 请访问 [Maven官网](https://maven.apache.org/) 下载对应系统的 Maven 安装包进行安装。
2. 为您的项目添加 Maven 依赖项，只需在 pom.xml 中找到 `<dependencies>` 标签，在里面添加以下依赖项即可。
```
<dependency>
     <groupId>com.tencentcloudapi</groupId>
     <artifactId>tencentcloud-sdk-java</artifactId>
     <!-- go to https://search.maven.org/search?q=tencentcloud-sdk-java and get the latest version. -->
     <!-- 请到https://search.maven.org/search?q=tencentcloud-sdk-java查询所有版本，最新版本如下 -->
     <version>3.1.322</version>
</dependency>
```
>!
>- 这里的版本号只是举例，您可以在 [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 上找到最新的版本。
>- Maven 仓库 中显示的4.0.11是废弃版本，由于 Maven 索引更新问题尚未完全删除。
>- 若上面的引用方式会将腾讯云所有产品 SDK 下载到本地，可以将 `artifactId` 替换成 `tencentcloud-sdk-java-cvm/cbs/vpc` ，即可引用特定产品的 SDK，代码中使用方式和大包相同，可参考示例。
>
3.  设置镜像源以加快下载速度，编辑 Maven 的 settings.xml 配置文件，在 mirrors 段落增加镜像配置。
```
    <mirror>
      <id>tencent</id>
      <name>tencent maven mirror</name>
      <url>https://mirrors.tencent.com/nexus/repository/maven-public/</url>
      <mirrorOf>*</mirrorOf>
    </mirror>
```

### 方式2：通过源码包安装
1.  前往[ Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-java) 下载源码压缩包。
2.  解压源码包到您项目合适的位置。
3.  需要将 vendor 目录下的 jar 包放在 Java 可找到的路径中。
4.  引用方法可参考 [使用 SDK](#SDK) 。

## 使用 SDK[](id:SDK)
以下为 TextModeration 接口的 demo 示例，其中 region 配置为广州，实际请按需配置。

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.ams.v20201229.AmsClient;
import com.tencentcloudapi.ams.v20201229.models.*;
public class TextModeration {
	public static void main(String[] args) {
		try {
			// 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密 
			// 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取 
			Credential cred = new Credential("SecretId", "SecretKey");
			// 实例化一个http选项，可选的，没有特殊需求可以跳过 
			HttpProfile httpProfile = new HttpProfile();
			httpProfile.setEndpoint("ams.tencentcloudapi.com");
			// 实例化一个client选项，可选的，没有特殊需求可以跳过 
			ClientProfile clientProfile = new ClientProfile();
			clientProfile.setHttpProfile(httpProfile);
			// 实例化要请求产品的client对象,clientProfile是可选的 
			AmsClient client = new AmsClient(cred, "ap-guangzhou", clientProfile);
			// 实例化一个请求对象,每个接口都会对应一个request对象 
			TextModerationRequest req = new TextModerationRequest();
			// 返回的resp是一个TextModerationResponse的实例，与请求对象对应 
			TextModerationResponse resp = client.TextModeration(req);
			// 输出json格式的字符串回包 
			System.out.println(TextModerationResponse.toJsonString(resp));
		} catch (TencentCloudSDKException e) {
			System.out.println(e.toString());
		}
	}
}
```
