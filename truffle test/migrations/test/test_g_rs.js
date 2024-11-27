const g_rs = artifacts.require("g_rs");

contract("g_rs", (accounts) => {
  let contract;
  const [seller, buyer] = accounts;

  beforeEach(async () => {
    contract = await g_rs.new();
    await contract.setSellerAddress(seller);
    await contract.setBuyerAddress([buyer]);
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

