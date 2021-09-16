## 操作场景
如果证书已过期，用户在浏览网站的时候会显示证书不可信；如果客户该域名有使用 API 调用，在调用过程中将会报错。为了避免证书过期对业务造成影响，请在腾讯云控制台上及时更新证书。

## 操作步骤
### 示例1：更换自有证书
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航中，选择选择【实例管理】>【域名接入】，进入域名接入页面。
2. 在域名接入页面，选中所需域名，单击【编辑】，进入编辑域名页面。
![](https://main.qcloudimg.com/raw/f26543b49f58a5c29de895b8b72c0d94.png)
3. 在编辑域名页面，单击服务器配置中的【重新关联】，弹窗证书配置窗口。
![](https://main.qcloudimg.com/raw/b6323012fa764e056e3e0de1108ecfb0.png)
4. 在证书配置窗口，证书来源选择自有证书，并输入相关的证书和私钥，单击【保存】，即可更换自有证书。
![](https://main.qcloudimg.com/raw/43e585d512df3a310c4082e6e902bc70.png)

### 示例2：腾讯云托管证书
1. 在 [域名接入](https://console.cloud.tencent.com/guanjia/instance/domain) 页面，选中所需域名，单击【编辑】，进入编辑域名页面。
![](https://main.qcloudimg.com/raw/f26543b49f58a5c29de895b8b72c0d94.png)
2. 在编辑域名页面，单击服务器配置中的【重新关联】，弹窗证书配置窗口。
![](https://main.qcloudimg.com/raw/b6323012fa764e056e3e0de1108ecfb0.png)
2. 在证书配置窗口，证书来源选择腾讯云托管证书，并选择新证书，单击【保存】，即可更换 SSL 证书。
>?此方法只适用于证书已经上传到 SSL 证书管理。
>
![](https://main.qcloudimg.com/raw/0ab087a75f4e1570d6adb19ec91090a5.png)

### 示例3：一键替换证书
1. 登录 [SSL 证书](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航中，单击【我的证书】，进入我的证书页面。
2. 在我的证书页面，选择所需 ID,单击【部署】，弹出选择部署类型弹窗。
![](https://main.qcloudimg.com/raw/59512620e91d930e09564cc158447acd.png)
3. 在选择部署类型弹窗，部署类型选择 Web 应用防火墙，并选择所需 WAF 资源，单击【确定】，即可一键替换证书。
![](https://main.qcloudimg.com/raw/fdf31449280401cf67ce7f64f50ceb6e.png)

## 检验是否生效
通过浏览器访问相关域名，可以查看证书的生效时间和到期时间。如果更换证书始终不生效，请 [联系我们](https://cloud.tencent.com/online-service?from=connect-us) 获得帮助。
![](https://main.qcloudimg.com/raw/e95302f7dd2c8749159f35673dc1c0ef.png)
