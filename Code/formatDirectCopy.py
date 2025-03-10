from textblob import TextBlob
import re

with open('manual\FIPS PUB 140-2.txt', 'r', encoding='UTF-8') as f:
    text = f.read()

blob = TextBlob(text)
test = """FIPS PUB 140-2
CHANGE NOTICES (12-03-2002)
FEDERAL INFORMATION PROCESSING STANDARDS PUBLICATION
(Supercedes FIPS PUB 140-1, 1994 January 11)
SECURITY REQUIREMENTS FOR CRYPTOGRAPHIC
MODULES
CATEGORY: COMPUTER SECURITY SUBCATEGORY: CRYPTOGRAPHY
Information Technology Laboratory
National Institute of Standards and Technology
Gaithersburg, MD 20899-8900
Issued May 25, 2001
U.S. Department of Commerce
Donald L. Evans, Secretary
Technology Administration
Phillip J. Bond, Under Secretary for Technology
National Institute of Standards and Technology
Arden L. Bement, Jr., Director
i
Foreword
The Federal Information Processing Standards Publication Series of the National Institute of Standards and Technology (NIST) is
the official series of publications relating to standards and guidelines adopted and promulgated under the provisions of Section
5131 of the Information Technology Management Reform Act of 1996 (Public Law 104-106) and the Computer Security Act of
1987 (Public Law 100-235). These mandates have given the Secretary of Commerce and NIST important responsibilities for
improving the utilization and management of computer and related telecommunications systems in the Federal government. The
NIST, through its Information Technology Laboratory, provides leadership, technical guidance, and coordination of government
efforts in the development of standards and guidelines in these areas.
Comments concerning Federal Information Processing Standards Publications are welcomed and should be addressed to the
Director, Information Technology Laboratory, National Institute of Standards and Technology, 100 Bureau Drive, Stop 8900,
Gaithersburg, MD 20899-8900.
 William Mehuron, Director
Information Technology Laboratory
Abstract
The selective application of technological and related procedural safeguards is an important responsibility of every Federal
organization in providing adequate security in its computer and telecommunication systems. This publication provides a standard
that will be used by Federal organizations when these organizations specify that cryptographic-based security systems are to be
used to provide protection for sensitive or valuable data. Protection of a cryptographic module within a security system is
necessary to maintain the confidentiality and integrity of the information protected by the module. This standard specifies the
security requirements that will be satisfied by a cryptographic module. The standard provides four increasing, qualitative levels
of security intended to cover a wide range of potential applications and environments. The security requirements cover areas
related to the secure design and implementation of a cryptographic module. These areas include cryptographic module
specification; cryptographic module ports and interfaces; roles, services, and authentication; finite state model; physical security;
operational environment; cryptographic key management; electromagnetic interference/electromagnetic compatibility
(EMI/EMC); self-tests; design assurance; and mitigation of other attacks.
Key words: computer security, telecommunication security, cryptography, cryptographic modules, Federal Information
Processing Standard (FIPS).
National Institute of Standards U.S. Government Printing Office For Sale by the National
and Technology Washington: 2001 Technical Information
FIPS PUB 140-2 Service
64 pages (May 25, 2001) U.S. Department of Commerce"""
fixed = ''
for s in blob.sentences:
    s = str(s)
    s = s[0] + s[1:-1].replace("\n", " ") + s[-1] if len(s) > 1 else s
    fixed = fixed + s

# with open('manual\FIPS PUB 140-2 FIXED.txt', 'w', encoding='UTF-8') as f:
#     f.write(fixed)
blobtest = TextBlob(test)
for t in blobtest.sentences:
    t = str(t)
    print(t + '\n')
    print(t[0] + t[1:-1].replace('\n', ' ') + t[-1] if len(t) > 1 else t)