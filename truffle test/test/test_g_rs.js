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
    const paymentAmount = web3.utils.toWei("1", "ether"); 
    await contract.pay_0({ from: buyer, value: paymentAmount });
    
  });

  it("should allow termination of the contract", async () => {
    const buyerIndex = 0;
    await contract.terminateByTransfer(buyerIndex, { from: seller });
    
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
