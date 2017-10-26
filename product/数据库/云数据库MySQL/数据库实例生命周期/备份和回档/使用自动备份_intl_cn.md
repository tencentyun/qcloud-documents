# 使用自动备份


#### 1 自动备份方式
目前，云数据库MySQL支持2种自动备份方式：

1.物理备份，物理数据全拷贝（目前正在邀测中）

2.逻辑备份，SQL语句的备份

#### 2 备份方式设置
在实例列表页，点击实例，进入[备份管理]，再点击[自动备份设置]，即可进行设置备份方式
![][image-1]
![][image-2]

#### 3 备份方式说明
1.逻辑备份支持实例级和库表级下载，物理备份仅支持实例级的下载
2.MySQL低于5.6版本的仅支持逻辑备份



[image-1]:	https://mc.qcloudimg.com/static/img/61eec4f474762057d6956dc61ecc1214/B1.png
[image-2]:	https://mc.qcloudimg.com/static/img/b9d7e7a4297ae93b6ada3a40cfc618b0/111.png