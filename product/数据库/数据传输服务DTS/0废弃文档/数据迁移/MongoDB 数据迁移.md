### 新建迁移任务
登录腾讯云 [DTS 控制台](https://console.cloud.tencent.com/dtsnew)，打开【数据迁移】页面单击【新建任务】。

### 选择链路区域
选择您迁移项目链路目标实际所在地区。
>目前 Mongo 数据迁移免费；
>迁移任务订购后不支持更换地域，请谨慎选择。

### 设置源库和目标库
填写任务设置、源库设置和目标库设置等信息。
![](https://main.qcloudimg.com/raw/755ef0b68e3e276a7aef162392cd550d.png)
#### 任务设置
填写迁移任务的名称，如果您希望迁移任务不是马上执行，可以为迁移任务设置定时执行。
![](https://main.qcloudimg.com/raw/f5b1a534bd8253e35a0e0f5eec24777b.png)
#### 源库设置
填入源库信息，信息填完后，您可以单击【测试连通性】测试您的源库是否可以连通。
![](https://main.qcloudimg.com/raw/fedacfd128d3797cf9bda97b5fcaa6c1.png)

#### 目标库设置
填写目标库信息，填完后，单击【保存】。
![](https://main.qcloudimg.com/raw/697c6fbf95a701d596fc17745b269c89.png)

### 选择类型和库表
选择类型和库列表，单击【下一步：校验任务】。
![](https://main.qcloudimg.com/raw/293ea79c8c4228dd424505d66f56ffb5.png)

### 校验任务
校验源实例服务是否正常以及目标实例迁入集合是否冲突。
![](https://main.qcloudimg.com/raw/10c3b4e303786fd1ed2b9963d1a568f8.png)

### 完成迁移
校验通过后，返回迁移任务列表，待增量同步完成100%，单击迁移任务右侧【完成】，方可完成迁移任务。
完成迁移。
![](https://main.qcloudimg.com/raw/54a9916ca7997a475cd4596ea1a61aab.png)
