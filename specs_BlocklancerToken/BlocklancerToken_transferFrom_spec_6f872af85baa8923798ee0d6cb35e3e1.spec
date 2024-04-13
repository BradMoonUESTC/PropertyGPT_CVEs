pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function transferFrom(address,address,uint256) public returns(bool) {}

rule ValidateTransferFromEffectiveness() {
    address $from;
    address $to;
    uint256 $amount;
    uint256 initialFromBalance = balances[$from];
    uint256 initialToBalance = balances[$to];
    uint256 allowedBefore = allowed[$from][msg.sender];

    // Assume the method caller is authorized and has enough allowance, and the transfer amount is valid
    __assume__(allowed[$from][msg.sender] >= $amount);
    __assume__(balances[$from] >= $amount);
    __assume__($amount > 0 && (initialToBalance + $amount > initialToBalance));

    transferFrom($from, $to, $amount);

    assert(balances[$from] == initialFromBalance - $amount); // Verify sender's balance is reduced correctly
    assert(balances[$to] == initialToBalance + $amount); // Verify recipient's balance is increased correctly
    assert(allowed[$from][msg.sender] == allowedBefore - $amount); // Verify the allowance is reduced correctly
}}