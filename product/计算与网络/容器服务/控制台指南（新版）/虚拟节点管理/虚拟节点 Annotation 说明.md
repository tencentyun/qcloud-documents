

您可通过在 yaml 中定义 annotation 的方式，实现虚拟节点的自定义 DNS 等能力，具体如下：

<table>
<thead>
<tr>
<th width="20%">Annotation Key</th>
<th width="40%">Annotation Value 及描述</th>
<th width="40%">是否必填</th>
</tr>
</thead>
<tbody>
<tr>
<td>eks.tke.cloud.tencent.com/resolv-conf</td>
<td> 容器解析域名时查询 DNS 服务器的 IP 地址列表。例如 <code>nameserver 8.8.8.8</code>。
<br> 可通过 <code>kubectl edit node eklet-subnet-xxxx</code> 添加该 annotation。
<br> 修改后调度到该虚拟节点的 Pod 默认全部采用该 DNS 配置。</td>
<td>否</td>
</tr>
</tr>
</tbody></table>

#### 示例
以下为虚拟节点自定义 DNS 配置的示例：

```
apiVersion: v1
kind: Node
metadata:
  annotations:
    eks.tke.cloud.tencent.com/resolv-conf：|
      nameserver 4.4.4.4
      nameserver 8.8.8.8
   
```



