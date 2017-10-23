
### 开发者注册流程
#### 1.账户登录
在 [QQ互联开放平台首页](https://connect.qq.com/) 单击右上角【登录】按钮，使用 QQ 帐号登录，如下图所示：
![](https://mc.qcloudimg.com/static/img/fc343806a2c338fdb2945a9ce203d56a/image.png)
> **注意：**
> 开发者 QQ 号码注册完成后将不能变更，建议使用 **公司公共 QQ 号码** 而不是员工私人号码注册，避免员工离职等不必要的麻烦。

#### 2.完善资料
登录成功后会跳转到开发者注册页面，在注册页面按要求提交公司或个人的基本资料。下图所示的是公司注册页面：
![](https://mc.qcloudimg.com/static/img/587bda12e7a9a1585dc3370c35e3dea9/image.png)
#### 3.等待审核
按要求提交资料后，审核通过即可成为开发者。
>**注意：**
>开发者资料审核一般会在三个工作日内完成，如有疑问，请咨询**企业 QQ：800013811**。

###  开发者创建应用、调用 OpenAPI 修改用户信息
#### 创建应用
1.开发者注册完成后，在 [QQ互联开放平台首页](https://connect.qq.com/) 依次单击【应用管理】>【移动应用】>【创建应用】按钮，选择创建移动应用，如下图所示：
![](https://mc.qcloudimg.com/static/img/bb1cf142ae37bc4a97d8ab617a575378/image.png)
2.进入资料填写页面，填写基本信息。
![](https://mc.qcloudimg.com/static/img/1271c932e2733c1e80fbf29fe3963bec/image.png)
3.填写应用信息。
>**注意：**
>游戏可以直接在此勾选开通社交能力（包括加好友能力、一键加绑群能力、游戏内置兴趣部落等）。

![](https://mc.qcloudimg.com/static/img/a6d938c771e1a8f599b6ceb710357c20/image.png)
4.提交后，即表示应用创建成功。
![](https://mc.qcloudimg.com/static/img/00ba5b02abc6c12e20bc4997eedac4fa/image.png)
#### 获取参数
创建完成后单击【应用管理】按钮，在应用列表中单击【查看】按钮，在【基本信息】中可以获取游戏应用的 ***APP ID*** 和 ***APP Key*** 参数。
>**注意：**
>***APP ID*** 和 ***APP Key***是游戏在 QQ 域下的唯一标识，以保证后续可以正确得对网站与用户进行验证与授权操作。

![](https://mc.qcloudimg.com/static/img/e1fa0c043126d5ed61a14871f2a79b43/image.png)
#### 修改用户信息
用户登录游戏后，游戏应用即可调用 OpenAPI 来获取用户的信息。我们提供了各种游戏应用接入给开发者，游戏应用可以调用这些 API 来实现需要的功能，使登录的 QQ 用户在移动应用上即可访问和修改受保护的个人信息。

具体的 API 可以通过单击【应用接口】查看，未开通的接口可以申请接口权限。如下图所示：
![](https://mc.qcloudimg.com/static/img/1ce7ad57f26616985865be87d6ce4b64/image.png)

#### 数据统计
在【数据统计】一栏中可以查询任意时间段的用户登录和分享数据，如下图所示：
![](https://mc.qcloudimg.com/static/img/232e6c724585a30a9a2af204f15c38a1/image.png)


