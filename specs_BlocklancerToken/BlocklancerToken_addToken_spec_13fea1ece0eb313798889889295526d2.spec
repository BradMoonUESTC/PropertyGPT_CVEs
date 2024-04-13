pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function addToken(address,uint256) public  {}

rule AddTokenAdjustsBalancesCorrectly() {
    address $investor;
    uint256 $add_amount;
    uint256 balanceBefore = balances[$investor];
    uint256 totalTokensBefore = totalTokens;
    
    addToken($investor, $add_amount);

    assert(balances[$investor] == balanceBefore + $add_amount);
    assert(totalTokens == totalTokensBefore + $add_amount);
}}