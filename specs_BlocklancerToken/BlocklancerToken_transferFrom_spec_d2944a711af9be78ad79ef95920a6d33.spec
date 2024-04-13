pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function transferFrom(address,address,uint256) public returns(bool) {}

rule CheckTransferFromReducesAllowanceCorrectly() {
    address $from;
    address $to;
    uint256 $amount;

    __assume__($from != $to);
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);

    uint256 allowanceBefore = allowed[$from][msg.sender];
    transferFrom($from, $to, $amount);

    assert(allowed[$from][msg.sender] == allowanceBefore - $amount);
}}