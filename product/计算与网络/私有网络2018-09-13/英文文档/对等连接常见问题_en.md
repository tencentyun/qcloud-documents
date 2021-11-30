## 1. Can a peering connection be established between two VPCs with overlapped IP addresses?
No. The IP ranges of the VPCs at the two sides of the peering connection must not overlap. [Click to view the usage constraints for peering connections](https://cloud.tencent.com/doc/product/215/5000#.E4.BD.BF.E7.94.A8.E7.BA.A6.E6.9D.9F).

## 2. If a peering connection is established between VPC A and VPC B, and another peering connection is established between VPC B and VPC C, does it mean VPC A and VPC C are connected?
No. Peering connections are non-transitive.

## 3. Is there a bandwidth limit for peering connections?
A bandwidth limit can be set when a **cross-region peering connection** is created using an API. Bandwidth limit for the console will be supported in the near future.
For the **peering connection within the same region**, there is no bandwidth fee and no bandwidth limit.

## 4. If I delete the peering connection on my side, can the other side access my VPC?
No. Either of the two sides of the peering connection can interrupt the peering connection at any time.
