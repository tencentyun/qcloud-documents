开发注意事项

##1.开发建议

1)url的末尾一定要加上“/”， 如：“/app_code/path/current_url/”不要写成“/app_code/path/current_url”

##2.数据库操作

蓝鲸中APP使用south来管理数据库。south针对django自带的syncdb同步models和数据库的缺陷开发的数据迁移工具，South能够检测对models的更改并同步到数据库。

South的使用方法如下:

1)执行命令```manage.py syncdb```, 这一步的作用是在数据库中创建south_migrationhistory的表，用来存放数据库的变更历史。 

2)执行```manage.py startapp yourappname```创建你的应用，并把你的应用添加到config/settings_custom.py文件"INSTALLED_APPS_CUSTOM"中。 

3)在django的models.py中建立数据库模型后，执行```schemamigration yourappname --init```，这一步执行完成后可以在你的app下看到一个migrations的文件夹，里面有__init__.py和0001_initial.py两个文件。

4)执行成功后再执行```migrate yourappname```，这时候数据库中已经建立了你定义的表，并可以看到south_migrationhistory表中增加了一条记录。

5)在工程中新增app，只需再次执行3—5的步骤即可。 

6)更改models.py的内容，只需执行```schemamigration yourappname --auto```和```migrate yourappname```即可。 

注意： 必须按上面的步骤顺序执行，```manage.py syncdb```这个命令只在第2步使用一次。

请注意在第一次syncdb时不要加入自己的app，先syncdb初始化south的数据，然后再加入自己的app进行south操作!
