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

function claimTile(uint256,uint256,uint256) public  {}

rule ClaimTileRespectsGameNumberAndTileUniqueness() {
    uint256 $xCoord;
    uint256 $yCoord;
    uint256 $gameNumber;

    uint256 currentGameNumber = $gameNumber;
    uint256 gameClaimedBefore = tiles[$xCoord][$yCoord].gameClaimed;
    
    claimTile($xCoord, $yCoord, $gameNumber);

    if($gameNumber != currentGameNumber || gameClaimedBefore == currentGameNumber) {
        assert(false); // Expecting revert if conditions met, so assertion fails if claimTile proceeds.
    } else {
        uint256 gameClaimedAfter = tiles[$xCoord][$yCoord].gameClaimed;
        assert(gameClaimedAfter == currentGameNumber);
    }
}}