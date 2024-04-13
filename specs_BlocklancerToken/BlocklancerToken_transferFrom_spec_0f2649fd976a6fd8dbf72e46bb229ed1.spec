pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromBalanceConsistency() {
    address $from;
    address $to;
    uint256 $amount;
    uint256 $balanceFromBefore = balances[$from];
    uint256 $balanceToBefore = balances[$to];
    uint256 $allowanceBefore = allowed[$from][msg.sender];

    __assume__($amount > 0);
    __assume__(balances[$from] >= $amount);
    __assume__(allowed[$from][msg.sender] >= $amount);
    
    transferFrom($from, $to, $amount);
    
    assert(balances[$from] == $balanceFromBefore - $amount);
    assert(balances[$to] == $balanceToBefore + $amount);
    assert(allowed[$from][msg.sender] == $allowanceBefore - $amount);
}}