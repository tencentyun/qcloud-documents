仓库提供 Webhook 通知配置，当事件被触发时，通知 Webhook 配置好的 URL。

## 前提条件
登录账号为具有该仓库的 admin（管理）或 write（读写）权限时，才可以编辑 Webhook 配置。

## 新建 Webhook
   
1、登录 [Tencent Hub 控制台](https://console.cloud.tencent.com/tencenthub/store/registry)。
2、单击左侧导航栏中的【仓库管理】，下拉选择对应的【空间】，选择仓库。
3、仓库页面单击【Webhook 通知】。
![](https://main.qcloudimg.com/raw/88863f5ac68580737681b2188570cd78.png)  
4、单击【新建】，填入 Webhook 名、Webhook URL、密钥、Webhook 事件，确定新增。  
![](https://main.qcloudimg.com/raw/85451e59e7c6ef195587d8391efd05bd.png)
5、查看触发记录历史。
![](https://main.qcloudimg.com/raw/1f2d4f3c9d7cb31a901d42d6f261dc19.png)
 Webhook 格式协议
   
```
{
  "repository": {
    "created_at": "2018-06-11T12:59:58Z",   #仓库创建时间
    "updated_at": "2018-06-14T13:19:10Z",   #仓库更新时间
    "namespace": "wadeorg",                 #仓库所属命名空间名字
    "name": "waderepo",                     #仓库名字
    "is_public": false,                     #是否公开。true-公开,false-私有
    "description": "t",                     #仓库的描述
    "summary": "t",                         #仓库的概要
    "labels": ["wade"],                     #仓库的标签
    "has_component": false                  #是否包含组件
    "url": "hub.tencentyun.com/wadeorg/waderepo"                  #镜像地址或二进制文件地址
  },
  "push_data": {
    "pusher": "wade",                       #push的tencenthub用户名
    "pushed_at": "2018-06-14T13:22:48.674902174Z",#push时间
    "tag": "test"                           #tag
  }
}
```



