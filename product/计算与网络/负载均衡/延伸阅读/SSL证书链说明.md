## SSL证书链定义

证书颁发机构(CA)共分为两种类型：根CA和中间CA。为了使SSL证书被信任，该证书必须由设备所连接的可信存储库CA颁发。
	
如果该证书不是由受信任CA，该链接设备(如网络浏览器)将检查，查看该证书是否由受信任的CA颁发，直到没有发现受信任CA为止。
	
SSL证书链就是证书列表中的根证书、中间证书到终端用户证书。

## SSL证书链举例
	
假设用户从Qcloud机构购买证书，域名是example.qcloud.

Qcloud机构不是一个根证书颁发机构。换句话说，它的证书并不是直接嵌入在web浏览器，因此它不能被明确的信赖。

- Qcloud机构使用由中间Qcloud证书颁发机构阿尔法颁发的证书
- 中间Qcloud CA阿尔法使用由中间Qcloud证书颁发机构贝塔颁发的证书
- 中间Qcloud CA贝塔使用由中间Qcloud证书颁发机构伽马颁发的证书
- 中间Qcloud CA伽马使用由The Root of Qcloud颁发的证书
- The Root of Qcloud是一个根CA。该证书是直接嵌入在您的web浏览器中，因此可以被信任。

以上的例子中，SSL证书链是由以下6个证书组成的：
1. 终端证书：颁发给example.qcloud，发行商：Qcloud机构
2. 中间证书1：颁发给example.qcloud，发行商： 中间Qcloud证书颁发机构阿尔法
3. 中间证书2：颁发给中间Qcloud证书颁发机构阿尔法，发行商： 中间Qcloud证书颁发机构贝塔
4. 中间证书3：颁发给中间Qcloud证书颁发机构贝塔，发行商： 中间Qcloud证书颁发机构伽马
5. 中间证书4：颁发给中间Qcloud证书颁发机构伽马，发行商：The Root of Qcloud
6. 根证书： 颁发给The Root of Qcloud，由The Root of Qcloud颁发

其中证书1 称为终端用户证书，证书2-5被称为中间证书。证书6被称为根证书。

当用户安装终端证书example.qcloud时，必须将所有的中间证书捆绑，并与终端证书一起安装。如果SSL证书链无效或被受损， 则用户的证书就不被某些设备信任。






