// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.20;

// A Stock Purchase Contract template
import "./OracleTest.sol";

contract g_rs {

    address payable public seller;
    address payable[] public buyer;

    OracleTest internal oracle;

    string public sellerName;
    string[] public buyerName;

    uint256 public EffectiveTime;
    uint256 public CloseTime;
    uint256 public OutSideClosingDate;

    uint256[] public pricePayedByBuyer;  // 改为动态数组
    bool[] public purchaseSellerConfirmed;  // 改为动态数组
    bool[] public purchaseBuyerConfirmed;  // 改为动态数组

    mapping(string => uint32) private fileHashMap;

    bool[] public terminateSellerConfirmed;  // 改为动态数组
    bool[] public terminateBuyerConfirmed;  // 改为动态数组

    enum State { Created, Locked, Release, Transferred, Inactive }
    State[] public state;  // 改为动态数组

    event Payed(uint256 paymentIndex);
    event Released(uint256 paymentIndex);
    event Terminated(uint256 buyerIndex);
    event TerminatedByOutOfDate();
    event Closed();

    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() payable {
        owner = msg.sender;
        sellerName = "BANK OF AMERICA, N.A.";
        buyerName = ["KAISER ALUMINUM & CHEMICAL CORPORATION"];
        seller = payable(address(0));
        buyer = [payable(address(0))];

        EffectiveTime = 1138233600; 
        CloseTime = 1000; 
        OutSideClosingDate = 1000; 

        state.push(State.Created);  // 初始化状态
        pricePayedByBuyer.push(0);  // 初始化买方支付金额
        purchaseSellerConfirmed.push(false);  // 初始化卖方确认
        purchaseBuyerConfirmed.push(false);  // 初始化买方确认
        terminateSellerConfirmed.push(false);  // 初始化卖方终止确认
        terminateBuyerConfirmed.push(false);  // 初始化买方终止确认
    }

    function pay_0() public payable {
        require(state[0] == State.Created || state[0] == State.Locked, "Invalid state");
        require(msg.sender == buyer[0], "Only buyer can pay");

        uint256 currentTime = oracle.getTime();
        require(currentTime <= CloseTime, "Time later than Close time");

        uint256 currentPrice = oracle.getPrice();
        uint256 price = 30000000 / currentPrice; 

        require(msg.value == price, "Incorrect payment amount");

        emit Payed(0);

        pricePayedByBuyer[0] += price;

        state[0] = State.Locked;
    }

    function purchaseConfirm(uint256 buyerIndex) public {
        require(buyerIndex < buyer.length, "Invalid buyer index");

        if (msg.sender == seller) {
            purchaseSellerConfirmed[buyerIndex] = true;
        } else {
            for (uint256 i = 0; i < buyerName.length; i++) {
                if (msg.sender == buyer[i]) {
                    purchaseBuyerConfirmed[i] = true;
                    return;
                }
            }
            revert("Caller not authorized");
        }
    }

    function payRelease_0() public {
        require(msg.sender == buyer[0], "Only buyer can release payment");

        uint256 currentTime = oracle.getTime();
        require(currentTime <= CloseTime, "Time later than Close time");

        require(purchaseBuyerConfirmed[0], "Buyer has not confirmed purchase");
        require(purchaseSellerConfirmed[0], "Seller has not confirmed purchase");

        emit Released(0);

        state[0] = State.Release;

        seller.transfer(pricePayedByBuyer[0]);

        pricePayedByBuyer[0] = 0;
    }

    function uploadFileHash(string memory fileName, uint32 hashCode) public {
        require(isAuthorized(msg.sender), "Caller not authorized");

        fileHashMap[fileName] = hashCode;
    }

    function terminateByTransfer(uint256 buyerIndex) public {
        require(isAuthorized(msg.sender), "Caller not authorized");

        uint256 currentTime = oracle.getTime();
        require(currentTime <= CloseTime, "Time later than Close time");

        require(terminateSellerConfirmed[buyerIndex], "Seller has not confirmed termination");
        require(terminateBuyerConfirmed[buyerIndex], "Buyer has not confirmed termination");

        emit Terminated(buyerIndex);

        state[buyerIndex] = State.Inactive;

        buyer[buyerIndex].transfer(pricePayedByBuyer[buyerIndex]);
    }

    function terminateByOutOfDate() public {
        uint256 currentTime = oracle.getTime();
        require(currentTime >= OutSideClosingDate, "Outside closing date not reached");

        emit TerminatedByOutOfDate();

        for (uint256 i = 0; i < buyerName.length; i++) {
            state[i] = State.Inactive;
            buyer[i].transfer(pricePayedByBuyer[i]);
        }
    }

    function close() public {
        uint256 currentTime = oracle.getTime();
        require(currentTime <= CloseTime, "Time later than Close time");

        emit Closed();

        for (uint256 i = 0; i < buyerName.length; i++) {
            state[i] = State.Inactive;
        }
    }

    function setOracleAddress(address addr) public onlyOwner {
        oracle = OracleTest(addr);
    }

    function setSellerAddress(address payable addr) public onlyOwner {
        seller = addr;
    }

    function setBuyerAddress(address payable[] memory addrs) public onlyOwner {
        buyer = addrs;
    }

    function setAllState(State s) public {
        for (uint256 i = 0; i < buyerName.length; i++) {
            state[i] = s;
        }
    }

    function getFileHash(string memory fileName) public view returns (uint32) {
        return fileHashMap[fileName];
    }

    function isAuthorized(address caller) internal view returns (bool) {
        if (caller == seller) {
            return true;
        }
        for (uint256 i = 0; i < buyer.length; i++) {
            if (caller == buyer[i]) {
                return true;
            }
        }
        return false;
    }
}
