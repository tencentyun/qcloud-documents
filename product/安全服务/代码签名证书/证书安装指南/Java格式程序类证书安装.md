### 1. 安装配置

Java格式类程序文件需要使用jarsigner进行数字签名。签名工具jarsigner是jdk中bin目录下的自带工具，如图
![](https://mc.qcloudimg.com/static/img/4d030150665b129714a3c71b1f8c762b/image.png)

### 2. 证书格式转换

代码签名证书会以pem格式颁发，而利用jarsigner签名需要使用jks格式转换，可以利用在线证书转换格式工具（如亚洲诚信在线格式转换工具：https://www.trustasia.com/tools-cert-converter ） 转换成需要的jks文件格式

>注意：由于用户没有上传pem私钥，因此在亚洲诚信证书格式转换中，“PEM私钥密码”不用填写。

### 3. 输入指令

将签名文件和待签名的jar程序文件放入jdk中的bin目录下，如放在：  
C:\Program Files\Java\jdk\bin下

执行命令

Jarsigner  -keystore <jks文件>  -storepass <刚才生成时候的密码> <要签署的jar文件>
Mykey（别名） -tsa <时间戳>（时间戳为可选项，需有网络的条件下才可以使用）

安装示例：
在Windows中cmd命令下，采用cd命令进入C:\Program Files\Java\jdk\bin，输入  

`Jarsigner  –keystore  1.jks –storepass 123123  1.jar  mykey  –tsa  http://sha256timestamp.ws.symantec.com/sha256/ `

### 4. 获取别名

利用在线证书转换工具转换证书格式时，需要提供文件别名，因此可通过keytool工具下的命名获取别名。  
利用windows下的cmd运行获取别名命令：  

keytool -list -keystore  <jks文件> -storepass  <jks密码>



