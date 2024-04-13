pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function addToken(address,uint256) public  {}

rule addTokenIncreasesBalanceAndTotalTokens() {
    address $invest;
    uint256 $value;
    uint256 initialBalance = balances[$invest];
    uint256 initialTotalTokens = totalTokens;
    
    addToken($invest, $value);

    assert(balances[$invest] == initialBalance + $value);
    assert(totalTokens == initialTotalTokens + $value);
}}