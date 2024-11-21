# Construct the prompt
prompt = f"""
You are a smart contract generator. Based on the following Solidity template, concept instance, and few-shot examples, generate a complete smart contract:
Template:
{solidity_template}

Concept Instance:
{concept_instance}

Few-Shot Examples:
{few_shot_examples}

Generate the final contract:
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant skilled in generating smart contracts."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=2000,
    temperature=0.5
)

generated_contract = response["choices"][0]["message"]["content"]

print("Generated Smart Contract:")
print(generated_contract)

# Save the contract to a file
with open("GeneratedContract.sol", "w") as file:
    file.write(generated_contract)
