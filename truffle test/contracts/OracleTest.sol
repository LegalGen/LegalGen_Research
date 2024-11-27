// SPDX-License-Identifier: GPL-3.0
pragma solidity 0.8.20;

contract OracleTest {
    uint256 private time = block.timestamp;
    uint256 private price = 100; // 
    bool private conditionState = true;

    function getTime() external view returns (uint256) {
        return time;
    }

    function getPrice() external view returns (uint256) {
        return price;
    }

    function getConditionState() external view returns (bool) {
        return conditionState;
    }

    function setTime(uint256 _time) external {
        time = _time;
    }

    function setPrice(uint256 _price) external {
        price = _price;
    }

    function setConditionState(bool _state) external {
        conditionState = _state;
    }
}
