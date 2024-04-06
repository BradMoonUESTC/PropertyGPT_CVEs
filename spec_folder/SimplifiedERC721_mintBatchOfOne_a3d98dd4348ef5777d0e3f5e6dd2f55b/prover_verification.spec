pragma solidity 0.8.0;

contract SimplifiedERC721 {mapping(uint256 => address) public _owners;
mapping(address => uint256) public _balances;
uint256 public _currentTokenId;

function mintBatchOfOne(address) public  {}

rule VerifySingleMintIncrement() {
    address $to;
    uint256 $tokenIdBeforeMint;
    uint256 $currentTokenId = $tokenIdBeforeMint;
    _currentTokenId = $currentTokenId;
    
    mintBatchOfOne($to);

    assert(_currentTokenId == $currentTokenId + 1);
}}