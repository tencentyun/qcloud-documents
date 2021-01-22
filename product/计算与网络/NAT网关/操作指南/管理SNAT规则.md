当NAT网关绑定多个EIP时，可以通过创建SNAT规则，为不同业务分组的云服务器指定访问公网的EIP。
例如，当NAT网关绑定了EIP1、EIP2、EIP3、EIP4等多个EIP时，则系统会在绑定的所有EIP中自动做负载均衡访问公网。如果将EIP1、EIP2、EIP3加入SNAT地址池，则系统使用SNAT地址池中的EIP访问公网，且自动在SNAT地址池中的EIP中做负载均衡。
本文介绍如何创建SNAT规则及SNAT规则的管理。
## 创建SNAT规则
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击【NAT 网关】，进入 NAT 网关列表页面。
3. 在列表中单击网关 ID 进入详情页。
4. 选择【SNAT规则】标签页 ，进入SNAT规则管理界面。
5. 单击【新建】，弹出【新建SNAT规则】对话框。
7. 设置SNAT规则。
   + 源网段粒度：支持子网和云服务器粒度 。
     + 子网：当选择子网时，子网所关联的路由表必须指向该NAT网关，该子网内的云服务器均按照SNAT规则访问外网。
     + 云服务器：当选择云服务器时，云服务器所在子网所关联的路由表必须指向该NAT网关，只有选定的云服务器按照SNAT规则访问外网。
   + 所属子网：选择子网，或云服务器所在子网。
   + 云服务器：仅当【源网段粒度】为【云服务器】时，需要指定云服务器，可添加多个云服务器。
   + 公网IP：指定访问公网的弹性公网IP。
   + 描述：自定义描述信息，最多支持60个字符。
![](https://main.qcloudimg.com/raw/e62bc5bbeb32946ec0dcb2a826e264ff.png)
![](https://main.qcloudimg.com/raw/6d7cfff1507c9442b70ad008f72cb892.png)
8.  完成SNAT规则的参数设置后，单击【提交】。    

## 编辑SNAT规则
>?修改存量SNAT规则中的公网IP，可能导致原有业务连接中断，重连后即可恢复，请谨慎操作。

1. 单击SNAT规则条目右侧的【编辑】，进入编辑对话框。
![](https://main.qcloudimg.com/raw/079de2a5646a23ff058059e2a2d709ab.png)
2. 修改SNAT规则中的公网IP地址或描述，然后单击【提交】完成修改。
3. 描述信息可单击SNAT规则中的描述信息旁的编辑图标，直接进行修改。
    ![](https://main.qcloudimg.com/raw/64525964961cc447f448819213b0ff8e.png)

## 查询SNAT规则
1. 在SNAT规则管理界面右上方的搜索框中，单击选择如下筛选条件，并在输入框中填写相应的参数值。
![](https://main.qcloudimg.com/raw/ebc799f1bbea1db44e8f56e442dfe1bd.png)
2. 单击搜索图标进行快速检索。
![](https://main.qcloudimg.com/raw/2532ac12b4f67600994aa32bf15530a1.png)
3. 单击子网/云服务器ID，可跳转到相应资源详情界面。


## 删除SNAT规则
如果您不需要为云服务器访问外网指定EIP，可删除SNAT规则。
1.  单击SNAT规则条目右侧的【删除】，进入确认删除对话框。
![](https://main.qcloudimg.com/raw/c5740afa666f3a9791e8464dcb622987.png)
2.  确认后，单击【确认】完成该条SNAT规则的删除。
3.  也可勾选多条SNAT规则，再单击上方的【删除】进行批量删除。
![](https://main.qcloudimg.com/raw/701ada78ef333aa47c547e8a77525376.png)