pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function addToken(address,uint256) public  {}

rule AddTokenUpdatesBalancesAndTotalTokens() {
    address $investor;
    uint256 $value;

    uint256 balanceBefore = balances[$investor];
    uint256 totalTokensBefore = totalTokens;
    addToken($investor, $value);

    // Check if investor's balance is correctly updated
    assert(balances[$investor] == (balanceBefore + $value));
    // Check if totalTokens is correctly updated
    assert(totalTokens == (totalTokensBefore + $value));
}}