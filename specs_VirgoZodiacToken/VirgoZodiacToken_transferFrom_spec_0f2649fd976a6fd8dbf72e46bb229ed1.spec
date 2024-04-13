pragma solidity 0.6.12;

contract VirgoZodiacToken {address owner;
mapping(address => uint256) private balances;
mapping(address => mapping(address => uint256)) private allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromDoesNotChangeBalanceSum() {
    address $from;
    address $to;
    uint256 $value;

    __assume__($from != $to);
    __assume__($value > 0);
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);

    uint256 balanceSumBefore = balances[$from] + balances[$to];

    // Assume the call to transferFrom is successful
    transferFrom($from, $to, $value);

    uint256 balanceSumAfter = balances[$from] + balances[$to];

    // Check that the sum of the balances before and after the transferFrom remains equal
    assert(balanceSumBefore == balanceSumAfter);
}}