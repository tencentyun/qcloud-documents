
企业账号 CompanyExample 下有一个子账号 Developer，该子账号需要通过控制台及 API 拥有对企业账号 CompanyExample 下的所有资源（包含日志集、日志主题、机器组等）有读权限（包含日志检索，日志采集、仪表盘和告警等配置查看）。

## 准备工作

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。创建子账号 Developer，详细操作请参考 [自定义创建子用户](https://cloud.tencent.com/document/product/598/13674)。
2. 在新建用户页面，单击【自定义创建】，进入选择用户类型页面，单击 **【可访问资源并接收消息】**。
3. 单击【下一步】，进入填写用户信息页面，选中**【编程访问】**及【**腾讯云控制台访问**】。

## 操作步骤

分为两个步骤：主账号 CompanyExample 给子账号 Developer 授权、子账号 Developer 访问 CLS 日志服务。
1. 主账号授权
 1. 主账号 CompanyExample 登录 [CAM 控制台](https://console.cloud.tencent.com/cam)。
 2. 在左侧导航中，单击【用户】>【用户列表】>【授权】。在页面【关联策略】中搜索 QcloudCLSReadOnlyAccess  ，并选中关联这个策略，单击【完成】即可。
   ![](https://main.qcloudimg.com/raw/bf8fdff48096fc52463b57d435c3f65c/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_391d4bf7-88f7-4260-8a93-57a75b18a64c.png)
2. 子账号访问
   子账号 Developer 可通过登录控制台及 API 访问 CLS 服务。需要注意的是，API 访问时需使用 主账号 CompanyExample 的 uin, 子账号 Developer 的 SecretId、SecretKey。子账号的 API  密钥可参考 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。

