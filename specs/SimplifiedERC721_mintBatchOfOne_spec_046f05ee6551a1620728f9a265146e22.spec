pragma solidity 0.8.0;

contract SimplifiedERC721 {mapping(uint256 => address) public _owners;
mapping(address => uint256) public _balances;
uint256 public _currentTokenId;

function balanceOf(address) public returns(uint256) {}
function mintBatchOfOne(address) public  {}

rule ensureMintBatchIncreasesTokenIdAndBalances() {
    address $to;
    uint256 tokenIdBefore = _currentTokenId;
    uint256 balanceBefore = balanceOf($to);

    mintBatchOfOne($to);

    assert(_currentTokenId == tokenIdBefore + 1);
    assert(balanceOf($to) == balanceBefore + 1);
}}