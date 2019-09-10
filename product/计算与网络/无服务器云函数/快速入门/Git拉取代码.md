针对单函数，提供从公网 Git 仓库拉取代码部署的能力。
在函数代码页面，提交方法选择“通过git上传代码包”。
填写 Git 相关认证信息，和仓库信息后，点击确定，云函数后台即可从 git 仓库拉取代码进行部署。

## 前提条件
 - 已开通云函数Git拉取代码功能。
云Git拉取代码目前为内测发布功能，可通过 [内测申请](https://cloud.tencent.com/apply/p/kd8np1at8r) 获取此功能。
 - 暂时只支持北京和广州地域。


![](https://main.qcloudimg.com/raw/e8823044d909585ecc662c3eee6f98a8.png)

### 支持的公网Git仓库列表：
    Github，Coding，码云

### Git认证信息：
    用户名：Git账户的用户名

    Token（或密码）：Git账户的私人令牌或者密码

## 私人令牌申请页面：

### GitHub
    Github：https://github.com/settings/tokens 需要赋予repo权限

![](https://main.qcloudimg.com/raw/8a41e0e1a9d39c951e014a50f9956ce3.png)

### Coding
    Coding：参照此文档https://open.coding.net/personal-access-token/#%E5%88%9B%E5%BB%BA%E4%B8%AA%E4%BA%BA%E8%AE%BF%E9%97%AE%E4%BB%A4%E7%89%8C

#### 用户名
![](https://main.qcloudimg.com/raw/bef9e8ca86af22d1384fe1b2ca0e3300.png)

#### Token
![](https://main.qcloudimg.com/raw/58698cb5e8ba44d806b4687a1d1fdc37.png)

### 码云

    码云：https://gitee.com/profile/personal_access_tokens 需要赋予projects权限

![](https://main.qcloudimg.com/raw/b8d35925768b86225fcccc10fcf070bb.png)