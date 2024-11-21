from difflib import SequenceMatcher
from solidity_parser import parser

legal_clauses = [
    "The buyer must pay $5000 before the deadline.",
    "The contract will terminate if the seller fails to deliver goods."
]

# Generated smart contract code
contract_code = """

"""


ast_tree = parser.parse(contract_code)


contract_logic = [
    "The buyer must pay $5000 before execution.",
    "The contract will terminate if goods are not delivered."
]


def calculate_similarity(clause, logic):
    return SequenceMatcher(None, clause, logic).ratio()

similarities = [calculate_similarity(c, l) for c, l in zip(legal_clauses, contract_logic)]
clause_consistency_score = sum(similarities) / len(similarities)
print(f"Clause Consistency Score: {clause_consistency_score:.2f}")
