legal_concepts = {"Buyer", "Seller", "Payment Amount", "Termination Conditions"}

contract_concepts = {"Buyer", "Seller", "Payment Amount", "State Updates"}

# Calculate semantic coverage
covered_concepts = legal_concepts.intersection(contract_concepts)
semantic_coverage_score = len(covered_concepts) / len(legal_concepts)
print(f"Semantic Coverage Score: {semantic_coverage_score:.2f}")
