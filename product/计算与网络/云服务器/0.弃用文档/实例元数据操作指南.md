对实例元数据的操作均只能从**云主机内部**进行。请先完成云主机登录操作。

## 1. 查询已提供的所有 meta-data 类型
命令：
```
curl http://metadata.tencentyun.com/
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/16ca44e2a77f6204637d41c58106bae0/1.1.jpg)

命令：
```
curl http://metadata.tencentyun.com/meta-data
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/98f7dfb2b963302179d14b380c337908/1.2.jpg)

## 2. 查询本机内网 IP 地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/local-ipv4
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/29c8b724f9b0dd013791b76b392b8515/2.jpg)

## 3. 查询本机公网 IP 地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/public-ipv4
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/479e61f940d534c3a8a3c47ab51e40d1/3.jpg)

## 4. 查询本机 ID
命令：
```
curl http://metadata.tencentyun.com/meta-data/uuid
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/ab13becde6cecd9aa20ecaadf1531b51/4.1.jpg)

命令：
```
curl http://metadata.tencentyun.com/meta-data/instance-id
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/f97d021073490943bedb3b1b7bc592a3/4.2.jpg)

## 5. 查询本机 eth0 设备地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/mac
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/18a9525df29eba8a14e996cfae870171/5.jpg)

## 6. 查询本机所在地域
命令：
```
curl http://metadata.tencentyun.com/meta-data/placement/region
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/6dffc561829ea2bfdb911f1642d8f27b/6.jpg)

## 7. 查询本机所在可用区
命令：
```
curl http://metadata.tencentyun.com/meta-data/placement/zone
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/50ff964c9ced130937b4da50f3d3be80/7.jpg)

## 8. 查询本机网络接口
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

## 9. 查询本机网络接口详细信息
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/4ee3cd5e1bcba00e846282aab4e352a0/9.jpg)

## 10. 查询本机网络接口内网IP地址列表
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/8a7e0b0e41a65b683f2f530131a45d07/10.jpg)

## 11. 查询本机网络接口设备地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/mac
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/0627af2fbc1aada52f5821f92d200f44/11.jpg)

## 12. 查询本机网络接口内网 IP 地址列表
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/primary-local-ipv4
```
返回值如下：
![](https://mc.qcloudimg.com/static/img/5458ecf47ec14ba9151e95d7eaa2efd4/12.jpg)

## 13. 查询本机网络接口公网 IP 地址列表
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/public-ipv4s
```
返回值如下：
![](https://mc.qcloudimg.com/static/img/19fa044afd25b8714b38312c7b3eef6c/13.jpg)

## 14. 查询本机网络接口网络信息
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/5c0b23aa98661c533b2ee9cfae3a79cd/14.jpg)

## 15. 查询本机网络接口网关地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/gateway
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/d297cd00f025c845111a50ee9874612d/15.jpg)

## 16. 查询本机网络接口内网 IP 地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/local-ipv4
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/24470fccb042eb877763a03100da8a10/16.jpg)

## 17. 查询本机网络接口公网 IP 地址
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/public-ipv4
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/c0344e7c89ab0643884d8ac2b859711b/17.jpg)

## 18. 查询本机网络接口公网网络模式
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/public-ipv4-mode
```
返回值如下：
 ![](https://mc.qcloudimg.com/static/img/115617733703e99602627bb3ce1f32cc/18.jpg)

> 备注：
- NAT: Network Address Translation，网络地址转换。
- direct: 直通网络，通过本机网络接口的公网IP地址直接路由访问公网。

## 19. 查询本机网络接口子网掩码
命令：
```
curl http://metadata.tencentyun.com/meta-data/network/interfaces/macs/52:54:00:13:5C:6C/local-ipv4s/10.104.187.40/subnet-mask
```
返回值如下:
 ![](https://mc.qcloudimg.com/static/img/ca9589a75e2a04859e3004e4b72ee967/19.jpg)




