pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function testFunction() public  {}

rule OwnerCannotCallTestFunction() {
    __assume__(msg.sender == 0x0000000000000000000000000000000000000001);
    __assume__(owner != 0x0000000000000000000000000000000000000001);

    testFunction();
    assert(false); // If testFunction was called without reverting, this line should never be reached.
}}