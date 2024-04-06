pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;


rule ensureFallbackPreservesBalanceCorrectly(){
    uint256 balanceBefore = address(this).balance;
    // Simulate the fallback function by sending ether directly to the contract
    (bool success, ) = address(this).call{value: 1 ether}("");
    assert(success);
    uint256 balanceAfter = address(this).balance;
    // Ensuring that the balance after receiving ether through fallback function
    // is exactly 1 ether more than the balance before. 
    assert(balanceBefore + 1 ether == balanceAfter);
}}