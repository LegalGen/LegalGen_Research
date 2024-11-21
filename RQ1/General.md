### **RQ1: How effective is LegalGen in synthesizing smart contracts from legal agreements?**

#### **Evaluation Setup**
- **Dataset**: 
  - 500 legal agreements from Law Insider, with 300 agreements for knowledge base construction and 200 for testing.
- **Methods**: 
  - LegalGen was tested with two LLM configurations: Llama and GPT-4o.
  - Baseline comparison with iSyn.
- **Metrics**:
  1. **Functional Similarity**: Validates core logic consistency with ground-truth contracts.
  2. **Semantic Similarity**: Uses AST-based similarity for semantic alignment.
  3. **LLM-Eval**: Assesses clause consistency, semantic coverage, and functional completeness.
  4. **Manual Inspection**: Verifies semantic accuracy and functional consistency.

#### **Key Results**
- **Performance**: 
  - LegalGen_{GPT-4o} achieved **0.925** functional and **0.917** semantic similarity scores, outperforming LegalGen$_{Llama}$ (**0.901**, **0.892**) and iSyn (**0.872**, **0.858**).
- **LLM-Eval Scores**:
  - LegalGen_{GPT-4o}: Clause Consistency (0.88), Semantic Coverage (0.85), Functional Completeness (0.91).
  - Outperformed iSyn in all metrics (improvements of 7-9%).
- **Case Study**: LegalGen handles complex clauses (e.g., payment logic) more accurately than iSyn.

#### **Reproducibility**
- Run `contract_generator.py` to synthesize smart contracts.
- Evaluate with provided test cases using Truffle (`truffle test`).  
- Full instructions available in the `README`. 

LegalGen demonstrates superior performance in generating accurate smart contracts compared to state-of-the-art methods.
