>? 目前弹性公网 IPv6 处于内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/c28sebss8v)。

## 开通 IPv6 公网
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性公网 IPv6】。
3. 选择需要开通 IPv6 公网的地域，如“华东地区（上海）”，单击【申请】，进入“申请弹性公网IPv6”页面。
4. 勾选需要开通 IPv6 公网的 IPv6 地址、目标带宽上限	，单击【提交】。
>?
>- 当运营商类型为 BGP 时，弹性公网 IPv6 地址即为弹性网卡获取到的 IPv6 地址，所以请确保弹性网卡已经获取到 IPv6 地址。
>- 单次操作可支持最多100个 IPv6 地址同时开通公网，如果超过100个 IPv6 地址需要开通公网，请分多次操作。
>
![](https://main.qcloudimg.com/raw/4c44f21f529e36adec4d12e9222a3d70.png)

## 关闭 IPv6 公网
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性公网 IPv6】。
3. 在弹性公网 IPv6 列表页，勾选需要关闭公网的 IPv6 地址，并单击【释放】。
![](https://main.qcloudimg.com/raw/2acd79fecc8022c2853fd138dccb2675.png)
4. 在弹窗中勾选【确定关闭以上 IP】并单击【确定】，即可释放弹性公网 IPv6。释放弹性公网 IPv6 后，对应的 IPv6 地址将关闭公网访问。


## 调整 IPv6 公网带宽
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择【IP 与网卡】>【弹性公网 IPv6】。
6. 在单个弹性公网 IPv6 的操作栏下，单击【调整带宽】。
![](https://main.qcloudimg.com/raw/6a229b67fd67f24fe896ac53517cbe29.png)
7. 在弹窗中，修改该弹性公网 IPv6 的公网带宽上限并单击【调整】即可。
![](https://main.qcloudimg.com/raw/a5570432079723d0728fcff0039766d2.png)
