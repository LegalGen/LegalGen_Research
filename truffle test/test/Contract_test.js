const GeneratedContract = artifacts.require("GeneratedContract");

contract("GeneratedContract", (accounts) => {
    const buyer = accounts[0];
    const seller = accounts[1];

    let instance;

    beforeEach(async () => {
        instance = await GeneratedContract.new();
    });

    it("should allow buyer to make a payment", async () => {
       
        const paymentAmount = web3.utils.toWei("1", "ether"); // 1 ETH
        await instance.pay({ from: buyer, value: paymentAmount });

 
        const state = await instance.getState();
        assert.equal(state, "Locked", "Payment did not update state correctly.");
    });

    it("should transfer payment to seller upon contract completion", async () => {
   
        const paymentAmount = web3.utils.toWei("1", "ether");
        await instance.pay({ from: buyer, value: paymentAmount });
        await instance.releasePayment({ from: buyer });


        const sellerBalance = await web3.eth.getBalance(seller);
        assert(sellerBalance > 0, "Seller did not receive the payment.");
    });

    it("should terminate contract if time exceeds deadline", async () => {

        await instance.setOracleTime(2000000000); // Mock future time
        await instance.terminateByOutOfDate({ from: buyer });

   
        const state = await instance.getState();
        assert.equal(state, "Inactive", "Contract termination logic failed.");
    });
});
