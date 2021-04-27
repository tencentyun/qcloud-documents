
## WordPress 规格说明
若您在腾讯云开源应用中心正式开通 WordPress 应用实例，将默认使用以下规格云资源：

<table>
<thead>
  <tr>
    <th width="25%">云资源</th>
    <th>规格</th>
    <th width="35%">定价</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>云托管<br>（CloudBase Run）</td>
    <td><ul style="margin:0"><li>默认配置0.25核0.5G内存的容器，伸缩范围0 - 4个实例，遇到 CPU 负载大于60将会进行扩容。无流量则会缩容到0，不产生费用</li><li>使用 “镜像拉取” 方式无构建费用</li></ul></td>
    <td><ul style="margin:0"><li><b>CPU：</b>0.055元/核/小时</li><li><b>内存：</b>0.032元/GiB/小时</li><li><b>流量：</b>0.8元/GB</li><li>具体可查看 <a href= "https://cloud.tencent.com/document/product/1243/47823#.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9">计费说明</a></ul></li></td>
  </tr>
  <tr>
    <td>云原生数据库 TDSQL-C<br>（MySQL for Serverless）</td>
    <td><ul style="margin:0"><li>数据库 1C1G</li><li>算力 Min 0.25/Max 0.5</li><li>存储按照容量计费</li></ul></td>
    <td><ul style="margin:0"><li><b>Serverless 算力价格：</b>0.000095元/个/秒</li><li><b>存储空间价格：</b>0.00485元/GB/小时</li><li>具体可查看 <a href= "https://cloud.tencent.com/document/product/1003/30493">计费说明</a></li></ul></td>
  </tr>
  <tr>
    <td>文件存储（CFS）</td>
    <td>按照实际容量付费，DAU 1000的站点预估消耗量在5GB以下</td>
    <td><ul style="margin:0"><li><b>存储空间0 - 10TB：</b><ul><li>0.35元/GB/月</li><li>0.00048611元/GB/时</li></ul></li><li><b>存储空间10TB以上：</b><ul><li>0.33 元/GB/月</li><li>0.00045833 元/GB/时</li></ul></li><li>具体可查看 <a href= "https://cloud.tencent.com/document/product/1003/30493#.E8.AE.A1.E8.B4.B9.E8.AF.B4.E6.98.8E">计费说明</a></li></ul></td>
  </tr>
</tbody>
</table>

## 费用计算示例
您在腾讯云开源应用中心使用已正式开通的 WordPress 应用实例，某天使用云托管1G流量以及6小时运行时间，文件存储空间为10G，云原生数据库一天中使用了10GB的存储空间，以及在一天的6个小时内，累计使用了个10000个 CCU 的量，则将产生以下费用：

- **每天预估云托管费用**：0.25核 × 0.055元/核/小时 × 6小时 + 0.5G × 0.032元/GiB/小时 × 6小时 + 0.8元/GB × 1G = 1.9元（保留小数点后一位）
- **每天预估存储空间费用**：0.00048611 元/GB/时 × 10GB × 24小时 = 0.1元（保留小数点后一位）
- **每天预估云原生数据库费用**：计算节点费用 + 存储空间费用 = 10000个 x 0.000095元/个/秒 + 0.00485元/GB/小时 × 10GB × 24小时 = 2.1元（保留小数点后一位）
- **每天预估总费用**：云托管费用 + 存储空间费用 + 云原生数据库费用 = 0.9元 + 0.1元 + 2.1元 = 3.1元



