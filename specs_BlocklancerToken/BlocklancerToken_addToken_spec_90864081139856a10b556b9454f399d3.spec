pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function addToken(address,uint256) public  {}

rule AddTokenValueConsistency() {
    address $investor; uint256 $value;
    uint256 totalTokensBefore = totalTokens;
    uint256 balanceBefore = balances[$investor];

    addToken($investor, $value);

    assert(totalTokens == totalTokensBefore + $value);
    assert(balances[$investor] == balanceBefore + $value);
}}