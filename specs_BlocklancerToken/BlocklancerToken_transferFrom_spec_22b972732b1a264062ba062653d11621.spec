pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromCorrectBalanceUpdate() {
    address $from;
    address $to;
    uint256 $amount;
    uint256 initialBalanceFrom = balances[$from];
    uint256 initialBalanceTo = balances[$to];
    uint256 initialAllowance = allowed[$from][msg.sender];

    __assume__(initialBalanceFrom >= $amount);
    __assume__(initialAllowance >= $amount);
    __assume__($amount > 0);

    transferFrom($from, $to, $amount);

    assert(balances[$from] == initialBalanceFrom - $amount);
    assert(balances[$to] == initialBalanceTo + $amount);
    assert(allowed[$from][msg.sender] == initialAllowance - $amount);
}}