## 操作场景
本文介绍如何通过云服务器控制台，为实例配置 HARP 分布式训练环境。


## 操作步骤

### 绑定弹性网卡
弹性网卡数量等于 GPU 卡的数量，例如8卡训练机器则需要绑定8张弹性网卡（加主网卡共9张网卡）。具体步骤如下：

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，选择实例 ID 进入详情页面。
2. 在实例详情页中，选择**弹性网卡**页签，并单击**绑定弹性网卡**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8d0419ff931ace556f31349b420d302b.png)
3. 在弹出的“绑定弹性网卡”窗口中，选择弹性网卡，单击**确认**即可。


### 配置并验证环境
1. 参考 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，登录实例。
2. 执行以下命令，执行配置脚本。
```plaintext
curl -s -L http://mirrors.tencent.com/install/GPU/taco/taco_setup.sh | sudo bash
```
返回结果如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/21cef08fafc066813c250c84ef6fa1f9.png" width="918px"/>
3. 执行以下命令，重启实例。
```plaintext
sudo reboot
```
4. 依次执行以下命令，检查是否配置成功。
 - 检查大页内存是否配置成功：
```plaintext
cat /proc/meminfo | grep HugePages_Total
```
返回如下结果，表示配置成功。
```plaintext
HugePages_Total:      50
```
 - 检查是否产生了配置文件：
```plaintext
ls -l /usr/local/tfabric/tools/config/ztcp*.conf
```
返回结果如下图所示，表示已产生配置文件。
![](https://qcloudimg.tencent-cloud.cn/raw/c779075e6997af803ef4eed17e1958da.png)
