pragma solidity 0.4.26;

contract Tiles{uint public constant NUM_TILES = 256;
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
function resetGame(address) public   
precondition{}

postcondition{
    currentGameBalance == 0;
    gameToWinner[__old__(currentGameNumber)] != address(0);
    currentGameNumber == __old__(currentGameNumber) + 1;
    numTilesClaimed == 0;
    pendingWithdrawals[__old__(gameToWinner[__old__(currentGameNumber)])] == __old__(pendingWithdrawals[__old__(gameToWinner[__old__(currentGameNumber)])]) + (__old__(currentGameBalance) * 9 / 10);
    gameEarnings == __old__(gameEarnings) + (__old__(currentGameBalance) - (__old__(currentGameBalance) * 9 / 10));
    __old__(willChangeCost) ? (currentGameCost == nextGameCost) : (currentGameCost == __old__(currentGameCost));
    willChangeCost == false;
}
}