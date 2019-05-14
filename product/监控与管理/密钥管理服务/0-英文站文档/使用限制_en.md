* A maximum of 200 CMKs can be created in each region.
* Different CMK is created in different region. Pay attention to the region specified in the cloud API during access.
* Alias must be unique in the region.
* To enhance security, the frequency at which the cloud API is called is limited. The upper limit is different depending on the usage.

    1) Key-operating APIs (Encrypt, Decrypt, GenerateDataKey) are called at a frequency of 600 counts per second.

    2) Key-managing APIs (all APIs except for key-operating APIs) are called at a frequency of 30 counts per second.
