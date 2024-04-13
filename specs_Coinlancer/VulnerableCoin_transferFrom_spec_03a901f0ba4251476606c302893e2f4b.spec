pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromMaintainsTotalBalance() {
    address $from;
    address $to;
    uint256 $amount;

    __assume__($from != address(0));
    __assume__($to != address(0));
    __assume__($from != $to);

    uint256 totalBalanceBefore = balances[$from] + balances[$to];
    transferFrom($from, $to, $amount);
    uint256 totalBalanceAfter = balances[$from] + balances[$to];

    assert(totalBalanceBefore == totalBalanceAfter);
}}