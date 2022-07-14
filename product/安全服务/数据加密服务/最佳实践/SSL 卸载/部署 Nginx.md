本文主要介绍如何部署 Nginx 服务 以及在 Nginx 上配置证书文件。

1. 将 `nginx-1.16.0_tassl_hsm.tgz` 上传至 CVM2 上并解压，下述以解压至 `/root/ nginx-1.16.0_tassl` 为例。
2. 安装 Nginx，在 `/root/nginx-1.16.0_tassl` 目录下执行：
```
./configure --with-http_ssl_module --with-stream --with-stream_ssl_module --with-openssl=/root/tasshsm_engine/tassl --prefix=/root/nginx
make
make install
```
3. 配置 Nginx 的使用证书，根据使用的算法选择如下任意一种。
 -  使用 RSA 单证书
根据如下代码所示，编辑 `/root/nginx/conf/nginx.conf` 配置文件中的证书部分。
```
user root;
worker_processes  1;
…
…
    # HTTPS server
    server {
        listen       443 ssl;
        server_name  localhost;

        #use tasshsm engine by key index
        ssl_certificate  /root/tasshsm_engine/cert/server/rsa/S_RSA_HSM.crt;
        ssl_certificate_key  engine:tasshsm_rsa:15;
      
        ssl_verify_client off; # for one-way https

        ssl_session_cache    shared:SSL:1m;
        ssl_session_timeout  5m;

        ssl_ciphers  HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers  on;

        location / {
            root   html;
            index  index.html index.htm;
```
**参数说明：**
    - ssl_certificate：配置 RSA 证书文件，带绝对路径。
    - ssl_certificate_key：配置存储 RSA 私钥的索引号。
    - ssl_verify_client off：不验证客户端。
 - 使用国密双证书
根据如下代码所示，编辑 `/root/nginx/conf/nginx.conf` 配置文件中的证书部分。
```
user root;
worker_processes  1;
…
…
    # HTTPS server
    server {
        listen       444 ssl;
        server_name  localhost;

        #use tasshsm engine by key index
        ssl_certificate   /root/tasshsm_engine/cert/server/sm2/SS_SM2_HSM.crt;
        ssl_certificate_key   engine:tasshsm_sm2:15;
        ssl_enc_certificate   /root/tasshsm_engine/cert/server/sm2/SE_SM2_HSM.crt;
        ssl_enc_certificate_key  engine:tasshsm_sm2:16;

        ssl_verify_client off; # for one-way https
        …
        location / {
            root   html;
            index  index.html index.htm;
```
**参数说明：**
    - ssl_certificate：配置签名证书文件，带绝对路径。
    - ssl_certificate_key：配置存储签名私钥的索引号。
    - ssl_enc_certificate：配置加密证书文件，带绝对路径。
    - ssl_enc_certificate_key：配置存储加密私钥的索引号。
    - ssl_verify_client off：不验证客户端。
 - 使用 ECC 单证书
根据如下代码所示，编辑 `/root/nginx/conf/nginx.conf` 配置文件中的证书部分。
```
user root;
worker_processes  1;
…
…
    # HTTPS server
    server {
        listen       445 ssl;
        server_name  localhost;

        #use tasshsm engine by key index
        ssl_certificate  /root/tasshsm_engine/cert/server/ecc/S_ECC_HSM.crt;
        ssl_certificate_key  engine:tasshsm_ecc:15;
      
        ssl_verify_client off; # for one-way https

        ssl_session_cache    shared:SSL:1m;
        ssl_session_timeout  5m;

        ssl_ciphers  HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers  on;

        location / {
            root   html;
            index  index.html index.htm;
```
**参数说明：**
    - ssl_certificate：配置 RSA 证书文件，带绝对路径。
    - ssl_certificate_key：配置存储 RSA 私钥的索引号。
    - ssl_verify_client off：不验证客户端。
4. 输入如下代码，启动 Nginx 代理。
```
cd /root/nginx/sbin
source ./setting
./nginx
```
**参数说明：**
source ./setting：设置 nginx 调用 ssl 的动态库为 tassl 引擎目录。

