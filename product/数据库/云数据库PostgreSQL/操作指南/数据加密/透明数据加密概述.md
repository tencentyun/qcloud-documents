## 概述
透明数据加密（Transparent Data Encryption，以下简称 TDE），提供文件级别的加密，可以做到对数据库上层的应用透明，用户不需要修改业务代码，存储在硬盘上的数据是加密的，对磁盘数据读取和写入时透明地进行加解密。

透明数据加密常用于解决一些安全合规问题，如 PCI DSS、等级安全保护等要求静态数据需要被保护的场景。

## 加密是什么
在密码学中，加密（Encryption）是将明文信息改变为难以读取的密文内容，使之不可读的过程。

现代密码学是基于数论和概率论的一门学科，加密的终极目标是香农定义的 Perfect security（也称 **Information-theoretic security**）：

Let E = (E, D) be a Shannon cipher defined over (K,M, C). Consider a probabilistic experiment in which the random variable k is uniformly distributed over K. If for all m0, m1 ∈ M, and all c ∈ C, we have

Pr[E(k, m0) = c] = Pr[E(k, m1) = c],

then we say that E is a perfectly secure Shannon cipher.

简单来说，对于密文 c，是可由任何一个明文 m 加密而来的，从密文中找不到它和明文之间的关联性。

## 加密算法的分类
加密算法可以分为两类：对称加密和非对称加密。
- 对称加密：加密和解密使用同样的密钥，对称加密的速度比非对称加密快很多，在很多场合都需要对称加密。
- 非对称加密：又称公开密钥加密，是加密和解密使用不同密钥的算法，主要用户信息传输。

对称加密算法常见的有 AES，3DES 等。非对称加密算法最广为使用的是 RSA 算法，其可靠性源自于对极大整数做因数分解的难度。

## TDE 威胁模型（Threat model）
TDE 主要用于保护静态数据 data at rest，防止磁盘被盗窃导致数据泄漏。

## 云数据库 PostgreSQL 加密实现方案
腾讯云数据库 PostgreSQL 通过向用户申请使用 KMS（Key Management Service）服务中保存的主密钥，生成 DEK（Data Encryption Key）密文与 DEK 明文对云产品加密所使用的密钥进行数据加密和解密。
![img](https://main.qcloudimg.com/raw/beb03cab3bc4157e94661a78904d34fd.png)
此类加密方案被称为信封加密，即用另一个密钥对密钥进行加密的过程称为“信封加密（Envelope Encryption）”。信封加密是一种应对海量数据的高性能加解密方案。其可通过生成 DEK 来对本地数据进行加解密，保证了业务加密性能的要求，同时也由 KMS 确保了数据密钥的随机性和安全性。

所有的加密解密操作均由数据库在内存中进行，每一次数据库重启以及存在关闭内存的操作时，均会重新从 KMS 获取密钥材料。本地存储中不保存任何可用于解密的密钥材料。
![](https://qcloudimg.tencent-cloud.cn/raw/9b2db6c35942d31a692f57e87937cea5.png)
