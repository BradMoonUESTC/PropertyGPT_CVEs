pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromBalanceAndAllowanceConsistency() {
    address $from;
    address $to;
    uint256 $amount;

    // Adjust assumptions using Ethereum addresses directly
    __assume__(msg.sender == 0x0000000000000000000000000000000000000003);
    __assume__($from != 0x0000000000000000000000000000000000000001);
    __assume__($to != 0x0000000000000000000000000000000000000002);

    uint256 balanceFromBefore = balances[$from];
    uint256 balanceToBefore = balances[$to];
    uint256 allowedFromBefore = allowed[$from][msg.sender];

    transferFrom($from, $to, $amount);

    if ($from != $to) {
        assert(balances[$from] == balanceFromBefore - $amount);
        assert(balances[$to] == balanceToBefore + $amount);
    } else {
        assert(balances[$from] == balanceFromBefore); // Since from and to are the same, balance should not change
    }
    assert(allowed[$from][msg.sender] == allowedFromBefore - $amount);
}}