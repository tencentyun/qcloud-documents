[ACL 规则](https://cloud.tencent.com/document/product/215/20088) 是一种子网级别的可选安全层，用于控制进出子网的数据流，可以精确到协议和端口粒度，实现子网粒度流量的精细化控制。您可以为具有相同网络流量控制的子网关联同一个网络 ACL。
本章节介绍通过子网控制台绑定/解绑、更换 ACL 规则的操作指导。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录中单击【子网】，进入子网管理页面。
3. 单击某子网 ID，进入子网详情界面后，可选择在如下任一位置执行 ACL 的绑定/解绑/更换操作。
    + 在基本信息页签下的【关联 ACL】中
    <img src="https://main.qcloudimg.com/raw/fe87d689ee1fa4f6b87e6dfa7ed6f644.png" width="50%" />
    + 在【ACL 规则】页签下
     <img src="https://main.qcloudimg.com/raw/01505eca4a05bf829b2deb29f0db2231.png" width="50%" />
4. 请根据业务需要执行如下操作（此处截图以 ACL 页签操作为例）：
  +  如果当前子网未绑定 ACL 规则，可单击【绑定】，选择合适的 ACL 规则，并单击【确定】完成绑定，绑定后立即生效，此时子网的出入流量只有规则策略为【允许】的流量才能通过。
  <img src="https://main.qcloudimg.com/raw/0bad22697aa3af3b36e866be781027ec.png" width="50%" />
 +  如果当前子网绑定的 ACL 规则不符合业务需要，您可以单击【更换】，更换 ACL 规则，更换后立即生效。
	<img src="https://main.qcloudimg.com/raw/b3b3d8815e2053a0b703f4a03f372aba.png" width="80%" />
 +  如果当前子网绑定了 ACL 规则，但您已不再需要控制子网的出入流量，可以单击【解绑】进行 ACL 规则的解绑。解绑成功后立即生效，此时子网的出入流量无规则限制。
	<img src="https://main.qcloudimg.com/raw/c3e375dca8a91f35cfe7f1087817db8a.png" width="80%" />
    	 
