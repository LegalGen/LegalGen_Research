const g_rs = artifacts.require("g_rs");

contract("g_rs", (accounts) => {
  let contract;
  const [seller, buyer] = accounts;

  beforeEach(async () => {
    contract = await g_rs.new();
    await contract.setSellerAddress(seller);
    await contract.setBuyerAddress([buyer]);
  });

  it("should correctly set the seller address", async () => {
    const setSeller = await contract.seller();
    assert.equal(setSeller, seller, "The seller address was not set correctly");
  });

  it("should correctly set the buyer address", async () => {
  const buyerAddresses = await contract.getBuyers();
  assert.equal(buyerAddresses[0], buyer, "The buyer address was not set correctly");
  });

  it("should test payment functionality", async () => {
    const paymentAmount = web3.utils.toWei("1", "ether"); // Example payment amount
    await contract.pay_0({ from: buyer, value: paymentAmount });

    // Check if the payment has been processed, you can add assertions for the emitted event
    // Example: Check if state has changed to Locked, or if event Payed was emitted
  });

  it("should allow termination of the contract", async () => {
    const buyerIndex = 0;
    await contract.terminateByTransfer(buyerIndex, { from: seller });

    // Add checks here, for example, check if the state is Inactive
    // Example: Check if state has changed to Inactive or if Terminated event was emitted
  });
});

  it("should set state to Inactive after termination", async () => {
    const buyerIndex = 0;
    await contract.terminateByTransfer(buyerIndex, { from: seller });
  
    const state = await contract.state();
    assert.equal(state.toString(), "2", "State should be Inactive after termination"); // Replace "2" with the correct enum value
  });
  
  it("should emit Terminated event upon contract termination", async () => {
    const buyerIndex = 0;
    const receipt = await contract.terminateByTransfer(buyerIndex, { from: seller });
  
    const event = receipt.logs.find(log => log.event === "Terminated");
    assert(event, "Terminated event should be emitted");
    assert.equal(event.args.by, seller, "Event should log the correct seller");
  });
