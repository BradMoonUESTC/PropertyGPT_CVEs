pragma solidity 0.6.12;

contract Tiles{uint public constant NUM_TILES = 256;
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
function determineWinner() public   
precondition{gameStopped == false}

postcondition{tiles[getRightCoordinate(blockhash(block.number - 1)[31])][getLeftCoordinate(blockhash(block.number - 1)[31])].claimedBy != address(0)}
}