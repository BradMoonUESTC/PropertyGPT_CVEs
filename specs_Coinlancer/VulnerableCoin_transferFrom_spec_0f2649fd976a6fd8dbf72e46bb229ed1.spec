pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule BalanceAfterTransferFromEqualsSumOfDeductedFromSenderAndAddedToRecipient() {
    address $from;
    address $to;
    uint256 $amount;

    require($from != $to);
    
    uint256 balanceFromBefore = balances[$from];
    uint256 balanceToBefore = balances[$to];
    uint256 allowedBefore = allowed[$from][msg.sender];
    
    __assume__(transferFrom($from, $to, $amount) == true);
    
    assert(balances[$from] == balanceFromBefore - $amount);
    assert(balances[$to] == balanceToBefore + $amount);
    assert(allowed[$from][msg.sender] == allowedBefore - $amount);
}}