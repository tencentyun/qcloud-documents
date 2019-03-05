## Gene Sequencing
Bioinformatics companies or labs obtain the original file of genomic sequences using a sequencer, and upload the preliminary analysis result of genomic sequences to a cloud storage system, such as COS. Then, they can use Tencent Cloud Batch to complete their secondary analysis.

![Gene Sequencing](https://mc.qcloudimg.com/static/img/810c499a0a74a2fba07fbe439ff6c7b1/image.png)

#### Common Steps
1. Bioinformatics experts obtain the original information from the sequencer or private cloud storage, and upload this information to a Tencent Cloud storage service, such as COS, CFS.
2. Users define a Batch job for analyzing information, and then submit this job. The storage configuration of the job is associated with the original information in the previous step.
3. Batch automatically schedules the resources, and deploys the custom analysis image uploaded by users to the scheduled CVM. Meanwhile, it automatically schedules the job to analyze the original information.
4. After the computing task is completed on CVM, Batch automatically uploads the analysis result to the location specified by users.
Upload the original information to be analyzed to COS.

## Movie, Video and Effect Picture Rendering
In vision creation industries such as movie and video, advertising and construction planning, content producers and post-production companies need to use a great number of machines to finish the rendering work for special effects, three-dimensional animations and special effect pictures. Tencent Cloud Batch provides users with the ability to automate the procedure of content rendering. You can build your own rendering-dependent process and use the massive resources and job scheduling capability of Batch to finish the vision creation job efficiently.

![Movie, Video and Effect Picture Rendering](https://mc.qcloudimg.com/static/img/c667521cad604d95cd9ef0efe011a361/image.png)

#### Common Steps
1. Users prepare the original materials required for rendering and upload them to a Tencent Cloud storage service, such as COS, CFS.
2. Users define a Batch job to analyze the information, and then submit this job. The storage configuration of the job is associated with the original information in the previous step.
3. Batch automatically schedules the resources, then deploys the custom rendering image uploaded by users to the scheduled CVM. Meanwhile, it automatically schedules the job to render videos or effect pictures.
4. After the rendering process is completed on CVM, Batch automatically uploads the generated videos or effect pictures to the location specified by users.

