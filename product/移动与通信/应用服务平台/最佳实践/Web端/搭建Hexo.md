
## 步骤1：安装 CloudBase CLI 以及本地部署 Hexo
1. 在本地安装 Node.js：如果未安装则前往 [NodeJS官网](https://nodejs.org) 下载安装。确保 Node.js 安装成功。
2. 打开命令提示符，执行如下命令：
```
npm i -g @cloudbase/cli hexo-cli
```
3. 执行完毕后，在本地新建一个文件夹。在新建的文件夹中运行命令提示符，执行如下命令：
```
hexo init
```
4. 在初始化中，您可以看到如下图的输出：
![](https://main.qcloudimg.com/raw/808ac3493252399ba1b2354879fc668a.png)
5. 初始化完成后，执行如下命令，启动预览：
```
hexo s
```
![](https://main.qcloudimg.com/raw/2cfab06f6c487057cbb8934cea6a5fb0.png)
- 预览后，在浏览器中打开 [localhost:4000](http://localhost:4000)，即可看到部署的 Hexo 博客。
![](https://main.qcloudimg.com/raw/5b91e6303e40aea5c1d5f0cfc521dc4a.png)



## 步骤2：创建云开发环境
1. 打开浏览器，进入腾讯云 [云开发控制台](https://console.cloud.tencent.com/tcb)，单击【立即创建】，新建一个环境来进行部署。
![](https://main.qcloudimg.com/raw/373ce011bfad392b5c2fedd8008bb6f5.png)
如果您之前创建过环境，可以继续使用已创建的**按量计费**环境，或者再次新建环境。
![](https://main.qcloudimg.com/raw/a342d1d01c934e2e4f6ee0680afad17d.png)
2. 在新建环境窗口中，按自己喜好要求填写环境名称，选择按量计费，开通环境。
![](https://main.qcloudimg.com/raw/529c3e20d8eb4edc7ab4c6fa504a52c7.png)
3. 在开通环境以后， 记住您的环境 ID，这个 ID 后续步骤会用到。
4. 单击环境，进入到环境的管理页面。单击左侧菜单栏中的【网站托管】，在页面中单击【开始使用】，开通静态托管服务。
![](https://main.qcloudimg.com/raw/3de236cbe3dfbe664803f9b6c996ea1b.png)
当您能看到这样的界面时，就说明已经开通好了。
![](https://main.qcloudimg.com/raw/794944962439c81cd6e671a8356ebfc6.png)



## 步骤3：初始化云开发 CLI
1. 打开命令提示符，输入如下代码：
```
cloudbase login
```
2. 将拉起浏览器授权，登录刚创建云开发环境的账号
![](https://main.qcloudimg.com/raw/026ba161e5820db9efa889c3b0d0c367.png)



## 步骤4：构建 Hexo 部署文件
1. 打开命令提示符，定位到步骤一新建的Hexo目录中，执行如下代码：
```
Hexo g
```
2. 将会生成部署文件，Hexo 会默认将文件生成在 Public 目录下：
![](https://main.qcloudimg.com/raw/b6f03410c72598c37632f1c35b1b9811.png)
3. 执行如下命令，将 Hexo 部署到云开发静态托管中（需要将 EnvID 替换为前面您记下的环境ID）。
```
cloudbase hosting:deploy public -e [EnvID]
```
![](https://main.qcloudimg.com/raw/a3835aacdbde4049d2cced769af62e17.png)


## 步骤5：浏览部署的 Hexo
1. 打开浏览器，进入 [腾讯云·云开发控制台](https://console.cloud.tencent.com/tcb)，单击部署的云开发环境，进入后单击左侧栏的【网站托管】-【设置】，在域名信息中找到默认域名。
![](https://main.qcloudimg.com/raw/ebd5e516a098daf471507f7e149996ea.png)
2. 在浏览器中打开此链接，则看到线上部署好的 Hexo 博客。
![](https://main.qcloudimg.com/raw/590b7ee62174aa74f0119ac4775c6362.png)
