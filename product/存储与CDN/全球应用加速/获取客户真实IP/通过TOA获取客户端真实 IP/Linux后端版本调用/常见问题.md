### 签名报错，例如 module verification failed: signature and/or required key missing - tainting kernel

- 解决：linux 内核会有对模块有签名校验，取决于编译内核时候是否开启此特性 
- 解决方法一：编译内核时，去掉签名支持 CONFIG_MODULE_SIG=n
- 解决方法二：有证书的情况下，可进行签名，举个例子：
  /usr/src/linux-4.9.61/scripts/sign-file sha512/usr/src/linux-4.9.61/certs/signing_key.pem /usr/src/linux-4.9.61/certs/signing_key.x509 toa.ko

  

### 编译时报错没有 /lib/modules 目录

-	解决：常见以下三种情况
-	没安装有内核包
-	路径被修改过，需要自行纠正下
-	安装的内核没有 build 目录，需手动软连接到对应版本内核的 header，例如
cd /lib/modules/4.9.0-13-amd64 && ln -s /usr/src/linux-headers-4.9.0-13-amd64 build
