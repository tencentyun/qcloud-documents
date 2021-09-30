
## 腾讯 HR 助手人员组织同步
1.  登录 [千帆 aPaaS 运行态首页](https://apaas.cloud.tencent.com/)，进入管理后台，单击左侧导航栏【用户管理】。当租户企业管理员未进行人员组织初始化时，进入下图页面。对于用户管理的基本介绍可参考 [用户管理](https://cloud.tencent.com/document/product/1365/57571)。
![img](https://main.qcloudimg.com/raw/e9f7e5ddea5cf770c012d181f74ea316.png)        
2. 单击【腾讯 HR 助手】，并填写相关信息。
![img](https://main.qcloudimg.com/raw/eeee86cc49847296503cee81091fb767.png)        
![img](https://main.qcloudimg.com/raw/395be3686c4b2541f2a7364519f98bea.png)        
3. 当完成信息的填写后单击【完成】，等待片刻即可完成同步，上图信息获取方式请见下文。

## 获取 E 人事 Corp Key
1. 登录 EHR 管理后台。
>?线下开通后，每位租户会有一个独立的登录链接，由工作人员进行提供。
![img](https://main.qcloudimg.com/raw/41973f2ac850857d92df5eb5974d514d.png)        
2. 从地址栏获取 Corp Key 信息。例如：`https://ehrnew-apaas.ihr.tencent-cloud.com/employeeInformation，ehrnew` 和` ihr.tencent-cloud.com` 之间的 apaas 即为 Corp Key。
![img](https://main.qcloudimg.com/raw/fa5ea4aea0c3619fc02f5ef570925ba2.png)        



## 创建玉符 OIDC 类型应用
1. 登录千帆玉符管理后台，定位到“应用管理”。
>?线下开通后，每位租户会有一个独立的登录链接，由工作人员进行提供。
![img](https://main.qcloudimg.com/raw/faaa40c168389b1b11d42428a9fd55c3.png)        
2. 单击【添加应用】，选择【创建自定义应用】进入创建应用页面。
![img](https://main.qcloudimg.com/raw/57eebdbd7902b6a573a468fe5c9fecec.png)        
3. 选择“OpenID Connect”类型。
![img](https://main.qcloudimg.com/raw/b3c3e2fbb2cb9930a039b0b76946e1fd.png)        
![img](https://main.qcloudimg.com/raw/d15a5eb3bb6b22cca0be9ede7554ca73.png)        
4. 填写应用基本信息，单击【确定】完成创建。
![img](https://main.qcloudimg.com/raw/56a7fbfb11489187e21c57b679748ad7.png)        



## 获取应用 Well-known 接口及 SecretId 和 SecretKey
1. 登录千帆玉符管理后台，单击“单点登录”中的【常规配置】。
![img](https://main.qcloudimg.com/raw/9c30ebe95643eca4bc88ba851468dc21.png)        
2. 获取应用 Well-known 接口地址，并将其填入配置页面对应字段。
![img](https://main.qcloudimg.com/raw/b67d02b223061c8442a89f3d6e876102.png)        
3. 获取应用 Client ID，并将其填入配置页面对应字段。
![img](https://main.qcloudimg.com/raw/767c009784e85bf600a77a5607ee8bf2.png)        
4. 获取应用 Client Secret，并将其填入配置页面对应字段。
![img](https://main.qcloudimg.com/raw/53eabdcecb9e2c5a2039cfe3c14f20e1.png)        
