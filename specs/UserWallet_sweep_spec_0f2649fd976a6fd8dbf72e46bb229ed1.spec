pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;

function sweep(address,uint256) public returns(bool) {}

rule EnsureDelegateCallMaintainsBalance() {
    address $token;
    uint256 $amount;
    uint256 balanceBefore = address(this).balance;

    sweep($token, $amount);

    assert(balanceBefore == address(this).balance);
}}