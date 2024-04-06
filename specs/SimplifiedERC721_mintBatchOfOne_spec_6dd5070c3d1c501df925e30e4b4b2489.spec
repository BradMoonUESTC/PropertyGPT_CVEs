pragma solidity 0.8.0;

contract SimplifiedERC721 {mapping(uint256 => address) public _owners;
mapping(address => uint256) public _balances;
uint256 public _currentTokenId;

function mintBatchOfOne(address) public  {}

rule VerifySingleBatchMintIncrementsTokenId() {
    uint256 $tokenIdBefore = _currentTokenId;
    address $to;
    
    mintBatchOfOne($to);

    assert(_currentTokenId == $tokenIdBefore + 1);
}}