pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;

function sweep(address,uint256) public returns(bool) {}

rule DelegatecallEffectiveness(){
    address $token;
    uint256 $amount;

    // Attempt to call sweep function
    bool success = sweep($token, $amount);
    
    // Verify delegatecall's success state
    assert(success == true);
}}