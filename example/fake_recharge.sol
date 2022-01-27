pragma solidity ^0.4.24;

contract FakeCharge {
    uint256 public totalSupply;
    mapping(address => uint256) balances;

    function transfer(address _to, uint256 _value) public returns (bool) {
        if (balances[msg.sender] >= _value && _value > 0) {
            balances[msg.sender] -= _value;
            balances[_to] += _value;
            return true;
        } else {
            return false;
        }
    }
}
