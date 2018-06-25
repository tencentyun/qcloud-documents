# Guide to *Dockerfile Path* and *Building Directory* for Building with Source Code

Tencent CCS provides the capability of auto image building. In the configuration for building with source code, you can specify the *Dockerfile Path* and *Building Directory*.

## How to Enter the *Dockerfile Path* and *Building Directory* for Building with Source Code ?

![][pic1]

Answer: **Enter the relative path to the project's root path.**

If you leave it blank, the system will provide its default value:

* The default vale of *Dockerfile Path* is: *Dockerfile* (`Dockerfile`) under the root directory of the code repository.
* The default value of *Building Directory* is: the root directory (`./`) of the code repository.

## How to Use *Dockerfile Path* and *Building Directory* for Building with Source Code?

To implement the feature of building images with source code, you first need to clone the user-specified repository, then switch to the corresponding branch or tag, and finally execute the command `docker build -f $DOCKERFILE_PATH $WORKDIR` in the root directory of the code repository to build a container image.

## How to Specify the Source Path in Dockerfile?

The source path should be a *Path Relative* to the *Building Directory* for  `COPY`, `ADD` and other commands related to the path.

[pic1]:https://mc.qcloudimg.com/static/img/33d587e49512bbee6ebc19d2f1961f94/pic1.png

