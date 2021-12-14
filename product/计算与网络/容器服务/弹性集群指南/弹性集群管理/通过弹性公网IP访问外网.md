
目前 EKS 已经支持在 Pod 中绑定 EIP ，只需在 template annotation 中说明即可。详情请参见 [Annotation 说明](https://cloud.tencent.com/document/product/457/44173) 文档。

跟 EIP 有关的 Annotation 标识共有四个：

| Annotation Key                                      | Annotation Value 及描述                                      | 是否必填                      |
| --------------------------------------------------- | ------------------------------------------------------------ | ----------------------------- |
| `eks.tke.cloud.tencent.com/eip-attributes`          | 表明该 Workload 的 Pod 需要关联 EIP，值为 `""` 时表明采用 EIP 默认配置创建。 `""` 内可填写 EIP 云 API 参数 json，实现自定义配置。 | 如需绑定 EIP ，则此项为必填项 |
| `eks.tke.cloud.tencent.com/eip-claim-delete-policy` | Pod 删除后，EIP 是否自动回收，Never 不回收，默认回收。          | 否                            |
| `eks.tke.cloud.tencent.com/eip-injection`           | 值为 "true" 时，表明会在 Pod 内暴露 EIP 的 IP 信息. 在 Pod 内使用 `ip addr` 命令可以查看到 EIP 的地址。 | 否                            |
| `eks.tke.cloud.tencent.com/eip-id-list`             | 表明使用存量 EIP，仅支持 statefulset。默认销毁 Pod 不会回收 EIP。注意，statefulset pod 的数量最多只能为此 Annotation 中指定 eipId 的数量。 | 否                            |

1. 如需为 Workload 或 Pod 绑定 EIP 访问公网，最简单的方式就是在对应 Workload 或 Pod 的 `annotation` 下，添加标识 `eks.tke.cloud.tencent.com/eip-attributes: ""` 。示例如下：
<dx-codeblock>
:::  yaml
metadata:
  name: tf-cnn
  annotations: 
    eks.tke.cloud.tencent.com/eip-attributes: ""  #需求EIP，配置均为默认
:::
</dx-codeblock>
2. 运行后执行以下命令查看事件：
```sh
kubectl describe pod [name]
```
可以发现多了两行跟 EIP 有关的事件，如下图所示，说明成功运行。
![](https://main.qcloudimg.com/raw/41f3957b664b1dbfee1ade405d522560.png)
3. 查看 log 文件也发现能正常下载数据集。如下图所示：
![](https://main.qcloudimg.com/raw/e0e02f6c1ec047bc09ead5f6259aad1f.png)
>!**EIP 的申请每天有限额**，不适用于需要多次运行的任务。具体限额请参见 [为什么无法申请 EIP](https://cloud.tencent.com/document/product/1199/41745#11) 常见问题说明。
