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

rule ValidateClaimFailureNoEffect() {
    address $claimant;
    uint256 $init_pendingWithdrawals = 0;
    pendingWithdrawals[$claimant] = $init_pendingWithdrawals;

    uint256 balanceBefore = $claimant.balance;
    claimWinnings();
    uint256 balanceAfter = $claimant.balance;

    assert(balanceBefore == balanceAfter && pendingWithdrawals[$claimant] == $init_pendingWithdrawals);
}}