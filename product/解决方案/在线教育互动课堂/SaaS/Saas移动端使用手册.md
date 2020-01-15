## 互动课堂 App 下载
- Android：应用宝搜索【腾讯云互动课堂】
- iOS：App Store 搜索【腾讯云互动课堂】

### 版本更新说明
当前版本是1.2.0版本。
- 完善课中互动（上下台/授权[操作白屏权限]）
- 支持签到与答题功能
- 优化课中页布局
- 修复一些已知问题

## 互动课堂 App 使用
### 加入课堂
1. **通过在线课堂 App 加入课堂**
页面显示如下图，加入课堂时需要输入【机构编号】、【课堂编号】、【用户名】、【密码】四个要素。登录成功后，直接跳转至课中页面，详见 [课中页面介绍](#.E8.AF.BE.E4.B8.AD.E9.A1.B5.E9.9D.A2.E4.BB.8B.E7.BB.8D)。
![](https://main.qcloudimg.com/raw/be232e94451967f1dd1819016144b063.png)
<table>
<tr>
<th>要素</th>
<th>说明</th>
</tr>
<tr>
<td>机构编号</td>
<td>由管理员告知。腾讯云互动课堂分配的公司编号。</td>
</tr>
<tr>
<td>课堂编号</td>
<td>由管理员告知。约好的课程编号。</td>
</tr>
<tr> 
<td>用户名</td>
<td> 由管理员告知。登录 App 的账号，仅管理员可修改。</td>
</tr>
<tr>
<td>密码</td>
<td>由管理员告知。登录 App 的密码，仅管理员可修改。</td>
</tr>
</table>
2. **通过管理员分享的链接加入课堂**
腾讯云互动课堂支持分享链接的方式加入课堂，通过老师或者管理员分享链接，学生在浏览器中打开。
![](https://main.qcloudimg.com/raw/78f3826ca26250a7b8d62184e795ecbe.jpg)
单击【打开App】后，会跳转至 App 的登录页，App 会自动填充机构编号和课堂编号信息。
 - 手 Q 客户端聊天窗口打开链接：在 iOS 平台由于系统限制，需要根据提示在浏览器中打开后方可跳转。Android 平台上根据提示操作即可。
 - 微信客户端聊天窗口上打开链接：iOS 和 Android 平台，均需要在浏览器中打开后方可跳转。单击右上角菜单，选择【在浏览器中打开】跳转到浏览器，后续操作与直接在浏览器中打开相同。
![](https://main.qcloudimg.com/raw/42fb55127a0889e6ae1dd3c66e615ccc.jpg)

#### 游客登录
![](https://main.qcloudimg.com/raw/930ea674f1e71949a7d0175023b41149.png)
<table>
<tr>
<th>要素</th>
<th>说明</th>
</tr>
<tr>
<td>课堂编号</td>
<td>由管理员告知。腾讯云互动课堂分配的课堂编号。</td>
</tr>
<tr>
<td>昵称</td>
<td>由用户自行指定</td>
</tr>
</table>

## 课中页面介绍
成功加入课堂后，就可以使用课堂中的各种功能。移动端暂时不支持老师端功能，老师端功能推荐使用桌面端完成。

进入课堂后，界面展示如下：
![](https://main.qcloudimg.com/raw/7b14e0d92502fb81f6ef07727824cd22.png)
学生端默认限制了白板操作，只能查看；但可通过举手互动，向老师请求获得白板操作授权，获得授权后，会展示白板工具菜单，如下：
![](https://main.qcloudimg.com/raw/e2678507e2d63ae23bd6ca041f9d82a5.png)
课中页面目前有两种布局配置，分别是**竖屏**布局和**横屏**布局，**竖屏**布局效果如上所示，**横屏**布局效果展示如下：
![](https://main.qcloudimg.com/raw/f5cc819ef33451bf8c2aa141bcff4a54.png)
签到效果：
![](https://main.qcloudimg.com/raw/7d8f0c7baa7551a585a333981ab7f26d.png)
答题效果：
![](https://main.qcloudimg.com/raw/855a592cad5c9359b7175ac6310fa840.png)
布局的设置在控制台或者云 API 新建课堂时设定，详情可参考 [控制台使用手册](https://cloud.tencent.com/document/product/680/37505) 或 [云 API-课堂模块](https://cloud.tencent.com/document/product/680/37540#.E8.AF.BE.E5.A0.82.E6.A8.A1.E5.9D.97) 部分。
