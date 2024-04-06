pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;

function sweep(address,uint256) public returns(bool) {}

rule EnsureDelegateCallConsistencyBeforeAndAfterSweep() {
    address $token;
    uint256 $amount;
    bytes memory sweepData = abi.encodeWithSignature("sweep(address,uint256)", $token, $amount);

    // Attempt to make a delegate call before the actual sweep function is called
    (bool successBefore,) = address(sweeperList.sweeperOf($token)).delegatecall(sweepData);

    // Call the sweep function which internally makes another delegate call
    sweep($token, $amount);

    // Attempt to make a delegate call after the sweep function is called with the same data
    (bool successAfter,) = address(sweeperList.sweeperOf($token)).delegatecall(sweepData);

    // Ensure the success of delegate calls before and after are consistent 
    assert(successBefore == successAfter);
}}