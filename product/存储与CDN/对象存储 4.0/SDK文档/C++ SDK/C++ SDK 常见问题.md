### 编译可执行程序的时候提示错误： PocoCrypto.so.64: undefined reference ，该如何处理？


```shell
   PocoCrypto.so.64: undefined reference to `PEM_write_bio_PrivateKey@libcrypto.so.10'
   libPocoNetSSL.so.64: undefined reference to `X509_check_host@libcrypto.so.10'
   ibPocoCrypto.so.64: undefined reference to `ECDSA_sign@OPENSSL_1.0.1_EC'
   libPocoCrypto.so.64: undefined reference to `CRYPTO_set_id_callback@libcrypto.so.10'
   ibPocoCrypto.so.64: undefined reference to `EVP_PKEY_id@libcrypto.so.10'
   libPocoNetSSL.so.64: undefined reference to `SSL_get1_session@libssl.so.10'
   libPocoNetSSL.so.64: undefined reference to `SSL_get_shutdown@libssl.so.10'
   libPocoCrypto.so.64: undefined reference to `EVP_PKEY_set1_RSA@libcrypto.so.10'
   libPocoCrypto.so.64: undefined reference to `SSL_load_error_strings@libssl.so.10'
```
这种情况一般是工程里自带的 poco 库的编译依赖的 SSL 版本与客户机器上的版本不一致导致的，需要用户重新编译 poco 库，并替换掉 third_party 里的poco库。

>! 此处建议执行以下命令从github下载源码。如果从poco官网下载，请下载COMPLETE版本。

```shell
wget https://github.com/pocoproject/poco/archive/refs/tags/poco-1.9.4-release.zip
cd poco-poco-1.9.4-release/
./configure --omit=Data/ODBC,Data/MySQL
mkdir my_build
cd my_build
cmake .. 
make -j5
```


### 编译 poco 库的时候无法编译出 PocoNetSSL 库，该如何处理？


一般是因为机器没装 openssl-devel 库。使用如下命令安装。
```shell
yum install -y openssl-devel
```



### 编译可执行程序的时候提示错误： undefined reference to qcloud_cos ，该如何处理？
```shell
undefined reference to `qcloud_cos::CosConfig::CosConfig(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)
```
这种情况一般是因为工程自带的 libcossdk.a 编译使用的 gcc 版本与客户机器上的 gcc 版本不一致导致的，需要客户重新编译 poco 库和 libcossdk。


### C++ SDK 报错请求过期报错请求过期：Request has expired ，该如何处理？


由于签名过期导致，重新生成签名即可解决；若重新生成签名仍报相同的错误，可以再检查下机器的本地时间是否已设置为标准的北京时间。


