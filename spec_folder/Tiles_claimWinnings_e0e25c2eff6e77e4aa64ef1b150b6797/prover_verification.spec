pragma solidity 0.4.26;

contract Tiles {uint public constant NUM_TILES = 256;
uint constant SIDE_LENGTH = 16;
uint private constant STARTING_GAME_NUMBER = 1;
uint public DEFAULT_GAME_COST = 5000000000000000;
address private owner;
uint public currentGameNumber;
uint public currentGameBalance;
uint public numTilesClaimed;
Tile[16][16] public tiles;
bool public gameStopped;
uint public gameEarnings;
bool public willChangeCost;
uint public currentGameCost;
uint public nextGameCost;
mapping (address => uint) public pendingWithdrawals;
mapping (uint => address) public gameToWinner;
struct Tile {
        uint gameClaimed;
        address claimedBy;
    }

function claimWinnings() public  {}

rule SuccessfulWinningsClaim() {
    address $claimer;
    uint256 $init_pendingWithdrawals;
    pendingWithdrawals[$claimer] = $init_pendingWithdrawals;

    uint256 balanceBefore = address($claimer).balance;
    
    claimWinnings();

    if (pendingWithdrawals[$claimer] != 0) {
        assert(address($claimer).balance == balanceBefore);
    } else {
        assert(address($claimer).balance > balanceBefore);
    }
}}