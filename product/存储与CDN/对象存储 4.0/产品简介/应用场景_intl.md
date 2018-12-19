## UGC Upload via Multiple Nodes
In such scenario, COS provides large IO throughput, which better solved the problem of concurrent uploads via multiple nodes. In addition, COS automatically selects the nearest node to upload UGC, which significantly shortens the queuing time of pictures and documents to be uploaded at the terminal and increases the success rate of file upload.

## Online Disk with Frequent IO
For online disk that requires frequent uploads and downloads, Cloud Object Storage has better scalability than the original NAS device. COS can automatically expand the volume along with the increasing of user data. For concurrent access, COS has more bandwidth support than the traditional NAS device, avoiding access delay or unavailable service.

## Mass Data Archiving and Backup
COS provides a set of hierarchical storage solutions for cold data storage. It is recommended that you store the data with low access frequency and low access speed demand in the Low-frequency Storage. Such method can reduce the storage costs by 40% while maintaining the data stability, providing massive low cost spaces for data archiving and backup.

## Hot Resources Delivery and Download
For delivery of hot files such as VOD sources and game resources, COS together with CDN allows you to flexibly deal with high-traffic and high-concurrency business scenarios. You can use COS as an origin server, place hot resources in the COS, and then deliver the resources to the end user via CDN. Such method will reduce your delivery traffic costs and terminal access delay, and Tencent's strong bandwidth support can resolve your concern of inability to access your business due to heavy traffic.
