pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function transferFrom(address,address,uint256) public returns(bool) {}

rule TransferFromRespectsAllowance() {
    address $from;
    address $to;
    uint256 $amount;
    uint256 allowedBefore = allowed[$from][msg.sender];
    __assume__(allowedBefore >= $amount);
    __assume__($to != address(0));

    transferFrom($from, $to, $amount);

    assert(allowed[$from][msg.sender] == allowedBefore - $amount);
}}