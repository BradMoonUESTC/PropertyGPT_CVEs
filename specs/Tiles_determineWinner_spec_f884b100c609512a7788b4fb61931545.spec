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

function getRightCoordinate(bytes1) public returns(uint256) {}
function getLeftCoordinate(bytes1) public returns(uint256) {}
function determineWinner() public  {}

rule ValidateWinnerConsistencyAfterDetermineWinner(){
    bytes32 winningHashBefore = blockhash(block.number - 1);
    bytes memory winningPairBefore = abi.encodePacked(winningHashBefore[31]);
    uint256 winningXBefore = getRightCoordinate(winningPairBefore[0]);
    uint256 winningYBefore = getLeftCoordinate(winningPairBefore[0]);
    address winnerBefore = tiles[winningXBefore][winningYBefore].claimedBy;

    determineWinner();

    bytes32 winningHashAfter = blockhash(block.number - 1);
    bytes memory winningPairAfter = abi.encodePacked(winningHashAfter[31]);
    uint256 winningXAfter = getRightCoordinate(winningPairAfter[0]);
    uint256 winningYAfter = getLeftCoordinate(winningPairAfter[0]);
    address winnerAfter = tiles[winningXAfter][winningYAfter].claimedBy;

    assert(winningHashBefore == winningHashAfter);
    assert(winningPairBefore[0] == winningPairAfter[0]);
    assert(winningXBefore == winningXAfter);
    assert(winningYBefore == winningYAfter);
    assert(winnerBefore == winnerAfter);
}}