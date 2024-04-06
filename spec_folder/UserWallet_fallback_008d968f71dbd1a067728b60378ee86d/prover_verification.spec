pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;


rule fallbackFunctionShouldNotChangeBalance() {
    uint256 balanceBefore = address(this).balance;
    (bool success, ) = address(this).call{value: 1 ether}("");
    assert(success);
    assert(balanceBefore + 1 ether == address(this).balance);
}}