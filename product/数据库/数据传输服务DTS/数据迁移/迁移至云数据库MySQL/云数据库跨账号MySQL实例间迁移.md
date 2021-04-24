
本文主要介绍通过 DTS 数据迁移功能实现从其他账号腾讯云数据库实例迁移数据至本账号下云数据库实例。

## 准备工作
在源端云数据库实例所属腾讯云账号中配置，将目标实例所属云账号作为授信云账号，允许通过数据传输服务访问源实例所属云账号的相关云资源。完成权限授权后，即可配置跨账号云数据库迁移任务。

### 授权账号
1. 使用源端云数据库实例所属的腾讯云账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam/role)，进入角色管理页面，单击【新建角色】。
2. 在选择角色载体页面，选择【腾讯云账号】方式。
![](https://main.qcloudimg.com/raw/937dad52c8b9c9dee558a22f7ed20e5c.png)
3. 在输入角色载体信息页面，配置相关信息，单击【下一步】。
 - 云账号类型：选择【其他主账号】。
 - 账号 ID：填入目标端所属的腾讯云账号 ID，账号 ID 可在 [账号信息](https://console.cloud.tencent.com/developer) 页面查看。
![](https://main.qcloudimg.com/raw/3892938446a46262f55e471dcc8516ae.png)
4. 在配置角色策略页面，选择【QcloudDTSReadOnlyAccess】策略，单击【下一步】。
![](https://main.qcloudimg.com/raw/ee4a145a7156e5823573951e0bdf0f56.png)
5. 在审阅页面，设置角色名称，单击【完成】后该角色创建完成。
![](https://main.qcloudimg.com/raw/1e1a0d270955967785c6a4ef9f50ae48.png)

### 策略定义
QcloudDTSReadOnlyAccess 策略定义如下，如果没有找到默认策略，用户也可以在策略管理页面中进行创建。
![](https://main.qcloudimg.com/raw/fee455d79706b2f65c6db28136c4f21d.png)
策略 json 语法如下：
```
{
    "version": "2.0",
    "statement": [
          {
               "action": [
                    "dts:Describe\*"
                ],
                "resource": "\*",
                "effect": "allow"
          }
     ]
}
```
完成权限授权后，即登录 [DTS 数据迁移控制台](https://console.cloud.tencent.com/dts/migration) 配置跨账号云数据库迁移任务。

