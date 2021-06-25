登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus)，创建 ETL 作业后，在【作业管理】中单击要进行开发的作业名称，然后单击【开发调试】，即可在草稿状态下进行作业开发。【作业草稿】即表示当前正处于可编辑的草稿状态下。

## 添加数据源表和目的表
开发 ETL 作业需在 数据源表和数据目的表中创建表。单击【添加】可以快速在编辑器中插入常用的 [MySQL](https://cloud.tencent.com/document/product/849/52698) 或 [ClickHouse](https://cloud.tencent.com/document/product/849/53389) 等数据流的表。
![](https://main.qcloudimg.com/raw/9f54a771afbb42c0dab56e3ed38979a1.png)


## 配置字段映射
添加数据源表和目的表完成后，下拉可以配置字段映射。单击“字段映射”右侧的刷新图标，即可读取数据源表中存在的字段。编辑映射到目的表的字段名称就可以完成配置。如果有“常量字段”或“计算字段”的需求，单击左下角【添加】，然后填写相应信息即可，此处将 weight 数值 * 2，映射到目的表中的 weight 字段。
![](https://main.qcloudimg.com/raw/772293f5a5d71c452c2a7523f002dae4.png)
配置完毕后，单击【作业参数】，在页面右侧弹出的参数界面中设置参数值，具体可参考 [作业参数](#id)。然后单击【确定】，保存数据源表和目的表和作业参数。
![](https://main.qcloudimg.com/raw/7175ab25a1e912e7b0536c531bca4504.png)

[](id:id)
## 作业参数
### Checkpoint
Checkpoint 即作业快照，开启 Checkpoint 之后作业会按照设置的时间间隔自动保存作业快照，用于遇到故障时作业的恢复。可设置 Checkpoint 的时间间隔，设置范围在30秒 - 3600秒。

### 算子默认并行度
用户指定的整个作业的算子默认并行度。1个并行度将占用1CU计算资源。
