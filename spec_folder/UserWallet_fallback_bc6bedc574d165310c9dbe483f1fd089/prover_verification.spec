pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;


rule ValidateFallbackPreservesBalance() {
    address $sender;
    uint256 $initialBalance = address(this).balance;

    // Simulating sending 1 ether to the contract without data to invoke the fallback function
    address(this).call{value: 1 ether}("");

    // After fallback function execution, verify that the contract's balance has increased by 1 ether
    assert(address(this).balance == $initialBalance + 1 ether);
}}