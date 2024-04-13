pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function testFunction() public  {}

rule CallerNotOwnerConstraint() {
    address $caller;
    address $owner = 0x0000000000000000000000000000000000000001;

    __assume__(msg.sender == $caller);

    require(msg.sender != $owner);
    testFunction();

    assert(msg.sender != owner);
}}