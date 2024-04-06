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

function resetGame(address) public  {}

rule ResetGameUpdatesWinnerAndGameNumberCorrectly() {
    address $winner;
    uint256 $currentGameNumberBefore = currentGameNumber;

    resetGame($winner);

    assert(gameToWinner[$currentGameNumberBefore] == $winner);
    assert(currentGameNumber == $currentGameNumberBefore + 1);
}}