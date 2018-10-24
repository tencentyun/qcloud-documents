可以，但是有两个前提条件：
1. 只能在该 VPC 所在地域的可用区下创建。比如，您的 VPC 所属地域是广州，那么您可以创建广州二区和三区的云服务器，但是您不可以在该 VPC 中同时创建广州二区和北京一区的云服务器，<a href="https://cloud.tencent.com/doc/product/215/4927#.E5.8F.AF.E7.94.A8.E5.8C.BA.EF.BC.88zone.EF.BC.89" target="_blank">单击查看地域和可用区分布详情</a>
2. 在某可用区创建云服务器，必须先创建该可用区的子网。

在不同可用区创建云服务器具体操作步骤如下：
1. 在该 VPC 下的**不同**可用区 <a href="https://cloud.tencent.com/doc/product/215/4927#.E6.96.B0.E5.A2.9E.E5.AD.90.E7.BD.91" target="_blank">创建子网</a>。
2. 创建云服务器。在 <a href="https://console.cloud.tencent.com/vpc/subnet" target="_blank">子网控制台</a> 内购买云服务器 / 在 <a href="https://cloud.tencent.com/product/cvm.html" target="_blank">云服务器介绍页</a> 购买网络配置中选择**不同可用区**的子网。
