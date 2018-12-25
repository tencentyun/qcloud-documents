## 通过 phpMyAdmin 控制台的图形界面
### 删除数据库

1. 进入 phpMyAdmin 控制台后（如何进入 phpMyAdmin 控制台请参见  [访问MySQL数据库](https://cloud.tencent.com/document/product/236/3130#.E5.A4.96.E7.BD.91.E8.AE.BF.E9.97.AE)），单击需要管理的数据库名称，进入数据库管理界面，单击【操作】按钮。如下图所示：
![](https://main.qcloudimg.com/raw/203db68053996f10322b58bd3d39a888.png)

2. 在此页面可以对数据库进行【新建数据表】、【重命名】、【删除数据库】等一系列操作。单击【删除数据库（DROP）】即完成数据库的删除操作。如下图所示：
![](https://main.qcloudimg.com/raw/437ffd41974ec6b22b11611609cd830b.png)


### 删除数据表
1. 选择需要删除表的数据库，在此页面可以对数据表进行【浏览】、【结构】、【搜索】、【删除】等一系列操作。单击【删除】按钮，如下图所示：
![](https://main.qcloudimg.com/raw/d346cd292ccadfbab50d9577332c19d2.png)


## 通过 phpMyAdmin 控制台的 SQL 命令
### 删除数据库
 1. 进入 phpMyAdmin 控制台后（如何进入 phpMyAdmin 控制台请参见 [访问MySQL数据库](https://cloud.tencent.com/document/product/236/3130#.E5.A4.96.E7.BD.91.E8.AE.BF.E9.97.AE)），通过 SQL 命令删除数据库，单击【SQL】按钮。如下图所示：

 ![](https://main.qcloudimg.com/raw/ff144c310615f66b914fd907f32b656b.png)

 2. 执行如下删除数据库命令：
 ```
  drop database <database name>；
 ```


 ### 删除数据表
 1. 通过 SQL 命令删除数据表，单击【SQL】按钮。如下图所示：

 ![](https://main.qcloudimg.com/raw/ff144c310615f66b914fd907f32b656b.png)

 2. 执行如下删除数据库命令：
```
 drop table <table name>；
 ```
