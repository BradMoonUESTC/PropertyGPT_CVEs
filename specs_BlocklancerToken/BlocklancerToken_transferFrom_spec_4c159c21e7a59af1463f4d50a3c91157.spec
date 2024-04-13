pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function transferFrom(address,address,uint256) public returns(bool) {}
function balanceOf(address) public returns(uint256) {}

rule ValidateTransferFromPreconditions() {
    address $from;
    address $to;
    uint256 $amount;
    
    __assume__(balanceOf($from) >= $amount);
    __assume__(allowed[$from][msg.sender] >= $amount);
    __assume__($amount > 0 && balanceOf($to) + $amount > balanceOf($to));
    
    uint256 balanceBeforeFrom = balanceOf($from);
    uint256 allowanceBefore = allowed[$from][msg.sender];
    uint256 balanceBeforeTo = balanceOf($to);

    transferFrom($from, $to, $amount);

    assert(balanceOf($from) == balanceBeforeFrom - $amount);
    assert(allowed[$from][msg.sender] == allowanceBefore - $amount);
    assert(balanceOf($to) == balanceBeforeTo + $amount);
}}