
企业账号 CompanyExample 下有一个子账号 Developer，该子账号需要通过控制台及 API 拥有对企业账号 CompanyExample 下的日志主题 -TopicA 有日志采集上传至 CLS 权限，其中包括使用 Loglistener 与 API 采集。

## 准备工作

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。创建子账号 Developer，详细操作请参考 [自定义创建子用户](https://cloud.tencent.com/document/product/598/13674)。
2. 在新建用户页面，单击【自定义创建】，进入选择用户类型页面，单击 **【可访问资源并接收消息】**。
3. 单击【下一步】，进入填写用户信息页面，选中**【编程访问】**及【**腾讯云控制台访问**】。


## 操作步骤

分为三个步骤：主账号创建自定义策略、主账号 CompanyExample 给子账号 Developer 授权预设权限、子账号 Developer 访问 CLS 日志服务。
1. 创建自定义策略

 1. 主账号 CompanyExample 登录 [CAM 控制台](https://console.cloud.tencent.com/cam)。
 1. 在左侧导航中，选择【策略】>【新建自定义策略】>【按策略语法创建】>【空白模版】建立新策略，如名称为 CLS-TopicA-Pushlog，并在【策略内容】中输入策略，参考以下内容：
```plaintext
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cls:pushLog"
            ],
            "resource": "qcs::cls:ap-guangzhou:uin/100004375281:topic/002dbab1-fcf2-4ca7-b602-fda10d5e1731",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": [
                "cls:listLogset",
                "cls:getConfig",
                "cls:agentHeartBeat"
            ],
            "resource": "*"
        }
    ]
}
```
>?resource 字段需要用户根据实际信息进行修改：地域信息、uin 表示主账号、topic 为日志主题 ID。
>

2. 主账号授权

 1. 主账号 CompanyExample 登录 [CAM 控制台](https://console.cloud.tencent.com/cam)。
 1. 在左侧导航中，单击【用户】>【用户列表】>【授权】。在页面【关联策略】中搜索步骤1中建立的策略（CLS-TopicA-Pushlog），并选中关联这个策略，单击【完成】即可。
      
3. 子账号访问
子账号 Developer 可通过登录控制台及 API 访问 CLS 服务。需要注意的是，API 访问时需使用主账号 CompanyExample 的 uin, 子账号 Developer 的 SecretId、SecretKey。子账号的 API  密钥可参考 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。
