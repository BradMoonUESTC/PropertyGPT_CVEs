pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromPreservesTotalBalance() {
    address $from; address $to; uint256 $amount;
    uint256 initialTotalBalance = balances[$from] + balances[$to];

    __assume__(allowed[$from][msg.sender] >= $amount);
    __assume__(balances[$from] >= $amount);
    __assume__($amount > 0);

    transferFrom($from, $to, $amount);

    uint256 finalTotalBalance = balances[$from] + balances[$to];
    assert(initialTotalBalance == finalTotalBalance);
}}