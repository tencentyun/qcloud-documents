## 操作场景

腾讯云容器服务提供升级 Kubernetes 版本的功能，通过该功能可以为您运行中的 Kubernetes 集群进行升级。

## 注意事项

- 升级集群时，需要先升级 Master 再升级 Node。
- 升级节点时，将会驱逐节点上运行的 Pod。建议升级节点前，预先新建合适配置的节点，保证集群有足够的资源用于存放被驱逐的 Pod。
- 升级节点时，将进行重装系统，请提前备份数据。
- 请在升级集群前，查看集群下节点是否均是健康状态。若节点不正常，您可以自行修复，也可以通过 [提交工单](https://console.qcloud.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1TKE&step=1) 联系我们协助您进行修复。

## 操作步骤

1. [提交工单](https://console.qcloud.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1TKE&step=1) 联系我们升级 Master 版本。
2. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
3. 在左侧导航栏中，单击【[集群](https://console.cloud.tencent.com/tke2/cluster?rid=4)】，进入 “集群管理” 页面。
4. 在需要升级的集群行中，单击【更多】>【升级集群】。
4. 选择需升级的节点（可分批升级，但最终需要保证集群内所以节点均升级完成），并填写节点相关配置。
5. 单击【完成】，完成升级。您可以在节点列表处查看节点升级的情况。

>? 节点会进行滚动升级，即升级完成上一个节点后才会升级下一个节点。
