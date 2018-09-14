将 QAPM.aar 文件拷贝到项目的 libs 目录下（如果没有此目录请自行创建）,配置 aar 的本地链接路径,类似如下

```
repositories {
    flatDir {
        dir 'libs'
    }
    google()
    jcenter()
}
```
