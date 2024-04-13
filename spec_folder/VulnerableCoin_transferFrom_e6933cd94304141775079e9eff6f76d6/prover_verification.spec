pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromCorrectness() {
    address $from;
    address $to;
    uint256 $amount;
    uint256 $otherAmount;

    __assume__($from != $to);
    __assume__($to != address(0));

    uint256 fromBalanceBefore = balances[$from];
    uint256 toBalanceBefore = balances[$to];
    uint256 allowedBefore = allowed[$from][msg.sender];

    transferFrom($from, $to, $amount);

    assert(fromBalanceBefore - $amount == balances[$from]);
    assert(toBalanceBefore + $amount == balances[$to]);
    assert(allowedBefore - $amount == allowed[$from][msg.sender]);
}}