pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;


rule testFallbackDoesNotAlterState() {
    address $targetAccount;
    uint256 $fundsToSend;
    
    // Attempt to capture the initial balance of the target account before sending Ether
    uint256 initialBalance = $targetAccount.balance;

    // Send Ether to the contract to trigger the fallback function
    payable($targetAccount).call{value: $fundsToSend}("");

    // Assert that the balance of the target account remains unchanged
    // Assuming the contract's fallback function does not change its state in a way that alters its balance
    assert($targetAccount.balance == initialBalance + $fundsToSend);
}}