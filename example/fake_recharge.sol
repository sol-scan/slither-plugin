pragma solidity ^0.4.24;

contract FakeCharge {
    uint256 public totalSupply;
    mapping(address => uint256) balances;

    function transfer(address to, uint256 value) public returns (bool) {
        // if (balances[msg.sender] >= value && value > 0) {
        //     balances[msg.sender] -= value;
        //     balances[to] += value;
        //     return true;
        // } else {
        //     return false;
        // }
        return _transfer(msg.sender, to, value);
    }

    function _transfer(address from, address to, uint256 value) private returns (bool) {
        if (balances[from] >= value && value > 0) {
            balances[from] -= value;
            balances[to] += value;
            return true;
        } else {
            return false;
        }
    }
}
