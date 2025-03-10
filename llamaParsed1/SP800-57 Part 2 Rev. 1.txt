```markdown
# Abstract

NIST Special Publication (SP) 800-57 provides cryptographic key management guidance. It consists of three parts. Part 1 provides general guidance and best practices for the management of cryptographic keying material. Part 2 provides guidance on policy and security planning requirements. Finally, Part 3 provides guidance when using the cryptographic features of current systems. Part 2 (this document) 1) identifies the concepts, functions and elements common to effective systems for the management of symmetric and asymmetric keys; 2) identifies the security planning requirements and documentation necessary for effective institutional key management; 3) describes Key Management Specification requirements; 4) describes cryptographic Key Management Policy documentation that is needed by organizations that use cryptography; and 5) describes Key Management Practice Statement requirements. Appendices provide examples of some key management infrastructures and supplemental documentation and planning materials.

## 1. Introduction

Cryptographic mechanisms are often used to protect the integrity and confidentiality of data that is sensitive, has a high value, or is vulnerable to unauthorized disclosure or undetected modification during transmission or while in storage. A cryptographic mechanism relies upon two basic components: an algorithm (or cryptographic methodology) and a variable cryptographic key. The algorithm and key are used together to apply cryptographic protection to data (e.g., to encrypt the data or to generate a digital signature) and to remove or check the protection (e.g., to decrypt the encrypted data or to verify a digital signature). This is analogous to a physical safe that can be opened only with the correct combination.

Two types of cryptographic algorithms are in common use today: symmetric key algorithms and asymmetric key algorithms. Symmetric key algorithms (sometimes called secret key algorithms) use a single key to both apply cryptographic protection and to remove or check the protection. Asymmetric key algorithms (often called public key algorithms) use a pair of keys (i.e., a key pair): a public key and a private key that are mathematically related to each other. In the case of symmetric key algorithms, the single key must be kept secret from everyone and everything not specifically authorized to access the information being protected. In asymmetric key cryptography, only one key in the key pair, the private key, must be kept secret; the other key can be made public. Symmetric key cryptography is most often used to protect the confidentiality of information or to authenticate the integrity of that information. Asymmetric key cryptography is commonly used to protect the integrity and authenticity of information and to establish symmetric keys. Given differences in the nature of symmetric and asymmetric key cryptography and of the
```# Requirements of Different Security Applications of Cryptography

Specific key management requirements and methods necessarily vary from application to application. Regardless of the algorithm or application, if cryptography is to deliver confidentiality, integrity, or authenticity, users and systems need to have assurance that the key is authentic, that it belongs to the entity with whom or which it is asserted to be associated, and that it has not been accessed by an unauthorized third party. SP 800-57, Recommendation for Key Management (hereafter referred to as SP 800-57 or the Recommendation), provides guidelines and best practices for achieving this necessary assurance.

## SP 800-57 Overview

SP 800-57 consists of three parts. This publication is Part 2 of the Recommendation (i.e., SP 800-57 Part 2 – Best Practices for Key Management Organizations) and is intended primarily to address the needs of U.S. government system owners and managers who are setting up or acquiring cryptographic key management capabilities. Parts 1 and 3 of SP 800-57 focus on cryptographic key management mechanisms. SP 800-57 Part 1, General, (hereafter referred to as Part 1) contains basic key management guidance intended to advise users, developers and system managers; and SP 800-57 Part 3, Application-Specific Key Management Guidance, (hereafter referred to as Part 3) is intended to address specific key management issues associated with currently available implementations.

SP 800-57 has been developed by and for the U.S. Federal Government. Non-governmental organizations may voluntarily choose to follow the practices provided herein.

## 1.1 Scope

This publication (hereafter referred to as Part 2) 1) identifies concepts, functions, and elements that should be common to cryptographic key management systems (CKMS); 2) identifies the security planning requirements and documentation necessary to effective organizational key management; and 3) describes cryptographic Key Management Policy and practice documentation and Key Management Specifications that are needed by organizations that use cryptography.

Although there are distinctions between symmetric and asymmetric key management requirements, there is an extensive set of management principles and organizational requirements that are common to both. This publication presents common key management requirements and identifies distinct symmetric algorithm-specific and asymmetric algorithm-specific requirements, when appropriate. This publication also makes recommendations to enterprise organizations for the management of cryptographic keys, the management of metadata associated with those keys (e.g., identifying information associated with the owners of keys, the lengths of keys, and acceptable uses for those keys), and the maintenance of associations between metadata and keys.

This publication is intended to acquaint system owners and managers of organizations.# Implementing and Using Cryptography

This document outlines the requirements that must be satisfied when cryptography is implemented in organizations. It does not address specific key management protocols, implementations, or the operation of key management components or systems. It focuses on principles and requirements that will need to be met by the key management protocols, components, systems, and services used by organizations.

## Key Management Protocols

Key management protocols are documented and coordinated rules for exchanging keys and metadata (e.g., in X.509 certificates). Key management components include the software module applications and hardware security modules (HSMs) that are used to generate, establish, distribute, store, account for, suspend, revoke, or destroy cryptographic keys and metadata.

## Cryptographic Key Management Systems (CKMS)

Cryptographic key management systems (CKMS) are composed of individual components and are used to carry out sets of key management functions or services. Key management services include the generation, destruction, revocation, distribution, and recovery of keys. Some CKMS services (e.g., certificate authority (CA)) may be provided by a third party under contract or Service Level Agreement.

## Applicable Laws and Directives

This document identifies applicable laws and directives concerning security planning and management and suggests approaches to satisfying those laws and directives with a view to minimizing the impact of the management overhead on organizational resources and efficiency. Part 2 also acknowledges that planning and documentation requirements associated with small-scale or single-system organizations will not need to be as elaborate as those required for large and diverse government agencies that are supported by multiple information technology systems.

## Key Management Policy

However, any organization that employs cryptography to provide security services needs to have key management policy, practices, and planning documentation. Part 2 recognizes that some key management functions, such as the provisioning and revocation of keys, are sufficiently labor-intensive that they act as an impediment to the adoption of cryptographic mechanisms – particularly in large network operations.

## Importance of Responsible Key Management

Nevertheless, responsible key management is essential to the effective use of cryptographic mechanisms for protecting information technology systems against attacks that threaten the confidentiality of the information processed, stored, and communicated; the integrity of information and systems operation; and the timely availability of critical information and services. Improved tools for the automation of many key management services are needed to improve the security, performance, and usability of CKMSs, but the characteristics identified in SP 800-57 as essential to secure and effective key management are valid and independent of performance and usability concerns.

## 1.2 Audience

The primary audience for Part 2 is the set of federal government system owners and managers who are setting up or acquiring cryptographic key management capabilities. However, consistent with...# Cybersecurity Enhancement Act of 2014

the Cybersecurity Enhancement Act of 2014 (PL 113-274), this Recommendation is also intended to provide cybersecurity guidelines to the private sector in addition to the government-focused guidance consistent with Office of Management and Budget (OMB) Circular A-130 (OMB 130). Since guidelines and best practices for the private sector are strictly voluntary, the requirement terms (i.e., the should/shall language) used for some recommendations and requirements do not apply outside the federal government. For federal government organizations, the terms should and shall have the following meaning in this document:

1. **shall**: This term is used to indicate a requirement for U. S. Federal government organizations based on a Federal Information Processing Standard (FIPS) or NIST Recommendation. Note that shall may be coupled with not to become shall not.
2. **should**: This term is used to indicate an important recommendation. Ignoring the recommendation could result in undesirable results. Note that should may be coupled with not to become should not.

## 1.3 Background and Rationale

As stated above, although there are significant differences in key management requirements for symmetric and asymmetric key management applications, there are principles common to both. The proper handling of and accounting for keys is necessary for cryptographic functions to be effective. For example, regardless of the cryptographic method employed, some secret or private keys will need to be made available to some set of the entities that use cryptography. Trust in the source of these keys is essential to any confidence in the cryptographic mechanisms being employed. Access to the private or secret keys by entities that are not intended to use them invalidates any assumptions regarding the confidentiality or integrity of information believed to be protected by the associated cryptographic mechanisms.

Although organizations may generate keys for their members and distribute keys to their members, the only way to completely protect information being stored under a cryptographic key is for the entity(ies) responsible for storing the information to control the generation, distribution, and key storage processes. An example of the fundamental differences between the protection requirements for symmetric keys and those for asymmetric keys is that, in the symmetric case, each party that is authorized to use a (secret) key must protect that key in order to avoid all of the parties who also share the key from losing the cryptographic protection afforded under that key. In the asymmetric case, only the party that owns and is authorized to use the private key must protect the confidentiality of that key; the other key of the key pair -- the public key -- may be known by anyone, but its ownership must be verified in a trusted manner.

However, it is essential in both cases to keep track of cryptographic keys in use across an enterprise. Information regarding the compromise of a secret or private key or regarding its revocation for any reason must be available to all parties reliant on the security.# Services that Use the Key

At the device or software application level, keys need to be provided, changed, and protected in a manner that enables cryptographic operation and preserves the integrity of cryptographic processes and their dependent services. FIPS 140 provides guidance on implementing cryptography into a cryptographic module. Other government publications that specify technical key management requirements for specific applications include:

a) SP 800-56A, Recommendation for Pair-Wise Key Establishment Schemes Using Discrete Logarithm Cryptography;
b) SP 800-56B, Recommendation for Pair-Wise Key Establishment Schemes Using Integer Factorization Cryptography;
c) SP 800-56C, Recommendation for Key Derivation Methods in Key-Establishment Schemes;
d) SP 800-71, Recommendation for Key Establishment Using Symmetric Block Ciphers;
e) SP 800-108, Recommendation for Key Derivation Using Pseudorandom Functions;
f) SP 800-131A, Transitioning the Use of Cryptographic Algorithms and Key Lengths;
g) SP 800-132, Recommendation for Password-Based Key Derivation: Part 1: Storage Applications;
h) SP 800-133, Recommendation for Cryptographic Key Generation; and
i) SP 800-135, Recommendation for Existing Application-Specific Key Derivation Functions.

Technical mechanisms alone are not sufficient to ensure the protection of sensitive information. Part 2 specifies key management planning requirements for the development, acquisition, and implementation of cryptographic product and services. In federal government systems, technical mechanisms are required to be used in combination with a set of procedures that implement a clearly understood and articulated protection policy.

In order for key management practices and procedures to be effectively employed, support for these practices and procedures at the highest levels of the organization is a practical necessity. The executive level of the organization needs to establish policies that identify executive-level key management roles and responsibilities for the organization. The key management policies need to support the establishment of, or access to, the services of a key management infrastructure and the employment and enforcement of key management practices and procedures.

## 1.4 Organization

Part 2 of the Recommendation for Key Management is organized as follows:

- **Section 2** introduces key management concepts that must be addressed or understood by organizations that use cryptography to protect information so that they can create key management policies, practice statements and planning documents.
- **Section 3** provides guidance on planning for the use of cryptography, including the rationale for key management planning.
- **Section 4** provides information that supports the development of Key Management Specifications by describing the key management components that may be required to operate a cryptographic device or application.
- **Section 5** and **Section 6** provide guidance for the development of organizational cryptographic Key Management Policy statements and Key Management Practice.# Statements

The policy and practice documentation may take the form of separate planning and implementation documents or may be included in an organization's existing information security policies and procedures.

- Appendix A provides cryptographic key management system (CKMS) examples.
- Appendix B provides key management inserts for security plan templates.
- Appendix C provides a Key Management Specification checklist for cryptographic product development.
- Appendix D provides a table of references.
- Appendix E identifies changes from the original SP 800-57 Part 2 document.

## 1.5 Glossary of Terms and Acronyms

The definitions provided below are consistent with Part 1. Note that the same terms may be defined differently in other documents. Also note that summaries of some of the glossary definitions are used as footnotes throughout the document to assist the reader; the complete definition is provided in Section 1.5.1.

### 1.5.1 Glossary

## 2 Key-Management Concepts

This section introduces key-management concepts that must be addressed or understood by any organization that uses cryptography to protect its information so that they can create key management policies, practice statements, and planning documents. Section 2.1 describes key establishment fundamentals, and Section 2.2 lists basic key management functions. Section 2.3 provides a high-level overview of cryptographic key management systems (CKMS) -- the framework and services that provide for the generation, establishment, control, accounting, and destruction of cryptographic keys. Section 2.4 presents general design requirements for a CKMS, and Section 2.5 briefly addresses trust mechanisms. Finally, Section 2.6 addresses the suspension and revocation of keys.

### 2.1 Key Establishment

Key establishment is the process that results in the sharing of a key between two or more entities. This process could be by a manual distribution, by using automated key-transport or key-agreement mechanisms, or by key derivation using an already-shared key between or among those entities. Key establishment processes include the creation of a key. Key establishment techniques and issues are discussed in Section 5.3 of SP 800-175B.

During key establishment, a decision must be made about the length of each key's cryptoperiod (the length of time that each key may be used). Guidance on the selection of cryptoperiods is provided in Part 1.

### 2.2 Key-Management Functions

Each key management function needs to be addressed by an organization's cryptographic Key Management Policy. This is true for organizations already using cryptography as well as organizations that do not currently acquire, distribute, use, and manage keying material. Key management policies and practices need to be documented (see Sections 5 and 6). Roles and responsibilities need to be defined for the management of at least the following functions:

- The generation or acquisition of key information (i.e., keying material and the associated metadata);# CURRENT_PAGE_RAW_OCR_TEXT

- The secure distribution of private keys, secret keys and the associated metadata;
- The establishment of cryptoperiods;
- Key and/or certificate inventory management, including procedures for the routine supersession of keys and certificates at the end of a cryptoperiod or validity period;
- Procedures for the emergency revocation of compromised keys and the establishment (e.g., distribution) of replacement keys and/or certificates;
- Accounting for and the storage and recovery of the operational and backed-up copies of key information;
- The storage and recovery of archived key information;
- Procedures for checking the integrity of stored key information before using it; and
- The destruction of private or secret keys that are no longer required.

## 2.3 Cryptographic Key Management Systems (CKMS)

The term cryptographic key management system (CKMS) refers to the framework and services that provide for the generation, establishment, control, accounting, and destruction of cryptographic keys and associated management information. It includes all elements (hardware, software, other equipment, and documentation); facilities; personnel; procedures; standards; and information products that form the system that establishes, manages, and supports cryptographic products and services for end entities. A CKMS may handle symmetric keys, asymmetric keys or both.

Key management policies, practice statements, and specifications should identify common CKMS elements and suggest functions of and relationships among the organizational elements responsible for the management and use of cryptographic keys. The complexity of a key-management infrastructure and the allocation of roles within a key-management infrastructure will depend on 1) the cryptographic algorithms employed, 2) the operational and communications relationships among the organizational elements being served, 3) the purposes for which cryptography is employed, and 4) the number and complexity of cryptographic keying relationships required by an organization.

The structure, complexity, and scale of CKMSs may vary considerably according to the needs of individual organizations. However, the elements and functions identified in Part 2 need to be present in most organizations that require cryptographic protection. This subsection describes the common CKMS organizational elements, functions, and requirements. Examples of real-world CKMS are provided in Appendix A.

A CKMS is designed to incorporate a set of functional elements that collectively provide unified and seamless protection policy enforcement and key management services. Several distinct functional elements are identified for the generation, establishment, and management of cryptographic keys: a Central Oversight Authority, one or more key processing facility(ies), (optional) service agents, client nodes and (optional) hardware tokens used for.# Entity

Authentication or initializing keys. It should be noted that organizations may choose to combine the functionality of more than one element into a single component. Figure 1 illustrates functional CKMS relationships.

## 2.3.1 Central Oversight Authority

As used in this Recommendation, the CKMS's Central Oversight Authority is the entity that provides overall CKMS data synchronization and system security oversight for an organization or set of organizations. The Central Oversight Authority 1) coordinates protection policy and practices (procedures) documentation, 2) may function as a holder of key management information provided by service agents, and 3) serves as the source for common and system-level information required by service agents (e.g., key information and registration information, directory data, system policy specifications, and system-wide key compromise and revocation information). As required by policies for survivability or continuity of operations, Central Oversight Authority facilities may be replicated at an appropriate remote site to function as a system backup.

## 2.3.2 Key-Processing Facility(ies)

Key-processing facilities are CKMS components that typically provide one or more of the following services:

- Generation and/or distribution of key information;
- Acquisition or generation of public-key certificates (where applicable);
- Backup, archiving, and inventories of key information;
- Maintenance of a database that maps entities to an organization's certificate or key structure;
- Maintenance and distribution of revoked key or certificate reports (see Section 2.6); and
- Generation of audit requests and the processing of audit responses as necessary for the detection of previously undetected compromises and the analysis of compromise events as needed to support recovery from compromises.

Where public key cryptography is employed, the organization operating the key processing facility will generally perform most PKI registration authority, repository, and archive functions. The organization also performs at least some PKI certification authority functions. Actual X.509 public-key certificates may be obtained from a government source (e.g., certification authorities generating identification or encryption certificates) or a commercial external certification authority (usually a commercial infrastructure/CA that supplies/sells X.509 certificates). Commercial external certification authority certificates should be cross-certified by a government root CA.

An organization may use more than one key-processing facility to provide these services (e.g., for inter-organizational interoperation). Key-processing facilities can be added to meet new requirements or deleted when no longer needed, and they may support both public key and symmetric key-establishment techniques. A key-processing facility may be distributed such that intermediary.# Redistribution Facilities

Maintain stores of keying material that exist in physical form (e.g., magnetic media, smart cards) and may also serve as a source for non-cryptographic products and services (e.g., software downloads for CKMS-reliant entities, usage documents, or policy authority). Secret and private keys and secret metadata that are electronically distributed to end entities shall be wrapped (i.e., encrypted and their integrity protected) for the end entity or for intermediary redistribution services before transmission. Public keys and products not requiring confidentiality protection (e.g., non-secret metadata) that are electronically distributed to end entities shall be provided with integrity protection.

Some key-processing facilities may generate and produce human-readable key information and other key-related information that require physical (i.e., manual) distribution. Keys that are manually distributed shall either 1) be cryptographically protected in the same manner as those intended for electronic distribution or 2) receive physical protection and be subject to controlled distribution (e.g., registered mail) between the key processing facility and the end entity. Part 1 provides general guidance for key distribution. Newly deployed key-processing facilities should be designed to support legacy and existing system requirements and to support future network services as they become available.

## 2.3.3 Service Agents

Some key-management infrastructures may be large enough or may support sufficiently complex organizations that it is impractical for the organizations to receive key information directly from a common CKMS key-processing facility. Intermediate distribution or service facilities, called service agents, may be employed to perform the distribution process.

Service agents, when required by the infrastructure, support an organization's CKMS(s) as single points of access for client nodes. When service agents are used, all transactions initiated by client nodes are either processed by a service agent or forwarded to a key-processing facility. When services are required from multiple key-processing facilities, service agents coordinate services among the key-processing facilities to which they are connected. A service agent that supports a major organizational unit or geographic region may either access a central or inter-organizational key-processing facility or employ local, dedicated processing facilities (e.g., commercial external CAs) as required to support survivability, performance, or availability requirements.

Service agents may be employed by human users or sponsors to order key information and services, retrieve key information, and manage keys and public-key certificates. A service agent may provide key information and/or certificates by utilizing specific key-processing facilities for key and/or certificate generation. Service agents may provide registration, directory services, support for data-recovery services (i.e., using key recovery), and access to relevant documentation such as policy.# CURRENT_PAGE_RAW_OCR_TEXT

## Statements and Infrastructure Devices
Service agents may also process requests for keying material, assign and manage CKMS roles and privileges, and provide interactive help-desk services.

## 2.3.4 Client Nodes
Client nodes are interfaces for human users, devices, applications and processes to access key management functions, including the requesting of certificates and keying material. Client nodes may include cryptographic modules, software, and the procedures necessary to provide access to other CKMS components. Client nodes may interact with service agents (when used) or interact directly with key-processing facilities (when service agents are not used) to obtain key management services. Client nodes may interact directly with other client nodes to establish keys (i.e., using key agreement or key transport schemes). Client nodes provide interfaces to end entities for the establishment of keying material, for the generation of requests for keying material, for the receipt and forwarding (as appropriate) of revoked key notifications (RKNs), for the receipt of audit requests, and for the delivery of audit responses.

Client nodes typically initiate requests for keys in order to synchronize new or existing entities with the current key structure and receive wrapped keys for distribution to end entities. A CKMS client node can be a special-purpose device containing a FIPS 140-validated cryptographic module. Actual interactions between a client node and a service agent or a key-processing facility (in the event that a service agent is not used) depend on whether the client node is a device, a functional security application or a computer process.

## 2.3.5 Tokens
Tokens may be used by human users to interface with their systems that include the CKMS's client node. These tokens typically contain information and keys that allow a human user to interact with their systems by authenticating the user's identity to the system and providing keys for protecting communications. Examples of such tokens are the Federal government's Personal Identity Verification (PIV) cards and Common Access Cards (CAC).

## 2.3.6 Public Key Infrastructure Environments
A public key infrastructure (PKI) is the combination of software, public key technologies, and services that enables enterprises to protect the security of their communications and business transactions on networks. A PKI integrates digital certificates, public key cryptography, and certification authorities into a complete enterprise-wide network security architecture. A typical enterprise's PKI encompasses the issuance of digital certificates to individual entities; end-entity enrollment software; integration with certificate directories; tools for managing, replacing, and revoking certificates; and related services and support.

The term public key infrastructure is derived from public key cryptography, the technology on which a PKI is based. Public key cryptography is the technology behind current digital signature techniques. It has unique features that make it extremely useful as a basis for.# Security Functions in Distributed Systems

A brief discussion of PKIs is provided in Section 5.2.3 of SP 800-175B and in SP 800-32. An example of a PKI is included in Appendix A.1.

## 2.3.7 Symmetric Key Environments

Symmetric key cryptography requires the originator and all intended consumers of specific information secured by a symmetric-key algorithm to share a secret key. This is in contrast to asymmetric-key (public key) algorithm that requires only one party participating in a transaction to know a private key and permits the other party or parties to know the corresponding public key.

Symmetric-key algorithms are generally much more computationally efficient than public key algorithms, so a symmetric-key algorithm is most commonly used to protect larger volumes of information such as the confidentiality of data in transit and in storage. Symmetric-key architectures include center-based architectures and key establishment for communicating groups.

While it is possible for pairs of correspondents to employ symmetric-key cryptographic algorithms for wrapping keys they exchange, institutional use of symmetric-key algorithms for key wrapping involves the distribution of keys by a central facility. SP 800-71 provides discussions on symmetric-key architectures: Key Distribution Centers, Key Translation Centers, Multiple-Center Groups and communicating groups (e.g., peer-to-peer communications).

## 2.3.8 Hierarchies and Meshes

Multiple key-processing facilities may be organized so that subscribers from different domains may interact with each other. Two common constructions are hierarchies and meshes.

In a CKMS hierarchy, as shown in Figure 2, multiple layers of key-processing facilities may be used, each with its own service agent(s) and client nodes, if appropriate (not shown in the figure). Each layer (except the top layer) is "dominated" in some way by a higher-level key-processing facility.

In a meshed CKMS architecture, as shown in Figure 3, each key-processing facility may interact with other key-processing facilities in the mesh, but no concept of dominance is implied by the architecture.

## 2.3.9 Centralized vs. Decentralized Infrastructures

A CKMS can be either centralized or decentralized in nature. For a PKI, the public key does not require protection, so decentralized key management can work efficiently for both large-scale and small-scale cases. The management of symmetric keys, particularly for large-scale operations, often employs a centralized structure.

Centralized CKMS key-management structures tend to be more structurally rigid than decentralized key-management structures, but the choice of how to establish keys, store and account for them, maintain an association of keys with the information protected under those keys, and dispose of keys that are no longer needed is a decision to be made by an organization's security.# Management Team

## 1. Key-Management Functions

Part 1 provides specific guidance regarding constraints associated with each key-management function across the life cycle of keying material.

## 2.3.10 Available Automated Key Management Schemes and Protocols

Examples of automated key-management systems include IPsec IKE and Kerberos. S/MIME and TLS also include automated key-management functions. The design of key-management schemes is technically very challenging. The most frequent sources of vulnerabilities that result in an adversary defeating cryptographic mechanisms are vulnerabilities in key management (e.g., a failure to change session keys frequently or at all, protocol weaknesses, insecure storage, or insecure transport).

Some examples of IETF standards and guidelines for cryptographic key management include:

- RFC 4210, Internet X.509 Public Key Infrastructure Certificate Management Protocol (CMP)
- RFC 4535, GSAKMP: Group Secure Association Key Management Protocol
- RFC 4758, Cryptographic Token Key Initialization
- RFC 4962, Guidance for Authentication, Authorization, and Accounting (AAA) Key Management
- RFC 5083, Cryptographic Message Syntax (CMS) Authenticated Enveloped-Data Content Type
- RFC 5272, Certificate Management Over CMS (CMC)
- RFC 5275, CMS Symmetric Key Management and Distribution
- RFC 5652, Cryptographic Message Syntax (CMS)
- RFC 5996, Internet Key Exchange Protocol Version 2 (IKEv2)
- RFC 6030, Portable Symmetric Key Container (PSKC)
- RFC 6031, Cryptographic Message Syntax (CMS) Symmetric Key Package Content Type
- RFC 6063, Dynamic Symmetric Key Provisioning Protocol (DSKPP)
- RFC 6160, Algorithms for Cryptographic Message Syntax (CMS)
- RFC 6402, Certificate Management Over CMS (CMC) Updates

## 2.4 General Design Requirements for CKMS

Regardless of the key-management structure, any CKMS design should describe how it provides cryptographic keys to the entities that will use those keys to protect sensitive information. The CKMS design documentation should specify the use of each key type, where and how keys can be generated, how they can be protected in storage and during delivery, and the types of entities to whom they can be delivered. CKMS design is the subject of SP 800-130, A Framework for Designing Cryptographic Key Management Systems.

SP 800-152 contains requirements for the design, implementation, and procurement of a CKMS for the U.S. Federal Government, but it can be used as a model for other sectors. A key-management system can be designed to provide services for a single individual (e.g., in a personal data-storage system), an organization (e.g., in a secure Virtual Private Network (VPN) for intra-office communications), or a large complex of organizations (e.g., in secure communications for the U.S. Government). A CKMS can be owned or rented. However, regardless of the design or source for the key-management system, the recommendations of Part 1 and SP 800-152 shall be followed.

## 2.5 Trust

Because the compromise of a cryptographic key compromises all of the information and processes protected by that key, it is essential that client nodes be able to trust that.# CURRENT_PAGE_RAW_OCR_TEXT

## keys and/or key components

come from a trusted source, and that their confidentiality (if required) and integrity have been protected both in storage and in transit. In the case of secret keys, the exposure of a key by any member of a communicating group or on any link between any pair in that group compromises all of the information that was shared by the group using that key. As a result, it is important to avoid using a key from an unauthenticated source, to protect all keys and key components in transit, and to protect stored keys for as long as any information protected under those keys requires protection. Cryptographic confidentiality and integrity mechanisms are most commonly used to establish trust anchors that enforce trust policies and practices. A trust anchor is an authoritative entity for which trust is assumed and not derived. For example, in a public key infrastructure (PKI), a trust anchor is an authoritative entity represented by a public key and associated data. "Trust anchor" also refers to the public key of this CA.

## 2.6 Revocation and Suspension

Section 8.3.5 of Part 1 discusses the revocation of cryptographic keys. Symmetric keys are often revoked by the use of Compromised Key Lists (CKLs). Certificate Revocation Lists (CRLs) are commonly used to revoke public key certificates, thus revoking the private key corresponding to the public key in the certificate. Regardless of whether symmetric or asymmetric keys are used, a means of revoking keys is required. This Recommendation will use the term revoked key notification (RKN) to refer to a mechanism to revoke keys. An RKN may include the revocation reason and an indication of when the revocation was requested. The inclusion of the revocation reason can be useful in risk decisions regarding the information that was received or stored using those keys.

A key may also be suspended from use for a variety of reasons, such as an unknown status of the key or due to the key owner being temporarily unavailable (e.g., the key owner is on extended leave). In the case of a certificate suspension, the intent is to suspend the use of the public key included in the certificate (e.g., to not verify digital signatures or establish keys while the use of the certificate is suspended). This may be communicated to relying parties as an "on hold" revocation reason code in a CRL and in an Online Certificate Status Protocol (OCSP) response. The certificate may later be revoked (e.g., a compromise of the private key corresponding to the public key in the certificate was confirmed) or the certificate may be reactivated (e.g., the key has not been compromised or the owner returned to work). Section 7.3.5 of Part 1 discusses the suspended state for a key.

## 3 Key Management Planning

### 3.1 Background

Federal government organizations are required by statutory and administrative rules and guidelines to protect the confidentiality and integrity of their sensitive information and# Processes

Federal agencies are required to determine a FIPS 200 impact level (i.e., Low, Moderate or High) based on the security categories defined in FIPS 199. The security categories are based on the potential impact on an organization if certain events occur that jeopardize the information and information systems needed by the organization to accomplish its assigned mission, protect its assets, fulfill its legal responsibilities, maintain its day-to-day functions, and protect individuals.

An organization also needs to define its security objectives for storing and/or communicating its sensitive information. These objectives may include the following:

- Providing confidentiality for stored and/or transmitted data,
- Source authentication for received data,
- Integrity protection for stored/transmitted data,
- Entity authentication, etc.

If cryptography is used to satisfy the requirement to protect an organization's sensitive information and processes, developers, integrators, and managers need to ensure that each cryptographic implementation satisfies all system security, compatibility, and interoperability requirements that are associated with the system into which it is being integrated.

Program managers who oversee the implementation of cryptography in federal systems are responsible for ensuring that the systems include all mechanisms, interfaces, policies, and procedures that are necessary to generate or otherwise establish, acquire, distribute, replace, account for, and protect key information that is required for system cryptographic operations in accordance with the recommendations presented in Part 1 and the policies and practices identified in this Part 2 document (SP 800-57).

The development of new cryptographic systems, including CKMS, should ideally be conducted following the processes described in SP 800-160. However, in many cases, systems that rely on cryptographic protection are already being used. Where such systems are being augmented or otherwise modified, security planning is still required, but the SP 800-160 processes will need to be abridged or otherwise adapted because of legacy constraints. Federal government organizations must still select SP 800-53 security controls based on system design, operational characteristics, and FIPS 199 impact levels.

## 3.1.1 Select SP 800-53 Controls

Given both the impact levels for an organization's sensitive information that needs to be protected using cryptography and the organization's security objectives (see Section 3.1), SP 800-53 security controls should be reviewed for applicability to the system, and either the use of applicable controls must be verified, or compensating controls that obviate the use of specific SP 800-53 controls must be documented. Note that the SP 800-53 security controls are described at a high level in many cases, and they may need to be interpreted or tailored to system characteristics and operational conditions.

## 3.1.2 IT System Examination# CURRENT_PAGE_RAW_OCR_TEXT

Most organizations have their sensitive information in an electronic form, and some of that information may be available online. The environment of the system on which the information resides needs to be examined to identify any CKMS components and cryptographic products that are available to provide the required cryptographic protections to that information (e.g., cryptographic applications and modules).

In all cases, any cryptographic functions shall be performed using FIPS 140-validated cryptographic modules. If any required functionality is not available, the shortfall needs to be identified.

## 3.2 Key Management Planning

Using the information from Section 3.1, determine how to integrate key management. Key management is often an afterthought in the cryptographic development process (i.e., when incorporating cryptographic processes into applications and systems). As a result, cryptographic subsystems often fail to support the key management functionality and protocols that are necessary to provide adequate security. Recognition of these shortcomings often results in modifications that may impact operational efficiency more than would have been the case if key management planning began during the initial development of the system or application.

All cryptographic development activities should involve key management planning and development of specifications by entities designated as responsible for the secure implementation of cryptography into an information system. Key management planning should begin during the initial conceptual/development stages of the cryptographic development lifecycle or during the initial discussion stages for the application of existing cryptographic mechanisms into information systems and networks. The specifications that result from the planning activities shall be consistent with NIST key management guidance (see Part 1 and SP 800-152).

All cryptographic purchasing plans, development activities, and application integration plans should involve key management planning. In the case of planning for the acquisition and use of existing cryptographic devices or software, key management planning should begin during the initial discussion stages for cryptographic applications or implementation efforts. The planning should be evolutionary in nature, changing as the cryptographic application and requirements change, and should be consistent with NIST key management guidance.

Key Management Plans should ensure that the key management products and services that are proposed for the cryptographic device, application or process are provided with adequate security, and are supportable and operationally suitable in accordance with the FIPS 140 security policy for any associated cryptographic module.

For the application of existing cryptographic products for which a Key Management Plan already exists, the existing plan should be reviewed in the context of the application's environment, and# Key Management Planning Process

Organizational Key Management Plans document the capabilities that cryptographic applications require from the organization's CKMS(s) and are often incorporated as appendices in system security plans. The purpose of these Key Management Plans is to ensure that any lifecycle key management services are supportable by and available from the CKMS in a secure and timely manner. The planning process must account for both the availability of critical resources and for assurance requirements implied by the organization's critical mission functions.

## Key Management Planning Steps

Key management planning involves the following steps:

1. An appropriate key management architecture is selected based on the available cryptographic mechanisms (see Section 3.1.2) and objectives (see Section 3.1). Section 2.3 provides examples of architectures to be considered.

2. A Key Management Specification is developed for each cryptographic product to be used in the system (see Section 4). When developing a Key Management Specification for a cryptographic product, the unique key management products and services needed from the CKMS to support the operation of the cryptographic product must be defined. The specification of cryptographic mechanisms, including key management functions, shall consider the organization's resource limitations and procedural environment. For example, an organization that lacks physical protection facilities, adequate vetting of support personnel, and the procedures and resources required for managing controlled unclassified information might find it difficult to satisfy the policies and procedures required for cryptography that are generally required for the protection of controlled unclassified information. Before either approving or rejecting specifications required for controlled unclassified information, the organization should consider the resource and operational implications of the decision.

A contrasting example is that of an organization that must exchange information that is assigned a Moderate or High FIPS 199 impact level; Moderate and High impact levels require a cryptographic module validated at FIPS 140 Level 3 or higher. Specifying a FIPS 140 Level 1 cryptographic module could adversely affect the organization's ability to continue to engage in mission-critical processing and communications partnerships.

If a Key Management Plan already exists for an organization, the Key Management Specification needs to be in conformance with the CKMS Security Policy (see Section 5). The CKMS Practice Statement should support both the CKMS Security Policy and the Key Management Specification.

3. Based on the Key Management Plan, a CKMS Security Policy (CKMS SP) is developed that documents the decisions made in developing the Key Management Plan. A CKMS SP is a set of rules that are established to describe the goals, responsibilities,# Key Management Overview

and overall requirements for the management of cryptographic keying material throughout the entire key lifecycle (see Section 5).

## 4. CKMS Operation

A CKMS may be operated by the organization owning the information to be protected, or may be operated by another organization (e.g., under contract). The organization operating the CKMS develops a CKMS Practice Statement (CKMS PS). A CKMS PS specifies how key management procedures and techniques are used to enforce the CKMS Security Policy (CKMS SP).

### 3.2.2 Key Management Planning Information Requirements

The level of key management planning detail required for cryptographic applications can be tailored, depending upon the scope and complexity of the application. If an organization's cryptographic support requirements are limited, for example, to e-mail security for a small number of employees, extensive planning documentation is neither feasible nor cost-effective (unless such security documentation is justified by a very high level of sensitivity associated with the organization's application). On the other hand, cryptographic security for a collection of networks that support thousands, or tens of thousands of users require the kind of extensive documentation described in Section 3.2.1 and in Appendix B. Regardless of the size and complexity of a cryptographic application, documentation of some basic key management characteristics and requirements is strongly recommended. Some basic information that needs to be documented for all applications is provided in the following subsections.

#### 3.2.2.1 Key Management Products and Services Requirements

The key management planning documentation should describe the keying material requirements for the key management products and services to be provided: the types, quantities, cryptoperiod (lifetime), algorithms, metadata types and any other additional information needed (e.g., domain parameters). If additional keys, certificates or tokens are required, the key management planning documentation should describe a rough order of magnitude for the quantities required. If the keys or certificates already issued (or planned to be issued) by the CKMS are adequate for the device, application or process described in the Key Management Specification, then the Key Management Specification should so state. Otherwise, any new or additional key, certificate, or token features (e.g., new certificate extensions or formats) should be described.

The requirement information for key management products and services may be included in table format. The following information should be included in the key management planning documentation:

- The types of key management products and services;
- The quantity of key management products required for the services to be provided (e.g., the number of keys to be issued per device, application or process to be keyed);
- The algorithm(s) employed for each key management product used and service provided.```markdown
# CURRENT_PAGE_RAW_OCR_TEXT

by a device, application or process;

- The key information format(s) (reference existing specifications, if applicable);
- The cryptoperiods to be enforced (may be a general recommendation or a recommendation specific to a service, key type, device, application, process or organization);
- PKI certificate classes (as applicable);
- Tokens or software modules to be used (as applicable);
- Dates when keying material is needed (plans for the distribution of the initial keys and the frequency of replacement of the keys);
- Provision for review or revision of replacement plans when the circumstances underlying replacement frequency change;
- The projected duration of the need (for devices, applications, processes or organizations); and
- The title or identity of the anticipated keying material manager (as applicable).

The format for the description of the key management products and services generally references an existing key specification. If the format of the key information is not already specified elsewhere, then the format and medium should be specified in the key management planning documentation.

## 3.2.2.2 Changes to Key Management Product Requirements and Transition Planning

Over time, the cryptanalytic capabilities and processing power available for performing cryptanalysis will eventually overtake the protection afforded by the implemented cryptographic algorithms. Most often, the cryptanalytic advances require a transition from a key size currently in use to a larger key size, but they can also result in the need to move from one algorithm to another. Examples include past requirements to transition from DES, Triple DES and SHA-1 to stronger algorithms, and the postulated need to transition from logarithmic and elliptic curve algorithms (e.g., RSA, Diffie Hellman and ECDSA) to algorithms more resistant to quantum computing. Regardless of the basis for transition and whether the transition involves a larger key size or a new algorithm, it is important to begin planning for transition as soon as possible after becoming aware of the need. Changes to either algorithm or key size most often require changes to the code and protocols, not just to configuration settings for the current code and protocols. Frequently, firmware or hardware changes are required. This always takes longer and is more complicated than expected. The transition period is usually measured in decades; during the period between the advent of a practical cryptographic attack and the completion of a transition, all information protected by the vulnerable cryptography is subject to disclosure, alteration, or both.

## 3.2.2.3 Key Management Products and Services Ordering

For keys distributed from a CA or other key processing center rather than keys established at client nodes using automated key establishment techniques, a description of the procedures for ordering keying material within a specified CKMS is required. Details should be included that are sufficient.
```# Key Management Planning Documentation

## 3.2.2.4 Keying Material Distribution
For keys distributed from a CA or other key processing center rather than keys established at client nodes using automated key establishment techniques, key management planning documentation should describe the distribution method. The distribution information will normally include how the key management products are distributed (e.g., by courier or using key transport protocols), how they are protected during distribution (e.g., key wrapping) and how they are distributed (e.g., by courier or using key transport protocols), the physical form of the product (e.g., electronic, PROM, disk, paper, etc.) and how they are identified during the distribution process.

## 3.2.2.5 Keying Material Storage
Key management planning documentation should address key information storage (e.g., the media used and the storage location, if appropriate) and the method for identifying the information during its storage life (e.g., by key name and date). The storage capacity capabilities for the key management products should be included.

## 3.2.2.6 Access Control
Key management planning documentation should address how access to the cryptographic application will be authorized, controlled, and validated for the request, generation, handling, establishment, storage, and/or use of key management products and services. Any use of authentication mechanisms such as passwords, tokens, personal identification numbers (PINs), or biometrics shall be included (with their expiration dates, where applicable). For PKI cryptographic applications, access privileges based on roles and the use of tokens shall be described.

## 3.2.2.7 Accounting for Keys and Certificates
Key management planning documentation must include a description of the accounting methods used for the keys and certificates employed by the cryptographic application (i.e., the use of an inventory and audit logs). When using cryptographic functions that employ keys, it is imperative to maintain a record of all long-term keys in use. Inventory management is concerned with establishing and maintaining records of the keys and/or certificates in use; assigning and tracking their owners or sponsors (who/what are responsible for the keys and where they are located or how to contact them); monitoring key and certificate status (e.g., expiration dates and whether compromised), and reporting the status to the appropriate official for remedial action, when required (e.g., to replace the key and/or certificate). The use of logs to support tracking the use of key management products and services, (including the generation/establishment, storage, use and/or destruction of key information) should be described. The use of appropriate access privileges to support the control of key management products and services used by the cryptographic device, application or process should also be included.# CURRENT_PAGE_RAW_OCR_TEXT

## Compromise Management and Recovery

Procedures for the restoration of protected communications and stored information content in the event of the compromise of a key should be described. The recovery process description should include the methods for re-keying (i.e., replacing the key and/or certificate). The methods for revoking keys should be described in detail, including the methods for issuing new certificates with new keys.

## Key Recovery

Key information that is in active memory or stored in normal operational storage may sometimes be lost or corrupted (e.g., from a system crash or power fluctuation); cryptographic keys used to protect archived data may be required when accessing that data (e.g., to decrypt the data). Key recovery is used to obtain currently unavailable key information by an authorized human entity. Key recovery may be possible if the key information has been backed up or archived. Key information may be recovered from backups during the key's cryptoperiod or from archives if the information has been archived; archived keys need to be retained as long as the archived information needs to be retained.

Sections 8.2.2.1 and 8.3.1 of Part 1 list key types that may be suitable for backing up or archiving, respectively. Issues associated with key recovery and discussions about whether or not different types of cryptographic keying material need to be recoverable are provided in Appendix B of Part 1. The recovery and permissible use of a recovered key is discussed in Section 5.3.4 of Part 1 and depends on the key type, assigned use, its cryptoperiod and whether it has been compromised.

An assessment needs to be made regarding which key information needs to be preserved for possible recovery at a later time. The decision employing a key recovery capability should be made on a case-by-case basis. The factors involved in a decision for or against key recovery should be carefully assessed. The trade-offs are concerned with continuity of operations versus the risk of possibly exposing the key and the information it protects if control of the key is lost.

A key recovery process description should include a discussion of the generation, storage, and access of the long-term storage keys used for the protection of backed-up and archived key information. The process of transitioning from the current to future long-term storage keys should also be addressed.```markdown
# CURRENT_PAGE_RAW_OCR_TEXT

## 3.2.2.10 CKMS Enhancement (optional)

The use of FIPS-140-validated cryptographic modules to perform cryptographic functions is required for federal agencies and highly encouraged for others. Such use may reduce some of the documentation requirements and facilitate both system integration and logistics support. It also encourages the feedback of locally specific requirements to the CKMS planning process. However, requirements may be identified that are currently not supported by the appropriate CKMS. If applicable, it would be useful to identify and address required improvements to the CKMS in order to achieve the needed functionality. This will assist in identifying requirements for current and/or planned capability increments for the CKMS. Even if a device, application or process can be fully supported by the current or planned CKMS, improvements to the CKMS should also be identified if they improve functionality or reduce workload without sacrificing security. The identified requirements can be analyzed for potential upgrades to the CKMS, based on available cost, schedule, and performance constraints.

## 4 Key Management Specification

A Key Management Specification is the document that describes the key management products that may be required to operate a cryptographic device or application. Where applicable, the Key Management Specification also describes key-management components that are provided by a cryptographic device. The Key Management Specification documents the capabilities that the cryptographic application requires from key sources (e.g., the CKMS). Examples are described in Appendix A to this Recommendation. Key Management Specifications are generally produced by developers or (where developers have failed to provide adequate capabilities) by integrators. Organizations shall select cryptographic devices and applications with cryptographic functions, key management products and key management services that conform to NIST standards to the maximum extent possible, and new cryptographic application development efforts shall comply with NIST key management recommendations. Accordingly, NIST criteria for the security, accuracy, and utility of key management products in electronic and physical forms shall be met (e.g., see FIPS 140, SP 800-53, and Part 1). The methods used in the design, evaluation, programming, generation, production, establishment, quality assurance, and inspection procedures for key management products and services should be structured to satisfy such criteria.

For cryptographic development efforts, a Cryptographic Key Management Specification and acquisition planning process should begin as soon as the candidate algorithm(s) and, if appropriate, keying material media and format have been identified. Key management considerations may affect algorithm choice, due to operational efficiency.
```# Considerations for the Anticipated Applications

When using existing cryptographic mechanisms to provide a cryptographic service for which no Key Management Specification exists, the planning and specification processes should begin during device and source selection, and continue through acquisition and installation.

Where the criteria for current or anticipated security, accuracy, and utility can be satisfied with any of the organization's existing suite of key management products and services, one of those products and services should be considered. Where the application of current key management products and services results in reduced security, accuracy, utility, or added cost to a cryptographic application, then an organization may initiate efforts to develop and implement other key management product and service types, variations, and, as necessary, production processes. However, such efforts should conform as closely as possible to NIST's established key management recommendations.

Processes for purchasing cryptographic products and services should include plans and provisions for the acquisition of keying material from trusted sources, secure paths for the transport of keying material, and/or FIPS 140-compliant automated key establishment mechanisms (see SP 800-56A, SP 800-56B and SP 800-71). Key management requirements shall be included in service agreements or contracts associated with cryptographically protected services.

For any cryptographic device or application employed by the federal government, there should be a specification of the keying material that the device or application requires, an identification of whether the keying material is internally or externally generated, a specification of keying material input/output interfaces, and a description of interfaces to any required validation process. Development of the specification should be initiated before any cryptographic procurement is initiated. Algorithms, key lengths, cryptoperiods, key sources, input/output interfaces (where applicable) and keying material access and handling requirements should also be specified. For devices using cryptographic modules that are validated under FIPS 140, most of these requirements are specified in the security policy posted with the validation information for each module. Note that all cryptographic modules used by federal agencies shall be validated in accordance with FIPS 140.

These specifications are required by system developers as well as by the managers of systems into which cryptographic mechanisms are integrated. They are also required by program managers who are responsible for the security of system implementations.

The types of key management components that are required for a specific cryptographic device or application and/or for suites of devices or applications used by organizations shall be conformant to NIST standards and guidelines, and new cryptographic device-# Development Efforts

Development efforts shall comply with NIST key-management recommendations. Accordingly, NIST criteria for the security, accuracy, and use of key management products in electronic and physical forms shall be met. Where the criteria for security, accuracy, and usability can be satisfied with standard key management components (e.g., PKI for public key systems), the use of those compliant components is encouraged. Appendix C is a checklist that may be used to guide Key Management Specification activities.

## 4.1 Key Management Specification Content

The level of detail required for each element of a Key Management Specification can be tailored, depending upon the environment and complexity of the device or application for which a Key Management Specification is being written. A Key Management Specification shall contain a title page that includes the device identifier or application type, and the developer's or integrator's identifier. Unless the information is tightly controlled, a Key Management Specification should not contain proprietary or sensitive information.

## 4.2 Cryptographic Application

A description of the cryptographic application will provide a basis for the development of the rest of a Key Management Specification. Cryptographic application coverage should consist of a brief description of the cryptographic application or device. This includes the purpose or use of the cryptographic application or device, and whether it is a new cryptographic application or device, a modification of an existing cryptographic application or device, or an existing cryptographic application or device for which no Key Management Specification currently exists. A brief description of the cryptographic services that the cryptographic application or device provides should be included. Information concerning long-term and potential interim key management support for the cryptographic application or device should be provided. Cryptographic applications may employ symmetric key cryptography, public key cryptography, or both. Examples of symmetric key cryptographic applications include full disk encryption for confidentiality, and the use of message authentication codes for integrity protection. Examples of public key cryptographic applications include 1) integrity protection for electronic mail, internet address information, and internet routing information using digital signatures and 2) asymmetric key transport to protect the confidentiality of symmetric keys in transit (encrypting the symmetric keys using a public key). Examples of applications that use both symmetric and asymmetric cryptography are Transport Layer Security (TLS) (using encryption to protect the transfer of data and information) and the encryption of electronic mail (e.g., SMIMEA), where symmetric key cryptography is used to protect the confidentiality of the information, and public key cryptography is used to protect the confidentiality of the symmetric keys.

## 4.3 Communications Environment# Key Management Specification

The Key Management Specification shall provide a brief description of the communications environment in which the cryptographic device or application is designed to operate. Some examples of communications environments include:

1. Data networks (e.g., intranet, Internet, VPN);
2. Wired communications (e.g., landline, dedicated or shared switching resources); and
3. Wireless communications (e.g., cell phones).

The environment description shall include any anticipated access controls on communications resources, data sensitivity, privacy issues, etc.

## 4.4 Key Management Metadata Requirements

A key's metadata is the information associated with a particular key that is used by a CKMS to manage the key. SP 800-152 states that the system designer should select the metadata that is appropriate for a trusted association with a key based upon a number of factors, including the key type, the key lifecycle states, and the security policy of the CKMS. The metadata elements cited in SP 800-152 specify a key's important characteristics, its acceptable uses, and other information that is related to the key. Metadata elements relevant to the management and use of a key must be correctly associated with a key and consulted whenever a key is stored, retrieved, loaded into a cryptographic module, used to protect data (e.g., including other keys), exchanged with peer entities authorized to use the key, and when assuring that a key is correctly protected.

For example, asymmetric cryptographic applications using public-key certificates (e.g., X.509 certificates) should describe the types of certificates in the metadata. Some examples of metadata elements from Section 6.2.1 of SP 800-152 include:

1. The different keying material classes or types required, supported, and/or generated (e.g., for PKI: signature keys, key establishment keys, and authentication keys; for symmetric keys: key wrapping keys, key derivation keys and data encryption keys);
2. The key management algorithm(s) (the applicable approved algorithms, e.g., FF DH and/or RSA);
3. The keying material format(s) (reference any existing key specification, if known);
4. The set of acceptable certificate policies (if applicable); and
5. Any tokens to be used for entity authentication (i.e., for access authorization or key entry).

The description of the keying material format (item 3 above) may reference a key specification for an existing cryptographic device. If the format of the keying material is not already specified, then the format and medium should be specified in any Key Management Specification. See Section 6.2.1 of SP 800-152 for a list of metadata elements to be considered for a CKMS.

## 4.5 Keying Material Generation

A Key Management Specification should include a description of the requirements for the establishment of keying material for the cryptographic device or application for which the Key Management Specification is written. If the cryptographic device or application does not provide key establishment capabilities, an identification of the keying material and...```markdown
# CURRENT_PAGE_RAW_OCR_TEXT

## source or method that
will be required from external sources should be provided.

### 4.6 Keying Material Distribution
When a device or application supports the automated establishment of keying material, a Key Management Specification should include a description of the distribution method(s) employed for the initial keying material used by the device or application. The distribution plan may describe how the keying material is distributed (e.g., manual, key loader device, etc.) and the form used (plaintext, wrapped, as key components with dual control and split knowledge required, etc.) In the case of a dependence on manual distribution, the dependence and any handling assumptions regarding keying material should be stated.

### 4.7 Key Information Storage
A Key Management Specification should address how the cryptographic device or application for which the Key Management Specification is being written stores and protects key information including how long it is to be stored. The integrity of all key information shall be protected; the confidentiality of secret and private keys and secret metadata shall be protected. When stored outside a cryptographic module, the method of protection depends on the impact level associated with the data protected by a key (see SP 800-152, Sections 6.1.2 and 6.2.1):
- For High and Moderate impact-level data, the confidentiality and integrity of the key information shall be cryptographically protected.
- For Low impact-level data, the confidentiality and integrity of the key information should be cryptographically protected.

When cryptographic protection is used, the security strength of the protection shall be selected in accordance with the impact level associated with the data protected by the key (see Section 2.2 of SP 800-152). The generation and management of the storage-protection keys shall be described, including the process of transitioning from the current to future storage keys. A Key Management Specification should also indicate how the key information is identified during its storage life (e.g., using a Distinguished Name or key identifier). The storage capacity requirements for storing the key information should be included.

### 4.8 Access Control
A Key Management Specification should address how access to the cryptographic devices or applications are to be authorized, controlled, and validated to request, generate, handle, distribute, store, use and/or destroy keying material. Any use of authenticators, such as passwords, personal identification numbers (PINs) and hardware tokens, should be included. For example, in PKI cryptographic applications, role and identity-based authentication and authorization, and the use of any tokens should be described.

### 4.9 Accounting and Auditing
When using cryptographic mechanisms employing keys, it is imperative to keep track of all non-ephemeral keys authorized for use by their owner entities (e.g., in a key or certificate inventory and in audit logs). In the case of symmetric keys, this includes the keys used for interaction.
```# Key Management Specification

between entities within an organization and the keys used between organizational entities and entities external to the organization. For asymmetric key pairs, this includes key pairs owned by organizational entities -- those entities authorized to use the private key of the key pair and any certificates containing the public key of each key pair.

Any Key Management Specification should describe any device or application support for the accounting of keying material and any support for or outputs to logs used to support the tracking of keying material generation, distribution, storage, use and/or destruction. The use of appropriate authorization mechanisms to support the control of keying material that is used by the cryptographic application should also be described. All Key Management Specifications shall identify where human and automated keying material inventory management and audit logging are required and, if applicable, where multiple parties are required to perform some operation.

A list of key types is provided in Section 5.1.1 of SP 800-57, Part 1. Examples of metadata elements to consider for association with keys are listed in SP 800-152 and Section 6.2.3 of Part 1. Metadata elements may be explicitly recorded with each key or certificate, may be explicitly recorded for groups of keys or certificates, may be implicitly known or a combination thereof. A long-term key shall be inventoried along with any information associated with it (e.g., domain parameters and metadata).

The generation, distribution, storage, use and/or destruction of all keys shall be logged. Some particularly important metadata elements that need to be associated with inventoried keys and certificates are the following. Note that in the case of certificates, some of the information may be available in the certificate itself.

## Common Elements

1. Common elements that shall be specified as required by all Key Management Specifications include:
- Type of key -- e.g., private signature key, symmetric data encryption key
- Key format -- e.g., TLS/SSL server certificate, TLS/SSL client certificate, code signing certificate, email certificate, ASN.1, and Tag-Length-Value (TLV) encoding for symmetric keys
- Key length -- e.g., 2048 bits, 256 bits
- Algorithm with which the key is used -- e.g., AES, ECDSA, RSA
- Schemes or modes of operation -- e.g., digital signatures, DH, GCM, etc.
- Key source:
- A description of where the key was generated and by what/whom
- How the key was generated and distributed (e.g., using a DH key agreement scheme, generated by an RBG and transported using RSA OAEP)
- The identifier of any keys used during the generation or distribution process (e.g., pointers to other keys in the inventory or database)
- Key owner(s)/authorized users/subject name:
- Entity identifier(s)
- Contact information for the owner or entity sponsor (e.g., email, phone)
- Application type(s) for the use of the key -- e.g., email, file encryption, code signing
- Installed location information (as appropriate)
- Address
- Type of device on which it is installed# Key Management Specifications

## 1. Location on Device
- Location on device (e.g., ID, file path, account, etc.)
- Status -- e.g., OK to use, compromised (with date), revoked (with date and reason), suspended (with start date and projected suspension end date), destroyed (with date), etc.

## 2. Common Elements
Common elements that should be specified as required by all Key Management Specifications include:
- Key identifier
- Business application name/id
- Applicable regulations and policies
- Authorities responsible for approving systems using cryptography for activation and operation.
- Storage protection when outside a cryptographic module:
- The algorithm(s) used to protect the integrity of the keying material and metadata and a pointer to the keying material used for the integrity protection
- If the key type is a secret or private key, the algorithm used to wrap the key and a pointer to the keying material used for key wrapping

## 3. Required Elements for Symmetric Key Systems
Elements that should be included as being required for symmetric key systems:
- Cryptoperiods -- by date or by usage:
- By date -- start and end dates for the originator-usage period and recipient-usage period
- By usage -- current count and the usage-count limit for the originator-usage period

## 4. Required Metadata for Asymmetric Keys and PKI Certificates
In the case of systems using asymmetric keys and PKI certificates (e.g., Transport Layer Security certificates), the following metadata elements shall be specified by all Key Management Specifications as being required:
- Certificate issuer -- e.g., Issuer distinguished name
- Signature algorithm used to sign the certificate
- Subject type -- indicating whether the certificate is for a CA or end entity
- Cryptoperiod -- start and end dates
- The corresponding key -- a pointer to the corresponding key

Also, in the case of asymmetric systems using PKI certificates (e.g., Transport Layer Security certificates), the following elements should be specified in Key Management Specifications as being required:
- Certificate serial number
- Authority Key Identifier
- Certificate Extensions
- Certificate validity period -- start and expiration dates

## 5. Required Information for Other Applications of Public Key Cryptography
In some other applications of public key cryptography (e.g., SSH), the following information shall be specified in Key Management Specifications as being required:
- Key subtype -- e.g., Host private key, known host key, user private key, authorized key
- Account (to which the key is associated)
- Authorized key options (e.g., cert-authority, no-agent-forwarding, no-pty)

## 6. Recovery from Compromise, Corruption, or Loss of Keying Material
A Key Management Specification should address any support for the restoration of protected communications in the event of the compromise, corruption, or loss of the keying material used by the cryptographic device or application. The recovery process description should include the methods for replacing keys and/or certificates with new keys. The methods for...# Revocation and Compromise Notification

Revocation and compromise notification (e.g., using RKNs) should be provided (e.g., the details for using Certificate Revocation Lists (CRLs) and Compromised Key Lists (CKLs)). When PKI certificates are used, a description of how certificates will be reissued with new public keys and replaced within the cryptographic application should also be included. General compromise-recovery guidance is provided in Section 9.3.4 of Part 1.

## 4.11 Key Recovery

Any Key Management Specification should include a description of product support or system functions for effecting key recovery. Key recovery addresses how unavailable keys can be recovered (e.g., encryption keys) from key backups or archives.

In the key-recovery process description, system developers should include a discussion of the generation, storage, and access to any keys used to protect the integrity or confidentiality of key information. Stored keys are expected to be protected as discussed in Section 5.7. General contingency planning guidance is provided in Section 9.3 of Part 1. Key recovery is discussed in Appendix B of Part 1.

# 5 CKMS Security Policy

An organization often creates and supports layered security policies, with high-level policies addressing the management of its information and lower-level policies specifying the rules for protecting the information.

- An organization's Information Management Policy governs the collection, processing, and use of an organization's information and should specify, at a high level, what information is to be collected or created, and how it is to be managed.
- The organization's Information Security Policy is created to support and enforce portions of the organization's Information Management Policy by specifying in more detail what information is to be protected from anticipated threats and how that protection is to be attained. A Federal organization may have different Information Security Policies covering different applications of categories of information.

A CKMS Security Policy (SP) is a high-level document that describes the authorization and protection objectives and constraints that apply to the generation, establishment, accounting, storage, use, and destruction of cryptographic keying material. It is intended to support an Information Security Policy by protecting the cryptographic keys and metadata used by a CKMS and to enforce restrictions associated with their use. A CKMS SP includes an identification of all cryptographic mechanisms and cryptographic protocols that can be used by the CKMS. A CKMS SP also includes a set of rules that are established to describe the goals, responsibilities, and overall requirements for the management of cryptographic keying material throughout the entire key lifecycle, including when they are operational, stored, transported, and used. As stated in SP 800-152, a CKMS SP should include the following:# CKMS Security Policy

a) The names of the organization(s) adopting the policy;
b) Who (person, title or role) is authorized to approve/modify the policy;
c) The impact-levels of the information that is specified in and controlled by the policy;
d) The primary data and key/metadata protection services (i.e., data confidentiality, data integrity, source authentication) that are to be provided by the CKMS;
e) The security services (e.g., personal accountability, personal privacy, availability, anonymity, unlinkability, unobservability) that can be supported by the CKMS;
f) Sensitivity and handling restrictions for keys and associated metadata;
g) The algorithms and all associated parameters to be used for each impact-level and with each protection service;
h) The expected maximum lifetime of keys and metadata for each cryptographic algorithm used;
i) The acceptable methods of user/role and source authentication for each information impact-level to be protected by a key and its associated metadata;
j) The backup, archiving and recovery requirements for keys and metadata at each information impact-level;
k) The roles to be supported by the CKMS;
l) The access control and physical security requirements for the CKMS's keys and metadata for each impact-level;
m) The means and rules for recovering keys and metadata; and
n) The communication protocols to be used when protecting sensitive data, keys, and metadata.

CKMS SPs are implemented through a combination of security mechanisms and procedures. An organization uses security mechanisms (e.g., safes, alarms, random number generators, encryption algorithms, signature, and authentication algorithms) as tools to implement a policy. However, key-management components will produce the desired results only if they are properly configured and maintained.

CKMS Security Policy statements are supported by CKMS Practice Statements (PS) that document the procedures that system administrators and users follow when establishing and maintaining key-management components using the CKMS. CKMS Practice Statement requirements are described in Section 6 below. The procedures documented in the CKMS Practice Statement describe how the security requirements in the CKMS SP are met and are directly linked to the key-management components employed by an organization (see PKI 01).

U.S. Government agencies that use cryptography are responsible for defining the CKMS SP that governs the lifecycle for the cryptographic keys as specified in Section 6.3 of SP 800-152 and in Part 1, Sections 7 and 8. A CKMS Practice Statement is then developed, based on the CKMS SP and the actual applications supported.

Policy documentation requirements associated with small scale or single-system cryptographic applications will obviously not be as elaborate as those required for large and diverse government agencies that are supported by several information technology systems. However, any organization that employs cryptography to provide security services is likely to require some level of policy, practices and planning documentation.# 5.1 Policy Content

The policy document or documents that comprise the CKMS SP include high-level key management structure and responsibilities, governing standards and guidelines, organizational dependencies and other relationships, and security objectives.

Most currently available guidance for CKMS SP development is focused primarily on the use of asymmetric algorithms and X.509 certificate-based key establishment and transport in a public key infrastructure (PKI) environment. In that environment, the CKMS SP is usually a stand-alone document known as a Certificate Policy (CP). Certificate issuance organizations also publish CPs. Although some interpretation is required, most of the guidance herein applies to symmetric-key environments as well.

The scope of a CKMS SP may be limited to the management of certificates for a single PKI certification authority (CA) and its supporting components, or to a symmetric-key environment between peer entities or between subscribers and a key center in a single key-center environment. Alternatively, the scope of a CKMS SP may include certificate management in a hierarchical PKI, a meshed PKI, or multiple-center symmetric-key environments (see Section 2.3). Note that multiple CAs or symmetric-key environments may operate under a single CKMS SP.

The CKMS SP is used for several different purposes. The CKMS SP is used to guide the development of CKMS Practice Statements for each CA or symmetric key center or multiple-center group that operates under its provisions. CA managers from the PKIs of other organizations' PKIs may review the CKMS SP/CP before cross-certification, and managers of symmetric-key CKMS may review the CKMS SP before joining new or existing multiple-center groups. Auditors and accreditors will use the CKMS SP as the basis for their reviews of CA and/or symmetric-key CKMS operations. Application owners that are considering a PKI certificate source should review a CKMS SP/CP to determine whether its certificates are appropriate for their applications.

## 5.1.1 General Policy Content Requirements

Although detailed formats are specified for some environments (e.g., see Appendix A for a PKI CP format), the policy documents into which key-management information is inserted may vary from organization to organization. In general, the information should appear in top-level organizational information systems policies and practices documents. The policy need not always be elaborate. A degree of flexibility may be desirable with respect to actual organizational assignments and operations procedures in order to accommodate organizational and information infrastructure changes over time. However, the CKMS SP needs to establish a policy foundation for the full set of key management functions.

## 5.1.2 Security Objectives

A CKMS SP should state the security objectives that are applicable to and expected to be supported by the CKMS. The security objectives should include the identification of:# CURRENT_PAGE_RAW_OCR_TEXT

## (a)
The nature of the information to be protected (e.g., financial transactions, privacy-sensitive information, critical process data);

## (b)
The classes of threats against which protection is required (e.g., the unauthorized modification of data, the replay of communications, the fraudulent repudiation of transactions, the disclosure of information to unauthorized parties);

## (c)
The FIPS 199 impact level that is determined by the consequences of a compromise of the protected information and/or processes (including the sensitivity and perishability of the information);

## (d)
The cryptographic protection mechanisms to be employed (e.g., message authentication codes, digital signatures, encryption);

## (e)
The protection requirements for cryptographic processes and keying material (e.g., tamper-resistant processes, confidentiality of keying material); and

## (f)
Applicable statutes, and executive directives and guidance to which the CKMS and its supporting documentation shall conform.

The statement of security objectives will provide a basis and justification for other provisions of the CKMS SP.

## 5.1.3 Organizational Responsibilities
The CKMS SP should identify the required CKMS management responsibilities and roles, including organizational contact information. The following classes of organizational responsibilities should be identified:

### (a)
Identification of an Individual Having Ultimate Responsibility for Key Management Within the Organization (e.g., the keying material manager) – Since the security of all data that is cryptographically protected depends on the security of the cryptographic keys employed, the ultimate responsibility for key management should reside at the executive level. The individual responsible for keying material management functions should report directly to the organization's Chief Information Officer (CIO). The individual responsible for keying material management should have capabilities and trustworthiness commensurate with the responsibility for maintaining the authority and integrity of all formal, electronic transactions and the confidentiality of all information that is sufficiently sensitive to warrant cryptographic protection.

### (b)
Identification of Infrastructure Entities and Roles - The CKMS SP should identify organizational responsibilities for critical CKMS roles. The following roles (where applicable to the type and complexity of the infrastructure being established) should be assigned and their responsibilities specified:
- Central Oversight Authority (may be the keying material manager),
- Oversight for relationships with public key certification authorities (CAs) or symmetric key centers,
- Oversight for relationships with registration authorities (RAs),
- Compliance auditor (ensures compliance with regulations and internal controls), and
- Oversight for operations (e.g., key processing facility(ies), service agents).

### (c)
Basis for and Identification of Essential Key Management Roles – The CKMS SP```markdown
# CURRENT_PAGE_RAW_OCR_TEXT

should also identify responsible organization(s), organization (not individual) contact information, and any relevant statutory or administrative requirements for the following functions, at a minimum:

- System administration and operation;
- Key generation or acquisition;
- Agreements with partner organizations regarding the mutual acceptance of keying material, as appropriate (e.g., agreements associated with multiple-center groups);
- Key establishment using manual or automated processes;
- Establishment of cryptoperiods, validity periods, and/or originator/recipient usage periods;
- Establishment of and accounting for keying material;
- Protection of secret and private keys and related materials;
- Emergency and routine revocation and suspension of keying material (e.g., revocation due to the compromise of a key);
- Auditing key usage logs;
- Key and/or certificate inventory management;
- Destruction of revoked or expired keys;
- Key back-up, archiving, and recovery;
- Compromise recovery;
- Contingency planning;
- Disciplinary consequences for the willful or negligent mishandling of keying material; and
- Generation, approval, and maintenance of key management policies and practice statements.

## 5.1.4 Sample CKMS SP Format

The sample format provided in this subsection is designed to be compatible with the standard format for PKI certificate policies (Appendix A). The sample format differs somewhat from that for PKI certificate policies (CPs) because some key management characteristics of and requirements for CKMS that accommodate symmetric keys differ from those for a purely PKI-based CKMS. The sample CKMS SP format below includes the general information called for in Subsections 5.1.2 and 5.1.3 above, plus some additional material that may be required in some administrative environments. As stated above, variations among organizational structures and needs will necessarily result in variations in the form and content of policy documentation. The sample CKMS SP format is provided as a general guide rather than as a mandatory template.

### (a) Introduction

The Introduction identifies and introduces the provisions of the policy document and indicates the security objectives and the types of entities and applications for which the CKMS SP is targeted. This section has the following subsections: 1) Overview, 2) Identification, 3) Community and Applicability, and 4) Contact Details.

#### Overview

This subsection introduces the CKMS SP.

#### Objectives

This subsection states the security objectives applicable to and expected to be supported by the CKMS. The Objectives subsection should include the elements of information called for in Section 5.1.2 (Security Objectives). (Note that in the case of a CP for a purely PKI environment, the Overview is followed by an Identification subsection that provides any applicable names or other identifiers, including ASN.1 object)
``````markdown
# CURRENT_PAGE_RAW_OCR_TEXT

## identifiers,
for the set of policy provisions.

## Community and Applicability
This subsection identifies the types of entities that establish keys or distribute certificates. In the general case of the CKMS, this will include the responsible entities identified in the "Identification of Infrastructure Entities and Roles" element of Section 5.1.3 (Organizational Responsibilities). (Note that in the case of a CKMS that includes a PKI CA, this subsection should identify the types of entities that issue certificates or that are certified as subject CAs, the types of entities that perform RA functions, and the types of entities that are certified as subject end entities or subscribers.)

This subsection may also contain:
- A list of applications for which the issued certificates and/or identified key types are suitable. (Examples of applications in this case are: electronic mail, retail transactions, contracts, travel orders, etc.)
- A list of applications to which the use of the issued certificates and/or identified key types is restricted. (This list implicitly prohibits all other uses for the certificates or key types.)
- A list of applications for which the use of the issued certificates and/or identified key types is prohibited.

## Contact Details
This subsection includes the organization, telephone number, and mailing and/or network address of the keying material manager. This is the authority responsible for the registration, maintenance, and interpretation of the CKMS SP (see Section 4.1.3).

## (b) General Provisions
The General Provisions section of the CKMS SP identifies any applicable policies regarding a range of legal and general practices topics. This section may contain subsections covering 1) obligations, 2) liability, 3) financial responsibility, 4) interpretation and enforcement, 5) fees, 6) publication and repositories, 7) compliance auditing, 8) confidentiality, and 9) intellectual property rights. Each subsection may need to separately state the provisions applying to each CKMS entity type. Note that many of the general provisions require input from and/or review by procurement elements of the organization.

### Obligations
This subsection contains, for each entity type, any applicable policies regarding the entity's obligations to other entities. Such provisions may include: 1) keying material manager and/or Central Oversight Authority obligations, 2) key center obligations (symmetric key management-specific), 3) multiple-center group obligations (symmetric key management-specific) 4) service agent obligations, 5) CA and/or RA obligations (public key management-specific), 6) User obligations (including client nodes and public key subscribers and relying parties), 7) key-recovery agent obligations, and 8) keying material repository obligations.

### Liability
This subsection contains, for each entity type, any applicable policies regarding the apportionment of liability (e.g., warranties and limitations on warranties,
```# CURRENT_PAGE_RAW_OCR_TEXT

## Kinds of Damages Covered and Disclaimers
Loss limitations per certificate or per transaction, and other exclusions, e.g., acts of God.

## Financial Responsibility
For key and/or certificate providers (e.g., key processing facilities, PKI CAs, key or certificate repositories, PKI RAs), this section contains any applicable policies regarding financial responsibilities, such as:
1. An indemnification statement,
2. Fiduciary relationships (or lack thereof) among the various entities, and
3. Administrative processes (e.g., accounting, audit).

## Interpretation and Enforcement
This subsection contains any applicable policies regarding the interpretation and enforcement of the CKMS SP or CKMS Practice Statement, addressing such topics as:
1. Governing law;
2. Dispute resolution procedures; and
3. Other technical contract issues, such as the severability of provisions, survival, merger, and notice.

## Fees
This subsection contains any applicable policies regarding interagency reimbursement or fees charged by key and/or certificate providers (e.g., reimbursement for key-center management, certificate issuance or renewal fees, a certificate access fee, revocation or status information access fee, key recovery fee, reimbursement for information desk services, fees for other services such as policy information, refund policy).

## Publication and Repositories
This subsection contains any applicable policies regarding:
1. A key and/or certificate source's obligations, where keys are not locally generated, to publish information regarding its practices, its products (e.g., keys and/or certificates), and the current status of such products;
2. The frequency of publication;
3. Access control on published information (e.g., policies, practice statements, certificates, key and/or certificate status, RKNs); and
4. Requirements pertaining to the use of repositories operated by private-sector CAs or by other independent parties.

## Compliance Audit
This subsection addresses any high-level policies regarding:
1. The frequency of compliance audits for CKMS entities,
2. The identity/qualifications of the compliance auditor,
3. The auditor's relationship to the entity being audited,
4. Topics covered under the compliance audit,
5. Actions taken as a result of a deficiency found during a compliance audit, and
6. The dissemination of compliance audit results.

## Confidentiality Policy
This subsection states policies regarding:
1. The types of information that shall be kept confidential by CKMS entities,
2. The types of information that are not considered confidential,
3. The dissemination of reasons for the revocation of certificates and symmetric keys,
4. The release of information to third parties (e.g., legal entities),
5. Information that can be revealed as part of civil discovery (e.g., material that may be subject to FOIA requests or subpoenas in civil actions),
6. The disclosure of keys.# CURRENT_PAGE_RAW_OCR_TEXT

or certificates by CKMS entities at subscriber/user request, and 7) any other circumstances under which confidential information may be disclosed.

## Intellectual Property Rights

This subsection addresses policies concerning the ownership rights of certificates, practice/policy specifications, names, and keys.

### (c) Identification and Authentication

The Identification and Authentication section describes circumstances and identifies any applicable regulatory authority and guidelines regarding the authentication of a certificate applicant or key requestor prior to the issuing of key(s) or certificate(s) by a keying material source. This section also includes policies regarding the authentication of parties requesting key or certificate replacement, key recovery or revocation. Where applicable, this section also addresses CKMS naming practices, including name ownership recognition and name dispute resolution. This section of the CKMS SP has the following subsections:

- Initial Registration,
- Routine Key and/or Certificate Replacement,
- Re-keying and Certificate Replacement After Revocation,
- Key Recovery, and
- Revocation Request.

### (d) Operational Requirements

The Operational Requirements section specifies policies regarding the imposition of requirements on CKMS entities with respect to various operational activities. This section should address the following topics, as appropriate:

- Request for actions needed to establish keys or certificates,
- Initial issuance of key and/or certificates,
- Validity checking and acceptance of keys and certificates,
- Establishing and maintaining inventories of keys and certificates that include expiration dates and linking keys to owner and sponsor identities,
- Notification to key owners when keys or certificates are about to expire,
- Key and/or certificate suspension and revocation,
- Security audit requirements,
- Key backup and archiving,
- Records archiving,
- Key and/or certificate replacement (i.e., re-keying and key derivation),
- Key recovery,
- Compromise and disaster recovery, and
- Key service termination (e.g., key center, CA, key storage).

Within each topic, separate consideration may need to be given to each type of CKMS component.

### (e) Minimum Baseline Security Controls

This section states the policies regarding the management, operational, and technical security controls (e.g., physical, procedural, and personnel controls) used by CKMS components to securely perform 1) key generation, 2) entity/source authentication, 3) key establishment and/or certificate issuance, 4) key inventory creation and maintenance, 5) key and/or certificate revocation and suspension, 6) auditing, and 7) key storage and recovery (i.e., to and from backups and archives).

For federal government systems, based on the FIPS 199 impact level, the appropriate minimum baseline of security controls contained in SP 800-53 shall be.# CURRENT_PAGE_RAW_OCR_TEXT

implemented and described in this section of the CKMS SP.

## (f) Cryptographic Key, Message Interchange, and/or Certificate Formats

This section is used to state policies specifying conformance to specific standards and/or guidelines regarding 1) key management architectures and/or protocols, 2) key management message formats, 3) certificate formats and/or 4) RKN formats.

## (g) Specification and Administration

This section of the policy document specifies:
- The organization(s) that has change-control responsibility for the CKMS SP,
- Publication and notification procedures for new CKMS SP versions, and
- CKMS Practice Statement approval procedures.

## 5.2 Policy Enforcement

In order to be effective, key management policies shall be enforced, and policy implementation should be evaluated on a regular basis and whenever there is a significant change in the cryptographic technologies used. Each organization will need to determine its enforcement requirements based on the sensitivity of information being exchanged or stored; the communications volume associated with sensitive or critical information and processes; the storage required for operational, backed-up and archived keys; provisions for key recovery; personnel resources; the size and complexity of the organization or organizations supported; the variety and numbers of cryptographic devices and applications; the types of cryptographic devices and applications; and the scale and complexity of protected communications facilities.

# 6 CKMS Practices Statement (CKMS PS)

The CKMS Practices Statement (CKMS PS) establishes a trust root for the CKMS and specifies how key management procedures and techniques are used to enforce the CKMS Security Policy (see Section 5) and to conform with the Key Management Specification (see Section 4). For example, a CKMS Security policy might state that secret and private keys shall be protected from unauthorized disclosure. The corresponding CKMS PS might then state that secret and private keys shall be either cryptographically wrapped or physically protected, and that it is the responsibility of the network systems administrator to ensure that the keys are properly safeguarded. (The CKMS PS would also identify and provide contact information for the network systems administrator.) Note that the practices information contained in a CKMS PS is more prescriptive and specific than policy material contained in a CKMS Security Policy so it will be subject to more frequent change. Several CKMS PSs may implement a CKMS Security Policy for a single organization or one for each organizational key management domain (e.g., one for each of several CAs).

## 6.1 Alternative Practice Statement Formats

As in the case of the policy documentation, the security plan, practice document (i.e., CKMS PS), and/or procedure document into which a CKMS PS is inserted will vary from organization to organization. In general, the nature and complexity of the CKMS PS will vary with an# Organization's Key Management Infrastructure

## Overview
The organization's existing documentation requirements and the size and complexity of an organization's key management infrastructure.

Each CKMS PS applies to a single CKMS or a single domain of that CKMS. The CKMS PS may be considered the overall operations manual for the CKMS. Specific portions of the CKMS PS may be extracted to form application or role-specific documentation. Auditors and accreditors may use the CKMS PS to supplement the CKMS Security Policy during reviews of CKMS operations.

### 6.1.1 Stand-Alone Practice Statement
While it is recommended that organizations create stand-alone practices documents (i.e., CKMS PSs), the practice information may be included in pre-existing top-level organizational information security policies and/or security procedures documents. A stand-alone CKMS PS may follow the general RFC 3647 format described for the CKMS Security Policy in Section 5.1.4, or it may follow a proprietary format. If the general outline of the sample CKMS Security Policy format is followed, the authors of the CKMS Security Policy will need to consider the basic differences in character between a CKMS Security Policy and a CKMS PS. While the CKMS Security Policy is a high-level document that describes a security policy for managing keys or certificates, the CKMS PS is a highly detailed document that describes how a CKMS implements a specific CKMS Security Policy. The CKMS PS identifies any CKMS Security Policies that it implements and specifies the mechanisms and procedures that are used to support each CKMS Security Policy. Where the CKMS Security Policy specifies organizational roles and states requirements for mechanisms and procedures, the CKMS PS identifies more specific roles and responsibilities, and describes the mechanisms and procedures in detail. (Note that descriptive material can sometimes be included by reference to other procedures, guidelines, and/or standards documents.) The CKMS PS should include sufficient operational detail to demonstrate that the CKMS Security Policy can be satisfied by this combination of mechanisms and procedures.

### 6.1.2 Certification Practices Statement
A certification practices statement (CPS) is a PKI-specific document. In a purely PKI environment, the RFC 3647-specified CPS may serve as the CKMS PS for a CA. In such cases, the CPS will follow the RFC 3647 format summarized in Appendix A.

## 6.2 Common CKMS PS Content
Regardless of the CKMS PS format employed, the CKMS PS needs to include a minimum set of information. This subsection identifies the kinds of information that should be included in all CKMS PSs, when appropriate.

### 6.2.1 Association of CKMS PS with the CKMS Security Policy
The CKMS PS should identify the CKMS to which it applies and the CKMS Security Policy that its content implements.

### 6.2.2 Identification of Responsible Entities and Contact Information
The CKMS PS should identify the organizational entities that perform the various```markdown
# Functions

Identified in the Organizational Responsibilities section (if following the organization of the CKMS Security Policy provided in Section 5.1.3). The individuals assigned to perform each key management role should be identified (e.g., by title). Contact information should include the individual's identity (e.g., a title), organization, business address, telephone number, and electronic mail address.

## 6.2.3 Key Generation and/or Certificate Issuance

The CKMS PS should prescribe key generation and/or certificate issuance functions. Key generation and/or certificate issuance should be accomplished in accordance with the guidelines contained in the key establishment sections of Part 1 (Section 8.1.5). The scope of key acquisition includes out-of-band procedures for acquiring initial and replacement keying material (e.g., initial key wrapping keys for communication with key centers and service agent procedures for the emergency replacement of compromised keys).

The CKMS PS generally identifies:
- Any management organization, roles, and responsibilities associated with key generation and/or certificate issuance,
- Any standards and guidelines governing key generation/certificate issuance facilities and processes, and
- Any documents required for authorization, implementation, and accounting functions.

For organizations that employ public-key cryptography, the CKMS PS (i.e., the CPS) should identify the certificate issuance elements of the CA (and its hardware, software, and human/organizational components as appropriate), as well as registration authorities (RAs). Operating procedures and quality control procedures for key generation keying material and/or certificate issuance may appear either in the CKMS PS or in separate documents referenced by the CKMS PS. A documentation of the key generation and/or certificate issuance processes should also be included in order to establish a chain of evidence to support the establishment of the trusted source of keying material (e.g., a trust root for public key certificates or a symmetric key center).

## 6.2.4 Key Agreement

Key agreement involves participation by more than one entity in the creation of shared keying material. Public key techniques are normally employed to accomplish key agreement. See SP 800-175B and SP 800-56A for further discussions of key agreement techniques. CKMS PSs may prescribe the organizational authority and procedures for authorizing and implementing key agreement between or among partner organizations. Within the context of a CKMS, key agreement will commonly be implemented by client nodes, using key agreement keys or key pairs received from key processing facilities.

## 6.2.5 Agreements Between Key Processing Centers

Organizations that have distinct public key certification hierarchies or meshes (see Section 2.3.8),
```# CURRENT_PAGE_RAW_OCR_TEXT

but require secure communications between their domains may agree to cross-certify their organizations' CAs (i.e., key processing facilities). Similarly, in centralized symmetric key management structures, multiple key centers (i.e., key processing facilities) may agree to work together as a multiple-center group (see SP 800-71).

Where entities within different organizations need to communicate securely with each other, the key processing facilities that serve them will need to establish formal agreements to work together to provide cryptographic services to their subscribers. For example, in PKI hierarchies or meshes, this would be a cross-certification agreement. CKMS PSs may prescribe the organizational authority and procedures for authorizing and implementing the cross-certification or sharing of keying material between or among partner organizations. Within the context of the CKMS, any authorization for these agreements should come from the Central Oversight Authority or its organizational equivalent. The cross-certification process between CAs or the sharing of keying material between key centers will normally be implemented in the key processing facility.

## 6.2.6 Key Establishment, Suspension and Revocation Structures

The CKMS PS should prescribe the organizational authority and procedures for the design and management of the organizational structure and information flow necessary to meet the organization's key establishment, suspension, and revocation requirements. The CKMS PS should include or reference guidelines for maintaining the continuity of operations and maintaining both the assurance and integrity of the revocation and suspension processes. The CKMS PS should include guidelines for the maintenance of revocation lists and the emergency replacement of keys and certificates as well as the timely and reliable routine establishment of keys and certificates. Both the establishment of an initial key between entities and changes to key establishment, suspension and revocation procedures should be authorized by the Central Oversight Authority and implemented by the key processing facility (or their equivalents) as described in the CKMS discussion (see Section 2.3.2). Additionally, a prescription of the audit and control of the key establishment process is necessary in order to maintain confidence in the integrity of the source of keying material.

## 6.2.7 Establishment of Cryptoperiods

The CKMS PS should prescribe cryptoperiods for the keying material employed by an organization. Cryptoperiods should be approved by the Central Oversight Authority, or its organizational equivalent, and should be implemented by the CA or other key processing facility and client nodes (or their equivalents), as described in the CKMS discussion (see Section 2.3). Recommendations for establishing cryptoperiods are provided in Section 5.3 of Part 1.

## 6.2.8 Tracking of and Accounting for Keying Material

For keys distributed from a key processing center rather than established at# Key Management System (CKMS) Policy Specification (PS)

## Client Nodes Using Key Agreement

Client nodes using key agreement or other automated key establishment techniques, the CKMS PS should prescribe the organizational authority and procedures for the local creation of, distribution of, access to, and accounting for keying material required at each phase of the key management lifecycle (see Part 1, Sections 7 and 8). Any relevant accounting formats and database structures should be specified as required for:

- Keying material generation or recovery requests,
- Authorization of the distribution of specific keying material to specific organizational destinations for use in specific devices,
- Physical or automated establishment of keys or related key information (to include metadata),
- Key and/or certificate inventories,
- Receipts for keys or related key information,
- Reporting of the receipt of keys not accompanied by authorized transmittal information,
- Backup and archiving of key information,
- Requesting the recovery of backed up or archived key information, and
- The destruction of key information and related cryptographic materials.

General accountability recommendations are provided in Section 9.2 of Part 1; general key inventory guidance is provided in Section 9.5 of Part 1. Responsibilities and procedures should be identified for a CKMS, including the Central Oversight Authority, the CA or other key processing facility, service agent, and client node entities of the CKMS (or their equivalents).

## 6.2.9 Protection of Key Information

The CKMS PS should prescribe the responsibilities, facilities, and procedures for the protection of key information. This includes requirements for both the transmission and storage of key information. Requirements should be specified for a CKMS, including the Central Oversight Authority, CA or other key processing facility, service agent, and client node entities of the CKMS (or their equivalents). General recommendations for the protection of keys at different lifecycle stages (provided in Part 1, Sections 6.1.1, 7 and 8) should be included or referenced in the CKMS PS.

Note that where keys and key establishment security mechanisms are integral to a FIPS 140-compliant cryptographic module or application, reference to FIPS 140, its validated security level and any local physical security procedures may provide an adequate specification of protection practices.

## 6.2.10 Suspension and Revocation of Keying Material

The CKMS PS should prescribe the roles, responsibilities, and procedures for the suspension, and emergency and routine revocation of keying material. The CKMS PS should also prescribe the roles, procedures, and protocols employed at the key processing facility for the generation of RKNs for lost or destroyed certificates and keys, or for compromised certificates and keys. The CKMS PS should also specify the roles, procedures, and protocols employed by service agents.```markdown
# CURRENT_PAGE_RAW_OCR_TEXT

and client node entities, or their organizational equivalents, for the timely
and secure reporting of potential compromises. The CKMS PS should identify the key types and reasons for which suspension and revocation actions are taken (e.g., suspension: key owner is on leave or a key compromise is suspected; revocation: key compromise or the key owner has left the organization); suspension and revocation are not necessary for ephemeral keys. General recommendations for key revocation are provided in Part 1, Section 8.3.5 and should be included or referenced in the CKMS PS.

## 6.2.11 Auditing

The CKMS PS should prescribe the roles, responsibilities, facilities, and procedures for the routine auditing of keying material and related records (e.g., metadata), including their generation, access and destruction. The CKMS PS should also describe audit reporting requirements and procedures. Auditing should occur wherever keys are handled (generated, stored, recovered, or destroyed). Note that audit requirements will depend on the sensitivity of the information (including what is to be audited, the frequency of audits, and the frequency of reviews of different elements of the audit log). Note that audits will generally be conducted in facilities that distribute or receive keys (e.g., CAs or other key processing centers) rather than for cryptographic devices that use automatically established keys. However, developers should include logging and auditing capabilities in clients. Conditions and procedures should also be included for unscheduled audits that are triggered by the observed and/or suspected unauthorized access, production, loss, or compromise of key information. General audit recommendations are provided in Part 1, Section 9.2 and SP 800-152, Section 8.2.4.

## 6.2.12 Key Destruction

The CKMS PS should prescribe the roles, responsibilities, facilities, and procedures for any routine destruction of revoked or expired keys required at all CKMS elements. Key destruction conditions and procedures may also be included. Part 1 (Sections 8.3.4 and 8.4) and SP 800-152 (Section 6.4.9) include recommendations that should be included or referenced in the CKMS PS. Note that the destruction of keys is not completed until all copies are destroyed (including backups). Keying material in archives may need to be retained for later retrieval, but the keys should be destroyed when no longer needed.

## 6.2.13 Key Backup, Archiving and Recovery

OMB Guidance to Federal Agencies on Data Availability and Encryption, 26 November 2001, states that agencies must address information availability and assurance requirements through appropriate data recovery mechanisms such as cryptographic key recovery. For each CKMS, the CKMS PS should prescribe any roles, responsibilities, facilities, and procedures necessary for all organizational elements to backup, archive and recover critical key information.
``````markdown
# CURRENT_PAGE_RAW_OCR_TEXT

## with the necessary
integrity mechanisms successfully verified for the stored information, in the
event of the loss or
expiration of the operational copy of cryptographic keys under which the data is
protected.

Backups support recovering the current operational keys. Archives support the
recovery of keys,
primarily for the recovery of information after the key's cryptoperiod has
expired. Key backup,
archive and recovery are normally the responsibility of the Central Oversight
Authority, or its
organizational equivalent, although mechanisms to support recovery may be
included in other
components of a CKMS. Part 1, Appendix B.5, contains general key recovery
recommendations
that should be included in or referenced by the CKMPS. Examples of key recovery
policies include
the Key Recovery Policy for The Department of the Treasury Public Key
Infrastructure (PKI),
Federal Public Key Infrastructure Key Recovery Policy, and Key Recovery Policy
for External
Certification Authorities.

## 6.2.14 Compromise Recovery
For all CKMS elements, the CKMS PS should prescribe any roles, responsibilities,
facilities, and
procedures required for recovery from the compromise of a cryptographic key at
any phase in its
lifecycle. Compromise recovery includes 1) the timely and secure notification of
owners and
sponsors of compromised keys that the compromise has occurred and 2) the timely
and secure
replacement of the compromised keys. Emergency key revocation and the generation
and
processing of RKNs are elements of compromise recovery, but compromise recovery
also
includes:
- The recognition and reporting of the compromise,
- The identification and/or establishment of replacement keys and/or
certificates,
- Recording the compromise and compromise recovery actions (may use existing
audit
mechanisms and procedures), and
- The destruction and/or de-registration of compromised keys, as appropriate.

Part 1 (Sections 9.3.4 and 10.2.9) and SP 800-152 (Section 6.8) contain
recommendations
regarding compromise recovery that should be included in or referenced by the
CKMS PS.

## 6.2.15 Policy Violation Consequences
The CKMS PS should prescribe any roles, responsibilities, and procedures
required for
establishing and carrying out disciplinary consequences for the willful or
negligent mishandling
of key information. The consequences should be commensurate with the potential
harm that can
result from the violation of the organization's policy, its mission, and/or
other affected
organizations. While the procedures apply to all CKMS elements, the
responsibility for
establishing and enforcing the procedures rests at the Central Oversight
Authority or its
organizational equivalent. Consequences prescribed in a CKMS PS shall be
enforced if they are
to be effective. Note that it is necessary to correlate compromise records and
the associated audit
```# CURRENT_PAGE_RAW_OCR_TEXT

logs to the disciplinary actions that are taken as a result of violations of policies or procedures.

## 6.2.16 Documentation

The CKMS PS should prescribe any roles, responsibilities, and procedures required for the generation, approval, and maintenance of the CKMS PS. The generation and maintenance of CKMS PSs should normally be the responsibilities of the entity responsible for management of the CA/key center. The CKMS PS should be approved by the Central Oversight Authority or its organizational equivalent. The generation and maintenance of audit records are also normally the responsibilities of the Central Oversight Authority or its organizational equivalent. The generation and maintenance of registration, de-registration, revocation and compromise lists, revoked key notifications, and accounting documentation should be accomplished at the key processing facility(ies), service agent(s), and client nodes (or their organizational equivalents), as required by the CKMS PS (see Section 2).