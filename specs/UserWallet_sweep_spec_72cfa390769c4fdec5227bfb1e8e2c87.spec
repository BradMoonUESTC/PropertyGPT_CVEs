pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet{AbstractSweeperList sweeperList;
function sweep(address,uint256) public returns(bool) 
precondition{}

postcondition{}
}