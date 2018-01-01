An image processing company leverages Tencent Cloud to provide an online image processing service that allows users to upload photos and edit them by cropping, removing red eye , whitening teeth , re-coloring, changing brightness, creating thumbnails, and so on. The whole process is as such: the user uploads the images, submits the tasks, waits for the images to edit, and downloads the edited images. The processing time varies depending on the effect the user applies on the image, and the user may upload dozens or even hundreds of pictures in parallel. Therefore, the total processing time is determined by the number of images to upload, image size and the effects the user applies on these images.

![](https://mc.qcloudimg.com/static/img/2046bcf206af343f274fd05c5f4ab3f0/image.png)

Tencent Cloud CMQ meets the above requirements: The user's images are stored in Tencent Cloud storage (such as CBS/COS); each operation request is saved as a message (image index, consisting of the image name + the operation type requested by the user + the index key of the image storage location) into the Request Queue.

The image processing service on the CVM receives the message (image index) from the Request Queue. The image processing server downloads the images from the cloud, edits them, sends the processing results to the Response Queue, and stores the edited images in the cloud storage. After that, the original and edited images are both stored in the cloud storage for customers to download at any time.

Tencent Cloud CMQ demonstrates high scalability and reliability under the following circumstances:

- If the image processing service is temporarily unavailable due to a bug or other causes, the system will inform the user of the error via CMQ. On the one hand, the user can continue to upload photos, the web server can continue to send a message to the Request Queue, and the message will be saved in the queue until the image processing service is available; one the other hand, the image processing service does not have to remember the messages that were processed before the crash, and the messages that were processed when it crashed could also be reprocessed. The feature of CMQ in receiving messages (including the sequential and concurrent queued messages) allows the message to remain in the queue upon receipt, until the recipient of the message explicitly removes it. It ensures that image processing and image uploading work independently of each other.

- If a single image processing service cannot meet the needs of users (or users have to wait for a long time to get the processing results after uploading the images), CMQ plus multiple image processing services will be able to meet the growing user access demands. The reasons why CMQ can meet such demands are:
1) A CMQ queue can be accessed by multiple servers to send, receive and delete concurrent queued messages at the same time;
2) A message can only be received by one server at a time and will be temporarily locked. The recipient of the message can specify the time when the message is locked, and delete the message after processing it. If the recipient fails to process the message, another service can get the message after the lock of the message expires.

These two features ensure that the number of processing servers can be dynamically increased or decreased as the load changes.
