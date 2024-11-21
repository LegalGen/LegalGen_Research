from brownie import MyContract, accounts

def test_payment():
    # Setup
    buyer = accounts[0]
    seller = accounts[1]
    contract = MyContract.deploy(buyer, seller, 1000, {'from': buyer})

    # Test payment
    tx = contract.pay({'from': buyer, 'value': 1000})
    assert tx, "Payment failed"

def test_termination():
    # Setup
    buyer = accounts[0]
    seller = accounts[1]
    contract = MyContract.deploy(buyer, seller, 1000, {'from': buyer})

    # Test termination
    contract.terminate({'from': buyer})
    assert contract.terminated() == True, "Termination failed"
