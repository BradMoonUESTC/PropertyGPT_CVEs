pragma solidity 0.6.12;

contract VulnerableWallet {address public owner;
mapping(address => address) private sweepers;

function sweep(address,uint256) public returns(bool) {}

rule VerifySweepFunctionWithDelegateCall() {
    address $sweeper;
    address $token;
    uint256 $amount;

    // Preset condition for the existence of a valid sweeper
    __assume__(sweepers[$token] == $sweeper);
    __assume__($sweeper != address(0));
    
    // Attempt to execute the sweep function via delegatecall
    (bool success, bytes memory returnedData) = $sweeper.delegatecall(abi.encodeWithSignature("sweep(address,uint256)", $token, $amount));

    // Asserting that the delegatecall successfully executed
    assert(success == true);

    // Verifying the delegatecall executes with the same input
    bool expectedSuccess;
    bytes memory expectedReturnedData;
    (expectedSuccess, expectedReturnedData) = $sweeper.delegatecall(abi.encodeWithSignature("sweep(address,uint256)", $token, $amount));

    // Ensuring that both attempts at delegatecall give consistent results
    assert(success == expectedSuccess);
}}