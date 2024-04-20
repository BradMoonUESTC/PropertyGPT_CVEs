/**
 *Submitted for verification at Etherscan.io on 2017-11-15
*/

pragma solidity 0.6.12;

contract Owned {
    address public owner;

    function owned() public {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function transferOwnership(address newOwner) onlyOwner public {
        owner = newOwner;
    }
}