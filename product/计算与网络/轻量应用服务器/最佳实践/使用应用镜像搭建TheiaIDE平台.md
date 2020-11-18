## 操作场景
Theia IDE 是一套构建基于 Web 的云端 IDE 的开源框架，是一个可扩展的平台，具备良好的多语言支持能力，并支持 VS Code 扩展。腾讯云轻量应用服务器提供 Theia IDE 镜像，已安装 Go、Python、Node.js、Clang 及 OpenJDK 开发环境，您可通过它便捷的实现跨平台，并可快速进行项目及业务开发。


## 操作步骤
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 单击【新建】，进入轻量应用服务器购买页面。如下图所示：
![](https://main.qcloudimg.com/raw/7679376b362b5357a9adff972e63adce.png)
	- **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，则地域选择 “广州”。
	- **镜像**：选择 “Theia IDE 1.5.0” 应用镜像。
	- **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、带宽或峰值带宽、每月流量），选择一种实例套餐。
	- **实例名称**：自定义实例名称，若不填则默认使用所选镜像名称。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
	- **购买时长**：默认1个月。
	- **购买数量**：默认1台。
3. 单击【立即购买】，并根据页面提示提交订单完成支付，返回轻量应用服务器控制台。
4. 待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
您可以在此页面查看 Theia IDE 应用的各项配置信息。
5. 选择【应用管理】页签，进入应用管理详情页。
6. <span id="Step6"></span>在“应用内软件信息”栏中，单击<img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px"/>，复制获取 Theia 1.5.0 的管理员帐户密码的命令。
7. 在“应用内软件信息”栏中，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/86c5b9650acf9d6b0f4bc0ad3e16156d.png)
8. <span id="Step8"></span>在弹出的登录窗口中，粘贴 [步骤6](#Step6) 复制的命令并按 **Enter**。
即可获取 Theia IDE 管理员账号（admin）和对应的密码，请妥善保管并记录。
9. 关闭登录窗口，并返回该实例的应用管理详情页。
10. 在“应用内软件信息”栏中，单击 Theia 1.5.0 的【访问地址】。
>!执行操作时建议使用 Chrome 或 Firefox 浏览器，其他浏览器（例如 Safari）可能存在兼容性问题。
>
11. 在弹出窗口中输入 [步骤8](#Step8) 获取的管理员帐户及密码，并单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/26af0c90cf5a4cb7a87942ce7c6bdd72.png)
验证成功后即可进入 Theia IDE 工作界面，按需进行使用。

## 后续操作
### 选择工作空间
1. 选择 Thiea IDE 起始界面中的【Open WordSpace】。
2. 在弹出的 “Open Workspace” 窗口的下拉列表中选择`/`，打开目录。在 Theia IDE 中目录即为工作空间，本文以选择 `/data` 为例。如下图所示：
![](https://main.qcloudimg.com/raw/5451fbf0a2d310a2b3b77be9bab1a1a4.png)
3. 单击【Open】，进入 `/data` 工作空间。


### 使用示例
>?Theia IDE 目前支持 Python、Java、Go、C/C++ 及 Node.js 语言。该步骤以命令行及界面两种方式分别运行 Python、Go 及 C++ 语言程序示例，您可按需选择对应语言进行操作。
>

#### Python
1. 在工作空间中，选择窗口上方的【File】>【New Folder】。
2. 在弹出窗口中创建名为 `Python` 的文件夹，并在其下创建简单示例文件 `main.py`。如下图所示：
![](https://main.qcloudimg.com/raw/f8b8f3f14629f090571bdc84f67bd577.png)
3. 您可使用以下两种方式运行该程序：
<ul>
<li><b>命令行方式：</b></li>
<ol type="i">
<li class="roman">选择窗口上方的【Terminal】>【New Terminal】，打开终端。</li>
<li class="roman">在终端中依次执行以下命令，运行程序。
<pre>cd Python</pre>
<pre>python3.8 main.py</pre>
执行结果如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/77a29e75d9473027a7b6d4b411c49a68.png" />
</li>
</ol>
</ul>
<ul>
<li><b>界面方式：</b></li>
选择窗口右上方的<img src="https://main.qcloudimg.com/raw/708198cbeab5c12c186e832ec484c60e.png" style="margin:-3px 0px"/>，运行程序。
执行结果如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/da0fb5c90d70695d8e1636cf6863cc20.png" />
</li>
</ol>
</ul>

#### Go
1. 在工作空间中，选择窗口上方的【File】>【New Folder】。
2. 在弹出窗口中创建名为 `go` 的文件夹，并在其下创建简单示例文件 `main.go`。如下图所示：
![](https://main.qcloudimg.com/raw/caedca384df2a2e8e42cee06af6600d9.png)
3. 您可使用以下两种方式运行该程序：
<ul>
<li><b>命令行方式：</b></li>
<ol type="i">
<li class="roman">选择窗口上方的【Terminal】>【New Terminal】，打开终端。</li>
<li class="roman">在终端中依次执行以下命令，运行程序。
<pre>cd go</pre>
<pre>go run main.go</pre>
执行结果如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/6550d3deeb6b9cd9776f1985d1bac710.png" />
</li>
</ol>
</ul>
<ul>
<li><b>界面方式：</b></li>
<ol type="i">
<li class="roman">选择左侧的<img src="https://main.qcloudimg.com/raw/710f37253b774a7e3aed3e94b5bb1777.png" style="margin:-6px 0px">，打开 DEBUG 栏。</li>
<li class="roman">在 DEBUG 中，选择下拉列表中的【Add Configuration】，生成配置文件。如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/6e6e83d3bc7476029b662997be9c1525.png" style="margin:-3px 0px">
</li>
<li class="roman">打开 <code>main.go</code> 文件，并选择 DEBUG 栏中的<img src="https://main.qcloudimg.com/raw/8d1ae32ecac7a0865835e8f3cfb7916c.png" style="margin:-3px 0px"/>，运行程序。执行结果如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/dab083f4d4496ef058a65a98782c33a9.png" style="margin:-3px 0px">
</li>
</ol>
</ul>

#### C++
1. 在工作空间中，选择窗口上方的【File】>【New Folder】。
2. 在弹出窗口中创建名为 `c++` 的文件夹，并在其下创建简单示例文件 `main.cpp`。如下图所示：
![](https://main.qcloudimg.com/raw/3eadfa7a7924581d0b3c87dd3cac35e2.png)
3. 您可使用以下两种方式运行该程序：
<ul>
<li><b>命令行方式：</b></li>
<ol type="i">
<li class="roman">选择窗口上方的【Terminal】>【New Terminal】，打开终端。</li>
<li class="roman">在终端中依次执行以下命令，运行程序。
<pre>cd c++</pre>
<pre>clang++ main.c</pre>
<pre>./a.out</pre>
执行结果如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/7f905e65bfa92c5182ad551993014f42.png" />
</li>
</ol>
</ul>
<ul>
<li><b>界面方式：</b></li>
<ol type="i">
<li class="roman">选择左侧的<img src="https://main.qcloudimg.com/raw/710f37253b774a7e3aed3e94b5bb1777.png" style="margin:-6px 0px">，打开 DEBUG 栏。</li>
<li class="roman">在 DEBUG 中，选择下拉列表中的【Add Configuration】，生成配置文件。如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/6e6e83d3bc7476029b662997be9c1525.png" style="margin:-3px 0px">
</li>
<li class="roman">在配置文件展开的下拉列表中，选择【{ } GDB CDT Local debugging】。</li>
<li class="roman">将配置文件中的 <code>/${command:askProgramPath}</code> 替换为 <code>/c++/a.out</code>，并保存修改。</li>
<li class="roman">选择 DEBUG 栏中的<img src="https://main.qcloudimg.com/raw/7090e9c3a03493c183e8a259896dcde9.png" style="margin:-3px 0px">，打开 Debug Console。</li>
<li class="roman">选择 DEBUG 栏中的<img src="https://main.qcloudimg.com/raw/8d1ae32ecac7a0865835e8f3cfb7916c.png" style="margin:-3px 0px"/>，运行程序。执行结果如下图所示：
<br>
<img src="https://main.qcloudimg.com/raw/fc23bdc950648b3e4302968ce9d4e240.png">
</li>
</ol>
</ul>


<style>
	.roman{
		list-style-type:lower-roman
	}
</style>
