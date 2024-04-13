pragma solidity 0.6.12;

contract Tiles {uint public constant NUM_TILES = 256;
uint constant SIDE_LENGTH = 16;
uint private constant STARTING_GAME_NUMBER = 1;
uint public DEFAULT_GAME_COST = 5000000000000000;
address payable private owner;
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

function claimTile(uint256,uint256,uint256) public  {}

rule ClaimTileGameNotManipulated() {
    uint $xCoord;
    uint $yCoord;
    uint $gameNumber;
    uint256 $msgValue;
    uint256 currentGameCostBefore = currentGameCost;
    uint currentGameNumberBefore = currentGameNumber;
    uint currentGameBalanceBefore = currentGameBalance;
    uint numTilesClaimedBefore = numTilesClaimed;

    __assume__($gameNumber == currentGameNumberBefore);
    __assume__($msgValue == currentGameCostBefore);

    claimTile($xCoord, $yCoord, $gameNumber);

    assert(currentGameBalance == currentGameBalanceBefore + $msgValue);
    assert(numTilesClaimed == numTilesClaimedBefore + 1);
}}