pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;


rule EnsureFallbackDoesNotChangeBalanceUnnecessarily() {
    address $anyAddress;
    uint256 balanceBefore = address(this).balance;
    (bool success,) = address(this).call{value: 1 ether}("");
    uint256 balanceAfter = address(this).balance;

    assert(success && (balanceBefore + 1 ether == balanceAfter));
}}