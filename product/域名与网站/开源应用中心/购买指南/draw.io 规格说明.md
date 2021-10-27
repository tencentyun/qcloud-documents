

## draw.io 规格说明
若您在腾讯云开源应用中心正式开通 draw.io 应用实例，将默认使用以下规格云资源：

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
    <td><ul style="margin:0"><li>默认配置2核4GiB内存的容器，伸缩范围0 - 10个实例，遇到 CPU 负载大于60将会进行扩容。无流量则会缩容到0，不产生费用</li><li>使用 “镜像拉取” 方式无构建费用</li></ul></td>
    <td><ul style="margin:0"><li><b>CPU：</b>0.055元/核/小时</li><li><b>内存：</b>0.032元/GiB/小时</li><li><b>流量：</b>0.8元/GB</li><li>具体可查看 <a href= "https://cloud.tencent.com/document/product/1243/47823#.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9">计费说明</a></ul></li></td>
  </tr>
</tbody>
</table>

## 费用计算示例
您在腾讯云开源应用中心使用已正式开通的 draw.io 应用实例，某天使用云托管0.5GB流量以及4小时运行时间，则将产生以下费用：
- **每天预估云托管费用**：2核 × 0.055元/核/小时 × 4小时 + 4GiB × 0.032元/GiB/小时 × 4小时 + 0.8元/GB × 0.5GB = 1.3元（保留小数点后一位）
- **每天预估总费用**：云托管费用 = 1.3元（保留小数点后一位）



