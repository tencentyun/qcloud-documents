## TPNS Android SDK 1.2.5.0

####  配置工程依赖环境（可选）

如果您在使用 SDK 依赖时遇到依赖拉取不到的情况，可以考虑在项目工程根目录 build.gradle 文件 allprojects.repositories 位置添加谷歌官方推荐镜像源 MavenCentral 和腾讯云镜像源，代码示例如下：

```
allprojects {
    repositories {
        google()
        jcenter()

        // 谷歌推荐 MavenCentral 镜像源
        mavenCentral()
        // 腾讯云镜像源
        maven { url 'https://mirrors.tencent.com/nexus/repository/maven-public/' }
    }
}
```

