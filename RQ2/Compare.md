### **RQ2: Comparison with Existing Work**

LegalGen significantly outperforms the state-of-the-art tool iSyn in synthesizing smart contracts. While iSyn relies on predefined intermediate representations (IR) and NLP techniques, it struggles with capturing the complex logic of financial agreements, such as multi-level conditions and dynamic pricing clauses.

#### **Performance Comparison**
LegalGen shows consistent improvements over iSyn across key metrics:

| Metric                  | iSyn   | LegalGen$_{Llama}$ | LegalGen$_{GPT-4o}$ |
|-------------------------|--------|--------------------|---------------------|
| Functional Similarity  | 0.872  | 0.901              | 0.925              |
| Semantic Similarity    | 0.858  | 0.892              | 0.917              |
| Clause Consistency     | 0.81   | 0.86               | 0.88               |
| Semantic Coverage      | 0.79   | 0.83               | 0.85               |
| Functional Completeness| 0.83   | 0.89               | 0.91               |

#### **Key Improvements**
1. **Higher Accuracy**: LegalGen achieves better functional and semantic similarity scores, particularly in complex scenarios such as payment clauses and time-dependent conditions.
2. **Robust Clause Handling**: The Concept Derivor and Ontology Inferrer modules enable LegalGen to translate legal clauses into smart contract code more accurately.
3. **Enhanced Test Results**: LegalGen$_{GPT-4o}$ achieves a 92.3% pass rate and 89.1% code coverage, outperforming iSyn’s 86.5% and 82.3%, respectively.

