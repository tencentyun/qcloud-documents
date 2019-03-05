
## How does SSL mutual authentication work

- The browser sends a connection request to the secure server.
- The server sends its certificate along with the certificate-related information to the client browser.
- The client browser checks whether the certificate sent from the server is issued by the CA center it trusts. If so, it will continue performing the protocol; otherwise, the client browser will send the user a warning message indicating this certificate is not credible and asking whether it wants to continue.
- Next, the client browser checks whether the information (such as domain name and public key) in the certificate is consistent with the relevant information sent by the server just now. If so, the client browser will recognize the authenticity of this server's identity.
- The server requests the client to send its own certificate. After receiving the certificate, the server verifies the client's certificate. If the verification fails, the server will reject the connection request; otherwise, the server will get the user's public key.
- The client browser sends the server a message indicating the communication symmetric encryption schemes it supports.
- The server selects an encryption scheme with the highest encryption level from the encryption schemes sent from the client, and sends the scheme that is encrypted with client's public key to the browser.
- The browser selects a session key for this encryption scheme, then uses server's public key to encrypt the session key and sends it to the server.
- When receiving the message from the browser, the server decrypts the message with its private key to get the session key.
- The subsequent communications between the server and browser will be performed using the symmetric encryption scheme with the encrypted symmetric key.

Mutual authentication means that the server and client authenticate each other and the server can only be accessed by the clients permitted by the server. This can result in a much higher security.

## How does SSL unidirectional authentication work

- The client browser sends the server the version number of SSL protocol, type of encryption algorithm, generated random numbers, and all the information needed in the communication between the server and client.
- The server sends the client the version number of SSL protocol, type of encryption algorithm, generated random numbers, and other relevant information as well as its certificate.
- The client uses the information sent from the server to verify the validity of the server, including whether the certificate is expired, whether the CA issuing the server certificate is credible, whether the public key of CA's certificate can correctly decrypt the CA's digital signature in the server certificate, and whether the domain name in the server certificate matches the server's actual domain name. If the validity verification fails, the communication will be disconnected; otherwise go to step 4.
- The client randomly generates a "symmetric key" for the communication later, and uses server's public key (obtained from the server certificate in step 2) to encrypt it, and then sends the encrypted "pre-master key" to the server.
- If the server requests for an authentication against the client (optional in handshake), the user can generate a random number which is then signed digitally, and sends the signed random number, along with client certificate as well as the encrypted "pre-master key" to the server.
- If the server requests for an authentication against the client, it must verify the validity of client certificate and signed random number, including: whether the certificate is expired, whether the CA issuing the certificate to the client is credible, whether the CA's public key can correctly decrypt the CA's digital signature in the client certificate, and whether the client certificate is in the Certificate Revocation List (CRL). If the verification fails, the communication will be disconnected immediately; otherwise, the server will use its own private key to decrypt the encrypted "pre-master key", and then perform a series of steps to generate a master key (the client will generate the same master key in the same way).
- The server and the client use the same master key (i.e. "session key"), a symmetric key, to encrypt and decrypt the SSL protocol-based secure data communication. Meanwhile, during the SSL communication, both sides need to make sure the integrity of data communication and avoid any changes in data communication.
- The client sends the server a message indicating that the master key in the previous step will be used as a symmetric key in the subsequent data communications and that the handshake at the client side has ended.
- The server sends the client a message indicating that the master key in the previous step will be used as a symmetric key in the subsequent data communications and that the handshake at the server side has ended.
- With the ending of handshake of SSL communication, the data communication in SSL secure channel starts. The client and the server start to use the same symmetric key for data communication while verifying the integrity of the communication data.

SSL unidirectional authentication only requires the SSL certificate to be deployed on the site. Any user can access the site (except for the restricted IPs) and only the server needs to provide the authentication information.

## Difference between SSL Mutual Authentication and SSL Unidirectional Authentication

In SSL mutual authentication, both server and client are required to have certificates, while  in SSL unidirectional authentication, CA certificate is not required on the client side.

Compared to the above steps, unidirectional authentication only eliminates the step in which the server verifies the client certificate. In addition, during the negotiation concerning symmetric encryption scheme and symmetric session key between the two sides, the encryption scheme sent from the server to the client s unencrypted (this will not affect the security of SSL procedure). In this way, the communication content between the two sides are encrypted data, and any third party launching a attack only obtains the encrypted data. The third party needs to decrypt the encrypted data to get useful information, and in this case, the security hinges on the security of encryption scheme. The encryption schemes available at present are sufficiently secure as long as the communication key is long enough. This is why we use 128-bit encrypted communication.

Generally, Web applications are simply configured with SSL unidirectional authentication. For some users in financial industry, an authentication against the client may be required for their application interfacing. In this case, SSL mutual authentication is needed.
