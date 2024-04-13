pragma solidity 0.6.12;

contract VirgoZodiacToken {address owner;
mapping(address => uint256) private balances;
mapping(address => mapping(address => uint256)) private allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromMaintainsTotalBalance() {
    address $from;
    address $to;
    uint256 $value;
    __assume__($to != 0x0000000000000000000000000000000000000001);

    uint256 totalBalanceBefore = balances[$from] + balances[$to];
    uint256 fromAllowanceBefore = allowed[$from][msg.sender];
    transferFrom($from, $to, $value);

    uint256 totalBalanceAfter = balances[$from] + balances[$to];
    uint256 fromAllowanceAfter = allowed[$from][msg.sender];

    assert(totalBalanceBefore == totalBalanceAfter);
    assert(fromAllowanceBefore >= fromAllowanceAfter);
}}