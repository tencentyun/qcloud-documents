## 说明
DockerHub 提供了大量的镜像可用，详情可查看 [DockerHub 官网](https://hub.docker.com/)。

Docker 容器的设计宗旨是让用户在相对独立的环境中运行独立的程序。

Docker 容器程序在镜像内程序运行结束后会自动退出。如果要令构建的镜像在服务中持续运行，需要在创建服务页面指定自身持续执行的程序，如：业务主程序，main 函数入口等。

由于企业环境的多样性，并非所有应用都能在  DockerHub 找到对应的镜像来使用。 您可以通过以下教程了解到如何将应用打包成Docker镜像。

Docker 生成镜像目前有两种方式：

- 通过 Dockerfile 自动构建镜像；
- 通过容器操作，并执行 Commit 打包生成镜像。


## Dockerfile 自动编译生成（推荐使用）
以 Dockerhub 官方提供的 WordPress 为例，[转到 github 查看详情 >>](https://github.com/docker-library/wordpress/blob/7d40c4237f01892bb6dbc67d1a82f5b15f807ca1/php5.6/apache/Dockerfile)

其 Dockfile 源码如下：
```shell
FROM php:5.6-apache

# install the PHP extensions we need
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev && rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd mysqli opcache

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=2'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN a2enmod rewrite expires

VOLUME /var/www/html

ENV WORDPRESS_VERSION 4.6.1
ENV WORDPRESS_SHA1 027e065d30a64720624a7404a1820e6c6fff1202

RUN set -x \
	&& curl -o wordpress.tar.gz -fSL "https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz" \
	&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress
	&& tar -xzf wordpress.tar.gz -C /usr/src/ \
	&& rm wordpress.tar.gz \
	&& chown -R www-data:www-data /usr/src/wordpress

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat

# ENTRYPOINT resets CMD
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["apache2-foreground"]
```

通过上述 Dockerfile 文件可以了解到，内置执行了许多的 Linux 命令来安装和部署软件。
在终端创建一个文件夹来保存该 Dockerfile 文件，并通过 docker build 命令来构建镜像。

```shell
[root@VM_88_88_centos worldpress]# docker build ./
Sending build context to Docker daemon 3.072 kB
Step 1 : FROM php:5.6-apache
Trying to pull repository docker.io/library/php ... 
5.6-apache: Pulling from docker.io/library/php
386a066cd84a: Pull complete 
269e95c6053a: Pull complete 
......
```
通过 docker images 命令即可查看到构建完成的镜像。
```shell
[root@VM_88_88_centos worldpress]# docker images
REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
worldpress                                     latest              9f0b470b5ddb        12 minutes ago      420 MB
docker.io/php                                  5.6-apache          eb8333e24502        5 days ago          389.7 MB                    
```

使用 Dockerfile 来构建镜像有以下建议：
1. 尽量精简，不安装多余的软件包。
2. 尽量选择 Docker 官方提供镜像作为基础版本，减少镜像体积。
3. Dockerfile 开头几行的指令应当固定下来，不建议频繁更改，有效利用缓存。
4. 多条 RUN 命令使用'\'连接，有利于理解且方便维护。
5. 通过 -t 标记构建镜像，有利于管理新创建的镜像。
6. 不在 Dockerfile 中映射公有端口。
7. Push 前先在本地运行，确保构建的镜像无误。

## 执行 Commit 实现打包生成镜像
通过 Dockerfile 可以快速构建镜像，而通过 commit 生成镜像可以解决应用在部署过程中有大量交互内容以及难以通过 Dockerfile 构建的问题。

通过 commit 构建镜像操作如下：
1. 运行基础镜像容器，并进入console。
```shell
[root@VM_88_88_centos ~]# docker run -i -t centos
[root@f5f1beda4075 /]# 
```
2. 安装需要的软件，并添加配置。
```shell
[root@f5f1beda4075 /]# yum update && yum install  openssh-server
Loaded plugins: fastestmirror, ovl
base                                                                                                                                                                    | 3.6 kB  00:00:00     
extras                                                                                                                                                                  | 3.4 kB  00:00:00     
updates                                                                                                                                                                 | 3.4 kB  00:00:00     
(1/4): base/7/x86_64/group_gz                                                                                                                                           | 155 kB  00:00:00     
(2/4): extras/7/x86_64/primary_db                                                                                                                                       | 166 kB  00:00:00     
(3/4): base/7/x86_64/primary_db                                                                                                                                         | 5.3 MB  00:00:00     
(4/4): updates/7/x86_64/primary_db 
......
......
......
Dependency Installed:
  fipscheck.x86_64 0:1.4.1-5.el7              fipscheck-lib.x86_64 0:1.4.1-5.el7              openssh.x86_64 0:6.6.1p1-25.el7_2              tcp_wrappers-libs.x86_64 0:7.6-77.el7             
Complete!
```

3. 配置完成后打开新终端保存该镜像。
```
shell
[root@VM_88_88_centos ~]# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
f5f1beda4075        centos              "/bin/bash"         8 minutes ago       Up 8 minutes                            hungry_kare
[root@VM_88_88_centos ~]# docker commit f5f1beda4075 test:v1.0      
sha256:65325ffd2af9d574afca917a8ce81cf8a710e6d1067ee611a87087e1aa88e4a4
[root@VM_88_88_centos ~]# 
[root@VM_88_88_centos ~]# docker images
REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
test                                           v1.0                65325ffd2af9        11 seconds ago      307.8 MB
```

