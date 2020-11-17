
企业账号 CompanyExample 下有一个子账号 Developer，该子账号需要通过控制台及 API 拥有对企业账号 CompanyExample 下的所有资源（包含日志集、日志主题、机器组等）有所有权限（包含日志采集、检索、分析、仪表盘和告警等）。

## 准备工作

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。创建子账号 Developer，详细操作请参考 [自定义创建子用户](https://cloud.tencent.com/document/product/598/13674)。
2. 在新建用户页面，单击【自定义创建】，进入选择用户类型页面，单击 **【可访问资源并接收消息】**。
3. 单击【下一步】，进入填写用户信息页面，选中**【编程访问】**及【**腾讯云控制台访问**】。

## 操作步骤

分为三个步骤：主账号 CompanyExample 创建自定义策略（可选，如需使用功能“投递至 COS”和“投递至 Ckafka”则创建此策略。用于配置“投递至 COS”时可列出 COS 的 bucket 列表，及配置“投递至 CKafka”时可列出 CKafka 的实例和 topic 列表）、主账号 CompanyExample 给子账号 Developer 授权、子账号 Developer 访问 CLS 日志服务。

1. 创建自定义策略（可选步骤，如需使用功能“投递至 COS”和“投递至 Ckafka”则创建此策略，否则跳到步骤2）
 1. 主账号 CompanyExample 登录 [CAM 控制台](https://console.cloud.tencent.com/cam)。
 2. 在左侧导航中，单击【策略】>【新建自定义策略】>【按策略语法创建】>【空白模版】建立新策略，如名称为 CLSListCosCKafka ，并在【策略内容】中，贴入以下内容：
	```plaintext
{
	 "version": "2.0",
	 "statement": [
		{
			"effect": "allow",
			"action": [
			    "cos:GetService",
				"ckafka:ListInstance",
				"ckafka:ListTopic"
		   ],
           "resource": "*"
        }
      ]
}
	```
  如下图所示：
   ![](https://main.qcloudimg.com/raw/f36326611c44fcf99ed1f09cdf7256c7/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_5834ae3b-4201-4c75-8e51-5e884e2d6207.png)

2. 主账号授权
	1. 主账号 CompanyExample 登录 [CAM 控制台](https://console.cloud.tencent.com/cam)。
	2. 在左侧导航中，单击【用户】>【用户列表】>【授权】。在页面【关联策略】中搜索 QcloudCLSFullAccess 和步骤1中建立的策略，如 CLSListCosCKafka ，并选中关联这两个策略，单击【完成】即可。
   ![企业微信截图_ed5d6bba-9cba-480d-9b30-210184865564](https://main.qcloudimg.com/raw/90aee492c0ac993dbf75625d59ea6496/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_ed5d6bba-9cba-480d-9b30-210184865564.png)

3. 子账号访问
   子账号 Developer 可通过登录控制台及 API 访问 CLS 服务。需要注意的是，API 访问时需使用主账号 CompanyExample 的 uin，子账号 Developer 的 SecretId、SecretKey。子账号的 API 密钥可参考 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。

