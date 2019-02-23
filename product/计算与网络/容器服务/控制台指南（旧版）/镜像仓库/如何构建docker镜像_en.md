## Description
DockerHub provides a large number of available images. For more information, please see [DockerHub Official Website](https://hub.docker.com/).

Docker container is designed to allow users to run programs independently in a relatively independent environment.

Docker container program will exit automatically when the program running in the image is completed. To keep the built image running in the service, you need to specify the programs that run persistently on the service creation page, such as main business program, main function entry, etc.

Given the diversity of enterprise environment, not all applications have corresponding images to use in DockerHub. The following tutorial will help you understand how to package applications into Docker image.

Currently, Docker generates images using the following two methods:

- Build images automatically using Dockerfile;
- Use container and execute `Commit` to generate image.


## Compile and Generate Image Automatically through Dockerfile (Recommended)
Take WordPress provided on the Dockerhub official website as an example. [Go to GitHub for more information](https://github.com/docker-library/wordpress/blob/7d40c4237f01892bb6dbc67d1a82f5b15f807ca1/php5.6/apache/Dockerfile).

The Dockfile source code is as follows:
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

As shown in the above Dockerfile file, the software is installed and deployed by running multiple built-in Linux commands.
Create a folder on the terminal to store the Dockerfile file, and build image by executing "docker build" command.

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
You can view the image you built by executing "docker images" command.
```shell
[root@VM_88_88_centos worldpress]# docker images
REPOSITORY                                     TAG                 IMAGE ID            CREATED             SIZE
worldpress                                     latest              9f0b470b5ddb        12 minutes ago      420 MB
docker.io/php                                  5.6-apache          eb8333e24502        5 days ago          389.7 MB                    
```

When building an image using Dockerfile, follow these suggestions:
1. Keep the image simple and avoid installing redundant software packages.
2. Choose official Docker image as the base tag, to reduce image size.
3. The commands in the first few lines of Dockerfile should be fixed. Avoid modifying these commands frequently to make efficient use of cache.
4. Multiple RUN commands are connected using "\" for better understanding and easy maintenance.
5. Build images using the "-t" flag, to help manage newly created images.
6. Do not map public ports in Dockerfile.
7. Run the image locally before pushing, to ensure the image is built without errors.

## Execute Commit to Generate Image
You can build image quickly by using Dockerfile, while generating image through Commit can solve the problem when it's difficult to build image through Dockerfile due to a large amount of interactive contents in the process of application deployment.

To build an image through Commit, follow the steps below:
1. Run the base image container and enter the console.
```shell
[root@VM_88_88_centos ~]# docker run -i -t centos
[root@f5f1beda4075 /]# 
```
2. Install the required softwares and add configurations.
```shell
[root@f5f1beda4075 /]# yum update && yum install openssh-server
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

3. After configuration is completed, open new terminal and save the image.
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


