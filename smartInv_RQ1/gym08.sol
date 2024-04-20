// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

contract VulnerableDepositContract {
    mapping(address => uint256) public deposits;

    function depositFromOtherContract(
        uint256 _depositAmount,
        address _forAddress
    ) external {
        deposits[_forAddress] += _depositAmount;
    }

    function getDeposit(address _address) public view returns (uint256) {
        return deposits[_address];
    }
}
