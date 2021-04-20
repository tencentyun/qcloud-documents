高可用虚拟 IP 与普通内网 IP 类似，均支持在控制台绑定或解绑 EIP，如果您有公网通信的需求，可参考本文为其绑定 EIP。如您没有公网通信的需求，可跳过本章节。

## 绑定 EIP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择【IP 与网卡】>【高可用虚拟 IP】。 
2. 在 HAVIP 管理页面，选择所在地域。
3. 选择待绑定 EIP 的 HAVIP，单击右侧操作列的【绑定】。
    ![](https://main.qcloudimg.com/raw/8ff34853fe60fa3ec2d9010df1bd3bbf.png)
4. 在弹出的【绑定弹性公网 IP】对话框中，单击需要绑定的 EIP。
    >!
    >+ 如无可用的 EIP，请先在 EIP 控制台创建 EIP 后再执行绑定操作，一个 HAVIP 只能绑定一个 EIP。
    >+ 如果 HAVIP 未绑定到云服务器实例上，绑定此 HAVIP 的 EIP 将处于【闲置】状态，系统会收取资源闲置费用。因此，请正确配置高可用，确保绑定成功。常见配置案例请参考：
    >  + [最佳实践 - 用 HAVIP + Keepallved 搭建高可用主备集群](https://cloud.tencent.com/document/product/215/20186)
    >  + [最佳实践 - 用 HAVIP + Windows Server Failover Cluster 搭建高可用 DB](https://cloud.tencent.com/document/product/215/20187) 
5. 单击【确定】完成 EIP 的绑定。
     ![](https://main.qcloudimg.com/raw/7b96dd411d694326603aac3035e75329.png)

## 解绑 EIP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择【IP 与网卡】>【高可用虚拟 IP】。 
2. 在 HAVIP 管理页面，选择所在地域。
3. 选择待解绑 EIP 的 HAVIP，单击右侧操作列的【解绑】。
4. 在弹出的【解绑弹性公网 IP】对话框中，请知悉如下风险，确认无误后，单击【确定】完成 EIP 的解绑。
   >!
   >+ 解绑 EIP 会影响公网业务，请评估业务影响并做好准备。
   >+ 解绑后的 EIP 将处于闲置状态，系统会收取资源闲置费用，如不需要，可直接 [释放 EIP](https://cloud.tencent.com/document/product/1199/41704)。
   >
 <img src="https://main.qcloudimg.com/raw/dfaef505c93aa5c72e1b23e9516a9cec.png" width="50%" />
