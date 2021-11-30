
## 1. Which encryption suites are supported by HTTPS?

ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-CHACHA20-POLY1305:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128:AES256:AES:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK

## 2. Which versions of SSL/TLS security protocols are supported by HTTPS?

Cloud Load Balancer HTTPS currently supports the following SSL protocols: TLSv1, TLSv1.1, TLSv1.2

## 3. Which port should be used for HTTPS listener?

There is no mandatory requirement for this. Port 443 is recommended.

## Why is HTTPS mutual authentication needed?

Some customers have a higher requirement for data security, such as those who deal with financial services. They require HTTPS authentication to be carried out on both server and client. In order to cater for the needs of such customers, we have launched HTTPS mutual authentication.

## 5. Why does HTTPS protocol actually generate more traffic than the billed traffic?

If HTTPS protocol is used, it actually generates more traffic than the billed traffic since some traffic are used for the protocol handshake.

## 6. When the HTTPS listener has been added, are the requests between the Cloud Load Balancer and back-end CVM still transmitted over HTTP protocol?

Yes. When the HTTPS Listener has been added, requests between the client and Cloud Load Balancer are encrypted over HTTPS protocol, and requests between the Cloud Load Balancer and back-end CVM are still transmitted over HTTP protocol. Therefore, there is no need to make SSL configuration for back-end CVM.

## 7. What types of certificates are supported by CLB currently?

It currently supports the upload of server certificate and CA certificate. For server certificate, both certificate content and private key are required to be uploaded. For CA certificate, only certificate content is required to be uploaded. Both types of certificates only support upload in PEM encoding format.

## 8. How many HTTPS certificates can be bound to a listener?

If HTTPS unidirectional authentication is used, only one server certificate can be bound to a listener. If HTTPS mutual authentication is used, one server certificate and one CA certificate are required to be bound to a listener.

## 9. How many Cloud Load Balancers or listeners can a certificate be applied to?

A certificate can be applied to one or multiple Cloud Load Balancers, or multiple listeners.

## 10. How to upload a certificate?

You can upload it by using API or Cloud Load Balancer console.

## 11. Are the certificates region-sensitive?

Yes. If a user's certificate needs to be used in multiple regions, it is necessary to upload the certificate in multiple regions to ensure the security and performance.

## 12. Can a certificate be deleted after being uploaded?

The Deletion function is not available now.

## 13. Do the certificates need to be uploaded to back-end CVM?

No. Cloud Load Balancer HTTPS provides the Certificate Management System to manage and store user certificates. Certificates do not need to be uploaded to back-end CVM, and all the private keys uploaded to the Certificate Management System are stored in an encrypted form.

## 14. What to do after a certificate expires?

When the current certificate expires, users need to update the certificate manually.

## 15. What to do when an error occurs while adding a certificate?

This maybe caused by the wrong content of private key. In this case, user need to replace it with a new certificate that meets the requirements.

