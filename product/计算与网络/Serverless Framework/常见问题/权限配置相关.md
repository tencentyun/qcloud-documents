### 报错“The appid is unavailable for legal reasons” 如何处理？
该报错是由于账户欠费，无法创建新的后付费资源所导致的。请您检查账户是否欠费，将账户充正后即可解决。

### 报错“you are not authorized to perform operation resource has no permission”如何处理？
该报错是由于账号本身或调用角色 SLS_QcsRole 缺少相关权限导致的，请根据报错信息，确定缺少的策略，再通过 [访问管理控制台](https://console.cloud.tencent.com/cam)，将缺少的策略赋予账号以及角色 SLS_QcsRole。
报错信息示例：
```
 [request id:xxxxx]you are not authorized to perform operation (scf:CreateFunction) resource (qcs::scf:gz:uin/xxxxxx:function/*) has no permission
```
从报错信息可知，缺少 `scf:CreateFunction` 的权限，因此需要登录控制台，为对应的账号与角色 SLS_QcsRole 赋予 `SCFFullAccess` 的策略。

### 子账号缺少权限该如何处理？
参考 [子账号权限配置说明](https://github.com/AprilJC/Serverless-Framework-Docs/blob/main/docs/%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8/%E6%9D%83%E9%99%90%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E.md#%E5%AD%90%E8%B4%A6%E5%8F%B7%E6%9D%83%E9%99%90%E9%85%8D%E7%BD%AE)。
