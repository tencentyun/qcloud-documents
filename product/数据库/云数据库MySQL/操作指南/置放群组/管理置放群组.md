
<span id = "xinjian_qunzu"></span>
## 创建置放群组
1.	登录 [MySQL 控制台](https://console.cloud.tencent.com/mysql/placement-group)，在左侧导航选择【置放群组】，选择地域，然后单击【新建】。
![](https://main.qcloudimg.com/raw/0078a3f326ef2d2850baf7f1cb4fc09d.png)
2.	在弹出的对话框，指定置放群组名称和备注信息，单击【确定】即可。
![](https://main.qcloudimg.com/raw/0f34570172b78aa75aa13990f5417f79.png)

## 创建实例及配置置放群组
1.	登录 [MySQL 购买页](https://buy.cloud.tencent.com/cdb)。
2.	在购买页选择各项配置后，单击【立即购买】。
 -  **置放群组**：选择已有置放群组，如置放群组不存在或不合适，可重新 [创建置放群组](#xinjian_qunzu)。
 -  **购买数量**：需要在该置放群组中添加的总实例数，总实例数需 ≤ 50，如需超过50个实例，可 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行反馈。
![](https://main.qcloudimg.com/raw/569958f131f492a913dce915ed5b90c6.png)

## 更改置放群组
>?目前仅支持修改置放群组的名称和备注，修改名称不影响置放群组下已创建的实例。
>
1.	在置放群组页，将鼠标移至置放群组名称或备注，单击<img src="https://main.qcloudimg.com/raw/071659c8118f8c9b94d4ab90cebbd955.png"  style="margin:0;">图标。
![](https://main.qcloudimg.com/raw/56e9ddfccbeb3d7f39b6cc17acac7a63.png)
2.	在弹出的对话框，输入想修改的名称或备注信息，单击【确定】即可。
![](https://main.qcloudimg.com/raw/a63ed76f304491ee13ce00e7fed39bbf.png)


## 删除置放群组
如果您需要替换或不再需要某个置放群组，可在控制台将其删除。删除置放群组前，必须先销毁在置放群组中配置的所有 MySQL 实例。

1. 在 [MySQL 控制台](https://console.cloud.tencent.com/cdb)，销毁置放群组包含的所有 MySQL 实例。
2. 在置放群组页，选择需要删除的置放群组，单击上方的【删除】可批量删除置放群组，单击操作列的【删除】可删除单个置放群组。
![](https://main.qcloudimg.com/raw/81e10cffcd45cce4819f7b8874794d9d.png)
3. 在弹出的对话框，单击【确定】即可。
>?删除后置放群组数据将被清除且不可恢复，请确认后再删除。

