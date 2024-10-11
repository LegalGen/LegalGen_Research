# LegalGen: LLM-Powered Smart Contract Synthesis from Legal Financial Agreements

LegalGen is an advanced framework designed to automate the conversion of legal financial agreements into blockchain-based smart contracts using large language models (LLMs). It leverages cutting-edge natural language processing (NLP) techniques and legal domain-specific knowledge to simplify and streamline the process of smart contract generation, significantly reducing the manual effort required to translate complex legal terms into executable code.

## Features

- **Automatic Smart Contract Generation**: Transforms legal agreements into executable smart contracts, primarily optimized for financial transaction agreements.
- **LLM-Enhanced NLP**: Uses state-of-the-art large language models (LLMs) to understand and process complex legal language.
- **Legal Knowledge Base**: Automatically builds a knowledge base from a large corpus of legal agreements to improve contract synthesis.
- **Clustering and Concept Extraction**: Groups legal agreements with similar structures, extracts key legal concepts (e.g., payment terms, breach conditions), and organizes them into an ontology.
- **Template-Based Contract Synthesis**: Generates Solidity-based smart contracts using predefined templates and legal domain knowledge.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use LegalGen locally, follow these steps:

### Prerequisites

1. Python 3.8 or later
2. Required libraries: `transformers`, `numpy`, `scikit-learn`, `solidity`

You can install the dependencies via `pip`:

```bash
pip install -r requirements.txt
```

### Setting Up the Project

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/LegalGen.git
cd LegalGen
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Set up a Solidity development environment to test the generated smart contracts, e.g., using the [Truffle Suite](https://www.trufflesuite.com/):

```bash
npm install -g truffle
```

## Usage

### Generating Smart Contracts from Legal Agreements

LegalGen automatically processes legal agreements to generate smart contracts. To use the tool:

1. Prepare a legal financial agreement in plain text format.
2. Run LegalGen using the following command:

```bash
python legalgen.py --input [legal_agreement.txt] --output [smart_contract.sol]
```

### Options

- `--input`: The path to the input legal agreement file.
- `--output`: The path where the generated smart contract will be saved.

Example:

```bash
python legalgen.py --input agreements/employment_agreement.txt --output contracts/employment_contract.sol
```

### Smart Contract Testing

Once the smart contract is generated, you can test it using the Truffle framework:

```bash
truffle test
```

This will run the tests for the generated Solidity contract to ensure functionality and correctness.

## Evaluation

LegalGen has been tested on over 500 real-world legal financial agreements from various categories, including:

- Employment Agreements
- Purchase Agreements
- Trust Agreements
- Credit Contracts

### Performance Metrics

LegalGen outperforms state-of-the-art techniques like iSyn in both functional and semantic similarity when generating smart contracts. Key evaluation metrics include:

- **Functional Similarity**: How closely the generated smart contract aligns with the expected functionality.
- **Semantic Similarity**: How well the contract reflects the legal clauses in the original agreement.
- **Clause Consistency**: Ensures the generated smart contracts accurately reflect the key clauses of the legal agreement.
- **Test Case Pass Rate**: Ensures the generated smart contracts pass all key functional tests.

## Contributing

We welcome contributions to LegalGen! If you are interested in contributing, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

