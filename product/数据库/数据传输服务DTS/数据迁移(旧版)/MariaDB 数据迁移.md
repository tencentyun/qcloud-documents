## 准备工作
迁移用户需要具备源数据库的权限，具体包括：RELOAD, PROCESS, REPLICATION SLAVE, LOCK TABLES, REPLICATION CLIENT, SHOW DATABASE, EVENT, SELECT。

如果源数据库的视图需要迁移，还需要具备SHOW VIEW权限。

## 操作步骤
### 1. 新建迁移任务
1）登录 [DTS 控制台](https://console.cloud.tencent.com/dts )，在数据迁移页，单击**新建迁移任务**。
2）在**链路地域**选择对应地域，单击**0元购买**。
>?迁移任务订购后不支持更换地域，请谨慎选择。

### 2. 设置源库和目标库
填写任务设置、源库设置和目标库设置等信息。

#### 任务设置
填写迁移任务的名称，如果您希望迁移任务不是马上执行，可以为迁移任务设置定时执行。
![](https://main.qcloudimg.com/raw/f5b1a534bd8253e35a0e0f5eec24777b.png)

#### 源库设置
填入源库信息，信息填完后，您可以单击**测试连通性**测试您的源库是否可以连通。
![](https://main.qcloudimg.com/raw/4a7070511fbde9cf4a5a207b6c1ee54e.png)

#### 目标库设置
填写目标库信息，填完后，单击**保存**。
![](https://main.qcloudimg.com/raw/93270ca13f74cac2f86012fd9df46549.png)

### 3. 选择类型和库表
选择类型和库列表，单击**下一步：校验任务**。
![](https://main.qcloudimg.com/raw/d9cda12bdba712013197a2434b7b0562.png)

### 4. 校验任务
校验源实例服务是否正常以及目标实例迁入集合是否冲突。
![](https://main.qcloudimg.com/raw/ff67c3ca23243c5759ec78ab061f6411.png)

### 5. 完成迁移
校验通过后，返回迁移任务列表，待增量同步完成 90%，单击迁移任务右侧**完成**，方可完成迁移任务。
![](https://main.qcloudimg.com/raw/2770041ad6f24bfe70a8ae64ee1ca30e.png)
完成迁移。
![](https://main.qcloudimg.com/raw/32ba2bfc5a3006da69893f784b9ea2b7.png)

