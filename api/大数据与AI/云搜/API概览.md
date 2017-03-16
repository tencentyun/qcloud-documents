| 接口功能 | Action ID | 
|---------|---------|
| 数据操作 | [DataManipulation](http://www.qcloud.com/doc/api/256/%E6%95%B0%E6%8D%AE%E6%93%8D%E4%BD%9C) | 
| 数据检索 | [DataSearch](http://www.qcloud.com/doc/api/256/%E6%95%B0%E6%8D%AE%E6%A3%80%E7%B4%A2) | 

<script type="text/plugin"  data-type = "code" action="start"> </script>

```C++
using Google.Cloud.Storage.V1;
using System;
using System.Diagnostics;

namespace GoogleCloudSamples
{
    class StorageQuickstart
    {
        static void Main(string[] args)
        {
            // Your Google Cloud Platform project ID.
            string projectId = "YOUR-PROJECT-ID";


            // Instantiates a client.
            StorageClient storageClient = StorageClient.Create();

            // The name for the new bucket.
            string bucketName = projectId + "-test-bucket";
            try
            {
                // Creates the new bucket.
                storageClient.CreateBucket(projectId, bucketName);
                Console.WriteLine($"Bucket {bucketName} created.");
            }
            catch (Google.GoogleApiException e)
            when (e.Error.Code == 409)
            {
                // The bucket already exists.  That's fine.
                Console.WriteLine(e.Error.Message);
            }
        }
    }
}
```
```GO
// Sample storage-quickstart creates a Google Cloud Storage bucket.
package main

import (
        "fmt"
        "log"

        // Imports the Google Cloud Storage client package.
        "cloud.google.com/go/storage"
        "golang.org/x/net/context"
)

func main() {
        ctx := context.Background()

        // Sets your Google Cloud Platform project ID.
        projectID := "YOUR_PROJECT_ID"

        // Creates a client.
        client, err := storage.NewClient(ctx)
        if err != nil {
                log.Fatalf("Failed to create client: %v", err)
        }

        // Sets the name for the new bucket.
        bucketName := "my-new-bucket"

        // Creates a Bucket instance.
        bucket := client.Bucket(bucketName)

        // Creates the new bucket.
        if err := bucket.Create(ctx, projectID, nil); err != nil {
                log.Fatalf("Failed to create bucket: %v", err)
        }

        fmt.Printf("Bucket %v created.\n", bucketName)
}
```
```JAVA
// Sample storage-quickstart creates a Google Cloud Storage bucket.
package main

import (
        "fmt"
        "log"

        // Imports the Google Cloud Storage client package.
        "cloud.google.com/go/storage"
        "golang.org/x/net/context"
)

func main() {
        ctx := context.Background()

        // Sets your Google Cloud Platform project ID.
        projectID := "YOUR_PROJECT_ID"

        // Creates a client.
        client, err := storage.NewClient(ctx)
        if err != nil {
                log.Fatalf("Failed to create client: %v", err)
        }

        // Sets the name for the new bucket.
        bucketName := "my-new-bucket"

        // Creates a Bucket instance.
        bucket := client.Bucket(bucketName)

        // Creates the new bucket.
        if err := bucket.Create(ctx, projectID, nil); err != nil {
                log.Fatalf("Failed to create bucket: %v", err)
        }

        fmt.Printf("Bucket %v created.\n", bucketName)
}
```
```PHP
// Sample storage-quickstart creates a Google Cloud Storage bucket.
package main

import (
        "fmt"
        "log"

        // Imports the Google Cloud Storage client package.
        "cloud.google.com/go/storage"
        "golang.org/x/net/context"
)

func main() {
        ctx := context.Background()

        // Sets your Google Cloud Platform project ID.
        projectID := "YOUR_PROJECT_ID"

        // Creates a client.
        client, err := storage.NewClient(ctx)
        if err != nil {
                log.Fatalf("Failed to create client: %v", err)
        }

        // Sets the name for the new bucket.
        bucketName := "my-new-bucket"

        // Creates a Bucket instance.
        bucket := client.Bucket(bucketName)

        // Creates the new bucket.
        if err := bucket.Create(ctx, projectID, nil); err != nil {
                log.Fatalf("Failed to create bucket: %v", err)
        }

        fmt.Printf("Bucket %v created.\n", bucketName)
}
```

<script type="text/plugin" action="end"></script>

