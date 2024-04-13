pragma solidity 0.6.12;

contract BlocklancerToken {string public name = "Lancer Token";
string public symbol = "LNC";
uint8 public decimals = 18;
mapping(address => uint256) public balances;
mapping(address => mapping (address => uint256)) public allowed;
uint256 totalTokens;

function addToken(address,uint256) public  {}

rule validateAddTokenFunctionality() {
    address $addrInvestor;
    uint256 $amountToAdd;

    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);

    uint256 initialBalanceInvestor = balances[$addrInvestor];
    uint256 initialTotalSupply = totalTokens;

    addToken($addrInvestor, $amountToAdd);

    assert(balances[$addrInvestor] == initialBalanceInvestor + $amountToAdd);
    assert(totalTokens == initialTotalSupply + $amountToAdd);
}}