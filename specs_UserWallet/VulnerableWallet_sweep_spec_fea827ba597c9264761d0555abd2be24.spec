pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule ValidSweeperDelegateCallCheck() {
    address $sweeper;
    address $token;
    uint256 $amount;

    // Assumptions
    __assume__(sweepers[$token] == $sweeper);
    __assume__($sweeper != address(0));

    // Execute the sweep function which internally makes a delegatecall
    bool success_original = sweep($token, $amount);

    // Directly simulate the delegatecall to compare with the sweep function's behavior
    (bool success_delegate, ) = $sweeper.delegatecall(abi.encodeWithSignature("sweep(address,uint256)", $token, $amount));

    // Assert the outcome to ensure the delegatecall's success status matches the sweep function's return
    assert(success_original == success_delegate);
}}