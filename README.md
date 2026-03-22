# sdev245-mod1

This week we have explored the key concept of the CIA triad. The CIA triad is comprised of three components: confidentiality, integrity, and availability.

Confidentiality means that data and resources in a system are only accessible by the desired users. This is done using an authentication procedure such as username and password login system, as well as with authorization methods such as the various access controls available. Some of the possible access controls could be role-based, relationship-based, or discretionary.

Integrity means that the data in the system is accurate and unaltered. Malicious actors could tamper with stored or transmitted data, so using tools such as hashing to ensure that data is consistent is key.

Availability means that information and resources are available to users when they need to access them. A common reason for disruption in service is a Denial of Service (DoS) attack. To help prevent outages an organization can have failover plans and ensure to update software and hardware as regularly as possible.

This exercise demonstrates the concept of access controls. This is a role-based access control in which the role assigned to the user determines what functions they are allowed to perform in the system.

In this short script, the user “bigBoss” is a hardcoded user that has the role of admin. Depending on whether the logged in user is an admin or user role, they are prompted with different questions necessitating input. Both logic paths are independent of each other so only an admin role goes down first logic path and only a user role goes down the second path.
