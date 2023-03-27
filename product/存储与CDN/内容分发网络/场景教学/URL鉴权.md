
## 业务场景
为了防止 URL 被盗刷 CDN 资源而产生高额流量，使用 URL 鉴权方式给 CDN 资源加密以防止被盗刷。


## 具体需求
配置 URL 鉴权域名：`www.qcdntest.cn`
测试资源访问路径：/test.jpg
鉴权密钥：dimtm5evg50ijsx2hvuwyfoiu65
签名参数：sign
有效时间：150s
鉴权范围：指定文件后缀鉴权
文件后辍：jpg;html;css

## 配置步骤
1. 在控制台菜单栏里选择**域名管理**，单击域名右侧**管理**，即可进入域名配置页面**访问控制**中找到鉴权配置，默认情况下，鉴权配置为关闭状态：
<img src="https://qcloudimg.tencent-cloud.cn/raw/ed254bc7a57977416766c4a399aaa82d.png" width="70%">
2. 配置状态打开，弹出配置框进入配置项
鉴权模式可以选择 TypeA、TypeB、TypeC、TypeD 四种模式可以选择，每种模式的访问 URL 格式不同，如下是对于各个模式的URL格式（访问 URL 中不能包含中文）<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/e0dc7ec84c4c275a30f1eee60e5df6f7.png" width="60%"><br>
TypeA：`http://DomainName/Filename?sign=timestamp-rand-uid-md5hash`
TypeB：`http://DomainName/timestamp/md5hash/FileName`
TypeC：`http://DomainName/md5hash/timestamp/FileName`
TypeD：`http://DomainName/FileName?sign=md5hash&t=timestamp`
	- 字段说明
		- DomainName：CDN 域名；
		- Filename：资源访问路径；
		- rand：随机字符串，0 - 100位随机字符串，由大小写字母与数字组成；
		- uid：  0
		- timestamp：  TypeA 使用十进制整型正数的 Unix 时间戳 、TypeB 使用十进制（YYYYMMDDHHMM）格式、TypeC 使用十六进制（Unix 时间戳）、TypeD 可选十或十六进制（Unix 时间戳） ；
		- md5hash：  MD5 格式：TypeA（文件路径-timestamp-rand-uid-自定义密钥）、TypeB（自定义密钥 + timestamp + 文件路径）、TypeC（自定义密钥 + 文件路径 + timestamp）、TypeD（自定义密钥 + 文件路径 + timestamp）；
3. 参数设置
将鉴权密钥、签名参数、有效时间填入对应参数
<img src="https://qcloudimg.tencent-cloud.cn/raw/ccef2008f7d3b2869affe3ae8e40015f.png" width="60%">
4. 配置鉴权的范围<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/dfa7f62c4eb152a3877e4120bbba641e.png" width="60%"><br>
根据业务需求给鉴权对象做鉴权，推荐选择指定文件后辍鉴权，将所有已经配置缓存的静态文件后辍鉴权。

## 测试验证
本次测试使用 TypeA 模式验证，其它模式的测试可参考以上步骤配置。
测试时间：2022年6月27日  11：30
测试 URL：`http://www.qcdntest.cn/test.jpg`


### 验证场景一
带鉴权参数，验证返回结果
打开鉴权计算器将参数填入 获得带鉴权 URL 如下（如是 https 访问需手动调整 https）：
`http://www.qcdntest.cn/test.jpg?sign=1656300600-FnyigRo7yny-0-3276ffbdf30dc974ed955d7db761653a`
执行命令：
```
curl http://www.qcdntest.cn/test.jpg?sign=1656300600-FnyigRo7yny-0-3276ffbdf30dc974ed955d7db761653a -i
```
<img src="https://qcloudimg.tencent-cloud.cn/raw/ad95dc383a89dbadab75ff15ee0990a2.png" width="70%">
带鉴权 URL 的结果返回200状态码，配置生效。

### 验证场景二
未带鉴权参数，验证返回结果
使用不带鉴权参数的 URL， 看测试域名是否能正常访问。
执行命令：
```
curl http://www.qcdntest.cn/test.jpg -i
```
<img src="https://qcloudimg.tencent-cloud.cn/raw/2c21ea57f1e10c3d9e3f0f1e64f94ace.png" width="70%">
未带鉴权参数的 URL，返回403状态码。

### 验证场景三
使用过期的鉴权 URL 参数，验证返回结果
过期鉴权 URL：`http://www.qcdntest.cn/test.jpg?sign=1656300600-FnyigRo7yny-0-3276ffbdf30dc974ed955d7db761653a`
执行命令：
```
curl http://www.qcdntest.cn/test.jpg?sign=1656300600-FnyigRo7yny-0-3276ffbdf30dc974ed955d7db761653a -i
```
<img src="https://qcloudimg.tencent-cloud.cn/raw/e123d6ed926c85ac8d6575510a0e44d2.png" width="70%">
带过期鉴权 URL，返回403状态码。

