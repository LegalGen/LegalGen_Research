### **FAQ (Frequently Asked Questions)**

#### **1. What is the main goal of LegalGen?**
LegalGen is a framework that leverages Large Language Models (LLMs) to synthesize blockchain-based smart contracts from legal agreements, particularly those involving financial transactions. It builds a knowledge base, extracts key concepts, and uses an ontology to generate accurate and functional Solidity smart contracts.

---

#### **2. What types of legal agreements does LegalGen support?**
Currently, LegalGen focuses on legal agreements related to financial transactions. These agreements were chosen because they represent over 80% of the agreements in Law Insider’s top categories.

---

#### **3. Which LLMs are supported by LegalGen?**
LegalGen has been tested with **Llama** and **GPT-4o**. However, other LLMs capable of text comprehension and code generation can also be integrated with minor adjustments.

---

#### **4. How does LegalGen improve on existing smart contract generation tools like iSyn?**
LegalGen enhances the process by:
- Leveraging LLMs fine-tuned with legal domain knowledge.
- Building a detailed knowledge base with clustering, segmentation, and ontology inference.
- Generating contracts that demonstrate higher functional and semantic similarity to the original legal agreements.
