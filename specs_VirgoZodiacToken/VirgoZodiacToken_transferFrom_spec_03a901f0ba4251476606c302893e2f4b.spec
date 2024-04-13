pragma solidity 0.6.12;

contract VirgoZodiacToken {address owner;
mapping(address => uint256) private balances;
mapping(address => mapping(address => uint256)) private allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromMaintainsTotalBalance() {
    address $from;
    address $to;
    uint256 $value;

    __assume__(msg.sender == $from || allowed[$from][msg.sender] >= $value);

    uint256 totalBalanceBefore = balances[$from] + balances[$to];
    transferFrom($from, $to, $value);

    if ($from != $to) {
        assert((balances[$from] + balances[$to]) == totalBalanceBefore);
    } else {
        // In case $from and $to are the same, the balance might only decrease due to fees not considered in this scenario
        assert((balances[$from] + balances[$to]) <= totalBalanceBefore);
    }
}}