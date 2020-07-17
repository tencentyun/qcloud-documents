## 创建数据库
1. 进入 phpMyAdmin 控制台后（如何进入 phpMyAdmin 控制台请参见 <a href="https://cloud.tencent.com/document/product/236/3130#.E5.A4.96.E7.BD.91.E8.AE.BF.E9.97.AE" target="_blank">访问MySQL数据库</a>）,单击【新建】或者【数据库】，进入创建数据库页面。如下图所示：
![][image-1]
2. 输入数据库名称，选择排序规则（默认为 utf8_general_ci），单击【创建】即完成了数据库的创建。如下图所示：
![][image-2] 
3. 选择想要操作的数据库，单击上方导航栏中的【操作】按钮，即可进入数据库操作页面，在此页面可以对数据库进行【新建数据表】、【重命名】、【删除数据库】等一系列操作。如下图所示：
![][image-3]

## 创建数据表
1. 选择需要建表的数据库，单击【新建】或者在【新建数据表】栏输入数据表名和选择字段数后单击【执行】，如下图所示：
![][image-4]
2. 进入数据表创建页面后，若需要添加字段，请在【添加】处输入所需添加的字段数，然后单击【执行】。【结构】栏为各字段信息的填写。【PARTITION definition】栏为分区信息（详见 [MySQL分区章节][2]）。请在填写完信息后单击【保存】按钮，即完成数据表的创建。如下图所示：
![][image-5]

[1]:    https://cloud.tencent.com/document/product/236/3130#.E5.A4.96.E7.BD.91.E8.AE.BF.E9.97.AE
[2]:    https://dev.mysql.com/doc/refman/5.6/en/partitioning.html

[image-1]:  https://mc.qcloudimg.com/static/img/d3861e2f034d0fb80e5c9f31d7cdf40f/step1.png
[image-2]:  https://mc.qcloudimg.com/static/img/b4bb4bd4af2a249177568cfce2a96794/step2.png
[image-3]:  https://mc.qcloudimg.com/static/img/06d40e8eebeb0559245c952aa44908b0/step3.png
[image-4]:  https://mc.qcloudimg.com/static/img/453cbaf6185036e8a0687acb27c9edba/step11.png
[image-5]:  https://mc.qcloudimg.com/static/img/af21217417b070500dafe476f3d8605d/step12.png
