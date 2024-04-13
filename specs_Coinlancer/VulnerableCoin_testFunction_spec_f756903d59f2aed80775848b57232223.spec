pragma solidity 0.6.12;

contract VulnerableCoin {string public constant symbol = "VULN";
string public constant name = "VulnerableCoin";
uint8 public constant decimals = 18;
uint256 private _totalSupply = 300 * 10**6 * 10**18;
address public owner;
mapping(address => uint256) balances;
mapping(address => mapping(address => uint256)) allowed;

function testFunction() public  {}

rule TestFunctionAssumptionOwnership() {
    // Setting up the scenario
    address $caller;

    // Assuming the caller is NOT the owner, this should trigger the require in the function
    __assume__($caller != 0x0000000000000000000000000000000000000001);

    // Assuming different potential owner address to test assume scenario
    __assume__(msg.sender == $caller);

    testFunction();

    // If the testFunction logic is triggered without reverting, assumption is validated
    assert(msg.sender != owner);
}}