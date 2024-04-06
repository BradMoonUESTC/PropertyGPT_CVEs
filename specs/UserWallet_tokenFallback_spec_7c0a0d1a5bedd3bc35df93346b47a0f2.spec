pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;

function tokenFallback(address,uint256,bytes) public  {}

rule CheckTokenFallbackSignatureCorrect() {
    assert(keccak256(abi.encodePacked("tokenFallback(address,uint256,bytes)")) == 0xc0ee0b8a);
}}