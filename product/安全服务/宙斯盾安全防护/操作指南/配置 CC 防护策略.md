
宙斯盾安全防护（Aegis Anti-DDoS）提供 HTTP CC 高级防护策略，CC 防护策略当设置 HTTP 请求数超过设定的 QPS 值时，才会触发 CC 防护。更详细的配置说明，详情请参见 [**自定义高级安全策略**](https://cloud.tencent.com/document/product/685/18800#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.AE.89.E5.85.A8.E7.AD.96.E7.95.A5)。

## 添加 CC 防护策略
1. 用户进入 [宙斯盾高防控制台](https://console.cloud.tencent.com/gamesec)，在左侧目录中，单击【HTTP CC 防护高级策略】，在 “HTTP CC 防护高级策略” 下，单击【添加新策略】。添加成功后，在 “操作” 列下单击【配置】进入策略配置页面。
![1](https://main.qcloudimg.com/raw/5d245bd6640218fb34c95cb5c6406282.png)
2. 根据业务特点和防护需求配置 HTTP QPS 请求阈值、URL 白名单、IP 黑白名单、CC 自定义防护模式等策略。单击保存即添加策略成功。
![2](https://main.qcloudimg.com/raw/bf27498dfeedd949d9e8c7e9b592f167.png)

## CC 防护策略直接绑定防护 IP
1. 单击【HTTP CC 防护高级策略】，在 “HTTP CC 防护高级策略” 下单击 “策略 ID”。
![3](https://main.qcloudimg.com/raw/10e1054434834930074d0914415febae.png)
2. 单击【绑定 IP 列表】，单击【添加 IP】。
![4](https://main.qcloudimg.com/raw/19176ba621dc3fc5d425ce44440e11ef.png)

## DDoS 高防 IP 绑定 CC 防护策略
1. 单击【DDoS 高防 IP 】，在 “DDoS 高防 IP” 下，选择 “高防 IP”，进入 “DDoS 高防  IP” 详情页。
![5](https://main.qcloudimg.com/raw/069205be880a4ccb459c70267091cf2f.png)
2. 单击 “高级配置信息”。单击【绑定】，选择好 CC 防护策略，单击【确认】。
![6](https://main.qcloudimg.com/raw/0849ec6e4559ce1c58cc379a662b8007.png)

## 给 DDoS 高防包下的防护 IP 配置 CC 防护策略
1.  单击【DDoS 高防包】，在 “DDoS 高防包” 下，选择 “高防包 ID”，进入 “DDoS 高防包” 详情页。
![7](https://main.qcloudimg.com/raw/111d2fe9087038c9931d4065ab4e0666.png)
2. 单击【防护 IP 列表】，勾选需要配置的 IP，单击 “配置 CC 防护策略”。
![8](https://main.qcloudimg.com/raw/860f2dad97b79beb12ef4b687a382de5.png)
