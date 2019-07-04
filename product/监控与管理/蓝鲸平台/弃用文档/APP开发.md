在开发者中心（http://o.qcloud.com/developer-center） 创建应用后，从SVN中checkout代码到本地就可以开始本地开发；本地调试成功后就可以将应用部署到蓝鲸平台中。

蓝鲸平台提供了一套基于Django框架的APP开发样例，样例中提供了QQ统一登录、腾讯云API接口、 任务调度等功能，用户在APP开发样例上进行二次开发，可以大幅度提高开发效率。创建应用时自动将最新版的开发样例代码初始化到APP的SVN中。

APP开发样例 访问地址：http://o.qcloud.com/console?app=app_template

## 1 本地开发准备

开发前准备包括：安装python、Mysql等开发环境的配置； APP开发样例下载；配置host。

**1.1 开发环境配置**

（1）安装python
（2）安装Mysql
（3）安装 setuptools-0.6c11.win32-py2.7.exe和MySQL-python-1.2.3.win32-py2.7.exe
（4）安装python库，包括django1.3、south、httplib2等
（5）安装本地开发工具，windows环境下推荐使用Eclipse进行代码开发、使用TortoiseSVN管理SVN

**1.2 从svn中检出（checkout）代码**

（1）将APP从SVN仓库中检出到本地目录中
（2）配置修改：
1）config/settings_develop.py 文件中DATABASES 项中：填写本地数据库的相关信息
2）本地使用Eclipse开发时，工程的启动端口默认为8000，如使用其他端口在config/settings_develop.py 文件中S_URL 项中：修改工程的启动端口

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/appkaifa-01.png)

**1.3 host配置**

在hosts中配置：127.0.0.1 app.o.qcloud.com

1）windows下host配置

C:\Windows\System32\drivers\etc\hosts文件 中 添加：

127.0.0.1 app.o.qcloud.com

2）linux下host配置

/etc/hosts 文件中添加：127.0.0.1 app.o.qcloud.com

## 2 开发注意事项

**2.1 开发建议**

(1）url的末尾一定要加上“/”， 如：“/app_code/path/current_url/”不要写成“/app_code/path/current_url”

**2.2 数据库操作**

蓝鲸中APP使用south来管理数据库。south针对django自带的syncdb同步models和数据库的缺陷开发的数据迁移工具，South能够检测对models的更改并同步到数据库。

South的使用方法如下:

（1）执行命令 manage.py syncdb, 这一步的作用是在数据库中创建south_migrationhistory的表，用来存放数据库的变更历史。 
（2）执行manage.py startapp yourappname 创建你的应用，并把你的应用添加到config/settings_custom.py文件"INSTALLED_APPS_CUSTOM"中。 
（3）在django的models.py中建立数据库模型后，执行 schemamigration yourappname --init，这一步执行完成后可以在你的app下看到一个migrations的文件夹，里面有__init__.py和0001_initial.py两个文件 
（4）执行成功后再执行migrate yourappname ，这时候数据库中已经建立了你定义的表，并可以看到south_migrationhistory表中增加了一条记录。
（5）在工程中新增app，只需再次执行3—5的步骤即可。 
（6）更改models.py的内容，只需执行schemamigration yourappname --auto 和migrate yourappname即可。 

>注意： 必须按上面的步骤顺序执行，manage.py syncdb这个命令只在第2步使用一次。

请注意在第一次syncdb时不要加入自己的app，先syncdb初始化south的数据，然后再加入自己的app进行south操作!

## 3 常见问题

**3.1 编码错误**

错误描述：'utf8' codec can't decode byte 0xb6 in position 6: invalid start byte 

错误原因：

（1）本地开发，将app工程目录放在包含中文名称的目录下。
解决方案：确保APP的路径不包含中文名称
（2）本地开发没有设置编码。

解决方案：

在python的安装路径中下的/Lib/site-packages下面创建文件sitecustomize.py，内容如下：

```
import sys 
sys.setdefaultencoding('utf-8')	# set default encoding as 'utf-8' 
```

如果没有加入该文件，则在有编码问题的.py代码中，加入以下代码：

```
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 
```

**3.2 工程文件目录冲突**

错误描述：工程运行启动时，提示No module named settings 错误

错误原因： 工程名和内建app名重复，如下图所示

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/appkaifa-02.png)

**解决方案**：修改工程名或内建app名称

**3.3 提测、上线时fixture数据冲突**

错误描述：用户提测、上线时报错，错误原因提示：syncdb_and_migrate Problem installing fixture

错误原因：初始化数据冲突

**解决方案：**
（1）请检查fixtures 文件内pk和username值是否和数据库中auth_user表里对应的用户名、id一致，请查询并修改。
（2）config/settings_custom.py 文件中的IS_FIXTURES 设置为False，关闭初始化数据开关。

**3.4 提测、上线时数据库错误**

错误描述：类似 _mysql_exceptions.OperationalError: (1045, "Access denied for user @ (using password: NO)") 错误

**解决方案：**请检查App的数据库配置（库名、用户名、密码）是否正确，如果使用非蓝鲸提供的DB，请给蓝鲸机器IP进行授权。

**3.5 SVN 相关问题**

遇到奇怪的SVN错误，可以：

（1）重新在本地新建目录，检出干净的svn
（2）或者先保存代码，然后删除该版本，重新导入