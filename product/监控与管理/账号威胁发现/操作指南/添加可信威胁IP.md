本文为您详细介绍如何管理可信/威胁 IP。

<dx-alert infotype="explain" title="">
- 可信 IP 列表：可信 IP 列表包含已列入白名单的，可与您的腾讯云环境安全通信的 IP 地址。腾讯云不会为可信 IP 列表中包含的 IP 地址生成结果。
- 威胁 IP 列表：威胁 IP 列表包含已知的恶意 IP 地址。腾讯云将为威胁 IP 列表中包含的 IP 地址生成结果。
- 若 IP 地址同时存在可信列表和威胁列表中，将优先按照可信 IP 处理。
</dx-alert>



## 添加列表信息
1. 将 IP 地址或 CIDR 地址一行一个，写入 TXT 文件并保存。
![](https://main.qcloudimg.com/raw/2460c1616bd24313237517a89e17145e.png)
2. 将上述 TXT 文件上传至公有读的 COS 即可。具体操作请参见 [上传对象](https://cloud.tencent.com/document/product/436/13321) 。
3. 单击对象右侧**详情**，进入对象详情页。
![](https://main.qcloudimg.com/raw/1582a5954a13d0ffed85753eebd6fecd.png)
4. 复制 COS 文件 URL。
![](https://main.qcloudimg.com/raw/2c97efe3a6a7f76761cfb39de6040636.png)
5. 登录 [威胁发现控制台](https://console.cloud.tencent.com/developer-security/threat-discovery)，单击左侧菜单栏的 **IP 清单**。
6. 根据需求，单击**添加可信 IP 列表**或**添加威胁 IP 列表**。
7. 进入弹窗填写列表名称、列表文件 URL，选择格式和同意协议。
	- 列表名称：填写名称，不可与列表中的其它名称重复。
	- 列表文件 URL：将步骤4复制的 URL，填写到此处。
	- 选择格式：目前仅支持 TXT 格式。
	- 同意协议：通过添加列表，表明您接受并同意威胁发现从此资源读取数据。
![](https://main.qcloudimg.com/raw/de12bfb5c763a0edec4826eba0d0f035.png)
8. 单击**提交**，等待状态跳转为“ACTIVE”，即添加成功。
![](https://main.qcloudimg.com/raw/25cb45dfbca8e1930c6374b0ab5adeef.png)

## 修改列表信息
单击列表右侧对应的**编辑**，即可修改列表信息。	
<dx-alert infotype="notice" title="">
若修改了 COS 文件中的 IP 列表，需要通过编辑来重新激活。
</dx-alert>


## 禁用与激活列表信息
- 在生效状态下，单击列表右侧对应的**禁用**，即可禁用 COS 文件。
- 在未生效状态下，单击列表右侧对应的**激活**，即可重新激活 COS 文件。

## 删除列表信息
1. 单击列表右侧对应的**删除**，将弹出对话框。
2. 单击**确定**，即可删除列表信息。


