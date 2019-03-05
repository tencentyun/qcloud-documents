### 如何查看地域列表？

介绍文档参考：[地域与可用区简介](https://cloud.tencent.com/document/product/213/6091)

#### 通过 API 接口查询：

- [查询地域列表](https://cloud.tencent.com/document/product/213/15708)
- [查询可用区列表](https://cloud.tencent.com/document/product/213/15707)

### 已购买的云服务器可以更换地域吗？

已购买的云服务器不支持更换地域，一个已经启动的实例是无法更改其可用区的。若您有更换地域和可用区的需求，可参考以下两种解决方式：

- 若购买时间在 5 天内， 您可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=7&source=0&data_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM&level3_id=158&radio_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%80%80%E8%BF%98&queue=1&scene_code=12646&step=2) 申请退还服务器。退还前请提前做好数据备份，退还后重新选购服务器即可。
- 从原始实例创建自定义镜像、使用自定义镜像在新可用区中启动实例以及更新新实例的配置。
  1. 创建当前实例的自定义镜像。有关更多信息，请参阅  [创建自定义镜像](https://cloud.tencent.com/doc/product/213/4942) 。
  2. 如果当前实例的网络环境为 [私有网络](https://cloud.tencent.com/doc/product/213/5227) 且需要在迁移后保留当前内网 IP 地址，用户可以先删除当前可用区中的子网，然后在新可用区中用与原始子网相同的 IP 地址范围创建子网。需要注意的是，不包含可用实例的子网才可以被删除。因此，应该将在当前子网中的所有实例移至新子网。
  3. 使用刚刚创建的自定义镜像在新的可用区中创建一个新实例。用户可以选择与原始实例相同的实例类型及配置，也可以选择新的实例类型及配置。有关更多信息，请参阅 [创建实例](https://cloud.tencent.com/doc/product/213/4855) 。
  4. 如果原始实例有关联的弹性公网 IP 地址，则将其与旧实例解关联并与新实例相关联。有关更多信息，请参阅  [弹性公网 IP](https://cloud.tencent.com/doc/product/213/5733) 。
  5. （可选）若原有实例为 [按量计费](https://cloud.tencent.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9) 类型，可选择销毁原始实例。有关更多信息，请参阅  [销毁实例](https://cloud.tencent.com/doc/product/213/4930)。若原有实例为 [包年包月](https://cloud.tencent.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88) 类型，可选择等待其过期并回收。