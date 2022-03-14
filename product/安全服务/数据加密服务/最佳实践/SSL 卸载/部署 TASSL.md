文本主要介绍 TASSL 引擎包的使用方法。

## 操作步骤
1. 将 `tasshsm_engine.tgz` 上传至 CVM2 上并解压，下述以解压至 `/root/tasshsm_engine` 为例。
2. 配置 TASSL 引擎要访问的 EVSM 信息，根据使用的算法选择如下任意一种。
 - 使用 RSA 算法
编辑 `/root/tasshsm_engine/cfg/tasshsm_rsa_engine.ini` 将其中的 IP 和 PORT，设置为 EVSM 的地址和主机服务端口号。
![](https://qcloudimg.tencent-cloud.cn/raw/0762663a5ac6cddcd2ee1abdab9c5302.png)
 - 使用国密 SM2 算法
编辑 `/root/tasshsm_engine/cfg/tasshsm_sm2_engine.ini` 将其中的 IP 和 PORT，设置为 EVSM 的地址和主机服务端口号。
![](https://qcloudimg.tencent-cloud.cn/raw/0762663a5ac6cddcd2ee1abdab9c5302.png)
 - 使用 ECC 算法
编辑 `/root/tasshsm_engine/cfg/tasshsm_ecc_engine.ini` 将其中的 IP 和 PORT，设置为 EVSM 的地址和主机服务端口号。
![](https://qcloudimg.tencent-cloud.cn/raw/0762663a5ac6cddcd2ee1abdab9c5302.png)
