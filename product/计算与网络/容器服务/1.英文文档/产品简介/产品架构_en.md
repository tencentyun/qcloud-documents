## Product Architecture

### Overall Architecture
This section describes the design and implementation of CCS system, and its product architecture is as follows:
![Alt text](https://main.qcloudimg.com/raw/599ac1bdd73c895ba7ca6a23dc55790a.jpg)

CCS consists of the following modules:

- **CCS console and APIs**: Users work with clusters and services through the console and cloud APIs.
- **User terminal**: Users perform operations such as upload/download and automatic building of images on their terminals or UI provided by Docker.
- **Image service modules:** Users can upload or download images locally using the image service modules provided by Tencent Cloud.
- **Container service modules**: The core CCS modules, including addition, deletion, modification and query of clusters and services.



