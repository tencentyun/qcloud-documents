### 1. What is cache purge?
Cache purge includes URL purge, directory purge, and URL prefetch. (For more information, please see [Cache Purge](https://cloud.tencent.com/document/product/228/6299)
- URL purge means to purge the cache on a file-by-file basis.
- Directory purge means to purge all the files under a directory on a file-by-file basis.
- URL prefetch means to prefetch resources on a file-by-file basis.

Purge vs. prefetch:
- After purge, the resource cached on the CDN nodes across the network is deleted. When a user's request reaches a node, the node will pull the requested resource from the origin server and then cache it while returning it to the user. In this way, it can be guaranteed that the user can get the up-to-date resources.
- After prefetch, the resource is cached on the CDN nodes across the network in advance. When a user's request reaches a node, the user can directly get the resource from the node.

### 2. What are the requirements for cache purge? How long does it take effect?
Cache purge includes URL purge, directory purge, and URL prefetch.
URL purge: A maximum of 10,000 URLs are allowed to be purged each day and a maximum of 1,000 URLs are allowed to be submitted for each purge. It takes about 5 minutes for the purge to take effect. If the cache validity period set for the file is less than 5 minutes, it is recommended to wait for the timeout and update, instead of using the purge tool.
Directory purge: A maximum of 100 directories are allowed to be purged each day and a maximum of 20 URL directories are allowed to be submitted for each purge. It takes about 5 minutes for the purge to take effect. If the cache validity period set for the folder is less than 5 minutes, it is recommended to wait for the timeout and update, instead of using the purge tool.
URL prefetch: This feature is only available for key CDN customers. If the resource has been cached on the node and has not expired, it will not be updated to the latest one. If you need to update the resources on all CDN nodes to the latest ones, you can purge them before prefetch. A maximum of 1,000 URLs are allowed to be prefetched each day and a maximum of 20 URLs are allowed to be submitted for each prefetch. It takes about 5 to 30 minutes for the prefetch to take effect, depending on the file size.

### 3. Will the cached content at CDN acceleration nodes be updated in real time?
No. The cached content at CDN nodes are updated based on the [cache expiration configuration](https://cloud.tencent.com/document/product/228/6290) you set on the console. If you need to update a file's cache in real time, do it by [purging cache](https://cloud.tencent.com/document/product/228/6299).

### 4. Is directory purge supported by CDN?
Yes. CDN supports URL purge, directory purge, and URL prefetch.
Method 1: [Purge the directory](https://console.cloud.tencent.com/cdn/refresh) on Tencent Cloud CDN console. For more information, please see [Cache Purge](https://cloud.tencent.com/document/product/228/6299).
Method 2: Purge the URL by calling the API. For more information, please see [URL Purge](https://cloud.tencent.com/document/product/228/3946).

### 5. How can I check the cache purge history?
You can check the cache purge history on the CDN console. For more information, please see [History](https://cloud.tencent.com/document/product/228/6299#.E6.93.8D.E4.BD.9C.E8.AE.B0.E5.BD.95).

### 6. Why doesn't directory prefetch or purge take effect?
Check whether Last-Modified of the origin server is changed. If it is changed, a failure of origin-pull will occur. If you cannot solve the problem, [submit a ticket](https://console.cloud.tencent.com/workorder/category) to notify the OPS personnel.
