pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromBalanceConsistency() {
    address $from;
    address $to;
    uint256 $amount;
    uint256 initFromBalance = balances[$from];
    uint256 initToBalance = balances[$to];

    __assume__(allowed[$from][msg.sender] >= $amount);
    __assume__(balances[$from] >= $amount);
    __assume__($to != address(0));

    transferFrom($from, $to, $amount);

    assert(balances[$from] == initFromBalance - $amount);
    assert(balances[$to] == initToBalance + $amount);
}}