// SPDX-License-Identifier: MIT
pragma solidity 0.6.12;

contract VirgoZodiacToken {
    address owner;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowed;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor() public {
        owner = msg.sender;
    }

    // This is the original transferFrom function without any modifications.
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {

        if (_value == 0) return false;

        uint256 fromBalance = balances[_from];
        uint256 allowance = allowed[_from][msg.sender];

        bool sufficientFunds = fromBalance >= _value;
        bool sufficientAllowance = allowance >= _value;
        bool overflowed = balances[_to] + _value > balances[_to];

        if (sufficientFunds && sufficientAllowance && !overflowed) {
            balances[_from] = fromBalance - _value;
            balances[_to] += _value;
            allowed[_from][msg.sender] = allowance - _value;

            emit Transfer(_from, _to, _value);
            return true;
        } else {
            return false;
        }
    }
}
