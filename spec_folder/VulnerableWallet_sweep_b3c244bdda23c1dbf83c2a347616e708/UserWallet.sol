// SPDX-License-Identifier: MIT
pragma solidity 0.6.12;

/**
 * Simplified version of the UserWallet and Controller contracts with a delegatecall vulnerability.
 */
contract VulnerableWallet {
    address public owner;
    mapping(address => address) private sweepers;

    event LogSweep(address indexed from, address indexed to, address indexed token, uint amount);

    constructor() public {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Function to add or update the sweeper address for a specific token
    function addSweeper(address _token, address _sweeper) public onlyOwner {
        sweepers[_token] = _sweeper;
    }

    // This function calls the sweeper associated with the token using delegatecall
    function sweep(address _token, uint _amount) public returns (bool) {
        address sweeper = sweepers[_token];
        require(sweeper != address(0), "Sweeper not found for token");

        // delegatecall to the sweeper, which may lead to state changes if the sweeper is malicious
        (bool success, ) = sweeper.delegatecall(abi.encodeWithSignature("sweep(address,uint256)", _token, _amount));
        require(success, "Sweep failed");

        emit LogSweep(address(this), msg.sender, _token, _amount);
        return true;
    }

    // Function to change the owner of the contract
    function changeOwner(address _newOwner) public onlyOwner {
        owner = _newOwner;
    }

    // Allow the contract to receive Ether
    receive() external payable {}
}
