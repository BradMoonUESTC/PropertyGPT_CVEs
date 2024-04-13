pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule DelegatecallSweeperIntegrity() {
    address $sweeper;
    address $token;
    uint256 $amount;

    // Establish initial conditions (including assuming that the sweeper is trusted/expected)
    sweepers[$token] = $sweeper;
    __assume__(sweepers[$token] != address(0)); // Assure sweeper is set and not a zero address
    __assume__($sweeper == 0x0000000000000000000000000000000000000001); // For simplicity, assuming sweeper is this specific address

    address initialSweeperState = sweepers[$token];

    // Perform the sweep assuming msg.sender satisfies certain conditions if needed
    __assume__(msg.sender == 0x0000000000000000000000000000000000000002); // Assume a specific sender if necessary
    sweep($token, $amount);

    // Assertions to check postconditions about the sweep function
    assert(initialSweeperState == sweepers[$token]); // Ensures sweeper address has not been maliciously changed
}}