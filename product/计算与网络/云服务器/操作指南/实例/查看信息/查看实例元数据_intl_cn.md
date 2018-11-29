实例元数据是有关您运行的实例的数据，可以用来配置或管理正在运行的实例。

>注：虽然只能从实例自身内部访问实例元数据，但数据并未进行加密保护。可访问实例的人员均可查看其元数据。因此，您应当采取适当的预防措施来保护敏感数据（例如使用永久加密密钥）。

## 实例 meta-data
腾讯云现在提供如下meta-data信息：

| 数据 | 描述 | 引入版本 |
|---------|---------|---------|
| instance-id | 实例 ID | 1.0 |
| uuid | 实例 ID | 1.0 |
| local-ipv4 | 实例内网 IP | 1.0 |
| public-ipv4 | 实例公网 IP | 1.0 |
| mac | 实例 eth0 设备 mac 地址 | 1.0 |
| placement/region | 实例所在地域信息 | 1.1 |
| placement/zone | 实例所在可用区信息 | 1.1 |
| network/network/macs/**mac**/mac | 实例网络接口设备地址 | 1.2 |
| network/network/macs/**mac**/primary-local-ipv4 | 实例网络接口主内网 IP 地址 | 1.2 |
| network/network/macs/**mac**/public-ipv4s | 实例网络接口公网 IP 地址 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/gateway | 实例网络接口网关地址 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/local-ipv4 | 实例网络接口内网 IP 地址 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/public-ipv4 | 实例网络接口公网 IP 地址 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/public-ipv4-mode | 实例网络接口公网网络模式 | 1.2 |
| network/network/macs/**mac**/local-ipv4s/**local-ipv4**/subnet-mask | 实例网络接口子网掩码 | 1.2 |

> 以上表格中粗体 **mac** 和 **local-ipv4** 字段分别表示实例指定网络接口的设备地址和内网 IP 地址。
> 
> 请求的目标URL地址，大小写敏感。请严格按照请求的返回结果来构造新请求的目标URL地址。

## 查询实例元数据
对实例元数据的操作均只能从**实例内部**进行。请先完成实例登录操作。有关登录实例的更多内容，请参考 [登录 Windows 实例](/doc/product/213/5435) 和 [登录 Linux 实例](/doc/product/213/5436)。

### 查询已提供的所有meta-data类型
命令：
```
curl http://metadata.tencentyun.com/
```
返回值如下
![](//mccdn.qcloud.com/img56a1ebcbd924d.png)

命令：

```
curl http://metadata.tencentyun.com/meta-data
```
返回值如下
![](//mccdn.qcloud.com/img56a1ed1128bd4.png)

其中placement字段包括region和zone两种数据。

命令：

```
curl http://metadata.tencentyun.com/meta-data/placement
```
返回值如下
![](//mccdn.qcloud.com/img56a1edb2b1349.png)



### 查询实例内网IP
命令：
```
curl http://metadata.tencentyun.com/meta-data/local-ipv4
```
返回值如下
![](//mccdn.qcloud.com/img56a1eeb9557a8.png)

### 查询实例公网IP
命令：
```
curl http://metadata.tencentyun.com/meta-data/public-ipv4
```
返回值如下
![](//mccdn.qcloud.com/img56a1f015c48e5.png)

### 查询实例ID
命令：
```
curl http://metadata.tencentyun.com/meta-data/instance-id
```
或
```
curl http://metadata.tencentyun.com/meta-data/uuid
```
返回值如下
![](//mccdn.qcloud.com/img56a1f1c703176.png)
![](//mccdn.qcloud.com/img56a1f35d0bb18.png)

### 查询实例eth0设备地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/mac
```
返回值如下
![](//mccdn.qcloud.com/img56a1f2800a4e2.png)

### 查询实例所在地域
命令：
```
curl http://metadata.tencentyun.com/meta-data/placement/region
```
返回值如下
![](//mccdn.qcloud.com/img56a1f3ecd50a2.png)

### 查询实例所在可用区
命令：
```
curl http://metadata.tencentyun.com/meta-data/placement/zone
```
返回值如下
![](//mccdn.qcloud.com/img56a1f45687788.png)

### 查询实例网络接口
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/ca12b20583f602d75a541d1a43452c2d/8.1.jpg)

命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/ced32a2fee5e5282cd038d4034fb11a0/8.2.jpg)

### 查询实例网络接口详细信息
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/4ee3cd5e1bcba00e846282aab4e352a0/9.jpg)

### 查询实例网络接口内网IP地址列表
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/8a7e0b0e41a65b683f2f530131a45d07/10.jpg)

### 查询实例网络接口设备地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/mac
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/0627af2fbc1aada52f5821f92d200f44/11.jpg)

### 查询实例网络接口内网 IP 地址列表
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/primary-local-ipv4
```
返回值如下：
![](https://mc.qcloudimg.com/static/img/5458ecf47ec14ba9151e95d7eaa2efd4/12.jpg)

### 查询实例网络接口公网 IP 地址列表
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/public-ipv4s
```
返回值如下：
![](https://mc.qcloudimg.com/static/img/19fa044afd25b8714b38312c7b3eef6c/13.jpg)

### 查询实例网络接口网络信息
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/5c0b23aa98661c533b2ee9cfae3a79cd/14.jpg)

### 查询实例网络接口网关地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/gateway
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/d297cd00f025c845111a50ee9874612d/15.jpg)

### 查询实例网络接口内网 IP 地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/local-ipv4
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/24470fccb042eb877763a03100da8a10/16.jpg)

### 查询实例网络接口公网 IP 地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/public-ipv4
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/c0344e7c89ab0643884d8ac2b859711b/17.jpg)

### 查询实例网络接口公网网络模式
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/public-ipv4-mode
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/115617733703e99602627bb3ce1f32cc/18.jpg)

> 备注：
- NAT: Network Address Translation，网络地址转换。
- direct: 直通网络，通过实例网络接口的公网IP地址直接路由访问公网。

### 查询实例网络接口子网掩码
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/subnet-mask
```
返回值如下:
 ![](https://mc.qcloudimg.com/static/img/ca9589a75e2a04859e3004e4b72ee967/19.jpg)
