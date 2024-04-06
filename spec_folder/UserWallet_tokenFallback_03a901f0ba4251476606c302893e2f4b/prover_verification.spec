pragma solidity 0.4.26;
interface AbstractSweeperList {
    function sweeperOf(address _token) external returns (address);
}

contract UserWallet {AbstractSweeperList sweeperList;

function tokenFallback(address,uint256,bytes) public  {}

rule VerifyTokenFallbackExecution(){
    address $senderAddress;
    address $fromAddress;
    uint256 $valueAmount;
    bytes memory $dataContent = ""; // Properly declared with the memory location

    // Attempting to call tokenFallback function with corrected encoding for bytes parameter
    (bool success, ) = $senderAddress.call(
       abi.encodeWithSignature("tokenFallback(address,uint256,bytes memory)", $fromAddress, $valueAmount, $dataContent)
    );
   
    // Checking the success status of the call without specifying an error message
    success == true;
}}