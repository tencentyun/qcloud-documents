将QAPM.aar文件拷贝到项目的libs目录下（如果无该目录请自行创建该目录）,配置 aar 的本地链接路径,类似如下
```
repositories {
    flatDir {
        dir 'libs'
    }
    google()
    jcenter()
}
```