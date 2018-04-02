配置 maven 的链接路径,类似如下
```
repositories {
    maven {
        url "http://maven.oa.com/nexus/content/repositories/thirdparty-snapshots"
    }
    google()
    jcenter()
}
```