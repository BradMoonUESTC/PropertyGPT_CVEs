pragma solidity 0.6.12;

contract Tiles {

    uint public constant NUM_TILES = 256;
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

    event GameWon(uint indexed gameNumber, address indexed winner);
    event TileClaimed(uint indexed gameNumber, uint indexed xCoord, uint indexed yCoord, address claimedBy);
    event WinningsClaimed(address indexed claimedBy, uint indexed amountClaimed);
    event FailedToClaim(address indexed claimedBy, uint indexed amountToClaim);
    event PrintWinningInfo(bytes32 hash, uint xCoord, uint yCoord);

    constructor() public payable {
        owner = msg.sender;
        currentGameNumber = STARTING_GAME_NUMBER;
        currentGameCost = DEFAULT_GAME_COST;
        numTilesClaimed = 0;
        gameStopped = false;
        gameEarnings = 0;
        willChangeCost = false;
        nextGameCost = DEFAULT_GAME_COST;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier gameRunning() {
        require(!gameStopped, "Game is stopped");
        _;
    }

    modifier gameNotRunning() {
        require(gameStopped == true, "Game is not stopped");
        _;
    }

    function cancelContract() public onlyOwner returns (bool) {
        gameStopped = true;
        refundTiles();
        refundWinnings();
        return true;
    }

function getRightCoordinate(byte input) public pure returns(uint) {
    uint8 val = uint8(input) & 15; // Cast `byte` to `uint8` and then apply bitwise AND
    return uint(val); // `val` is already `uint8` which can be safely cast to `uint`
}

function getLeftCoordinate(byte input) public pure returns(uint) {
    uint8 val = uint8(input) >> 4; // Cast `byte` to `uint8` and then right shift
    return uint(val); // `val` is already `uint8` which can be safely cast to `uint`
}


    function determineWinner() private {
        bytes32 winningHash = blockhash(block.number - 1);
        byte winningPair = winningHash[31];
        uint256 winningX = getRightCoordinate(winningPair);
        uint256 winningY = getLeftCoordinate(winningPair);
        address winner = tiles[winningX][winningY].claimedBy;
        emit PrintWinningInfo(winningHash, winningX, winningY);
        emit GameWon(currentGameNumber, winner);
        resetGame(winner);
    }

    function claimTile(uint xCoord, uint yCoord, uint gameNumber) public gameRunning payable {
        if (gameNumber != currentGameNumber || tiles[xCoord][yCoord].gameClaimed == currentGameNumber) {
            revert("Tile already claimed this game or wrong game number");
        }
        require(msg.value == currentGameCost, "Incorrect value");

        currentGameBalance += msg.value;
        tiles[xCoord][yCoord] = Tile(currentGameNumber, msg.sender);
        emit TileClaimed(currentGameNumber, xCoord, yCoord, msg.sender);
        numTilesClaimed += 1;
        if (numTilesClaimed == NUM_TILES) {
            determineWinner();
        }
    }

    function resetGame(address winner) private {
        uint winningAmount = uint(currentGameBalance) * uint(9) / uint(10);
        uint remainder = currentGameBalance - winningAmount;
        currentGameBalance = 0;

        gameToWinner[currentGameNumber] = winner;
        currentGameNumber++;
        numTilesClaimed = 0;

        pendingWithdrawals[winner] += winningAmount;
        gameEarnings += remainder;

        if (willChangeCost) {
            currentGameCost = nextGameCost;
            willChangeCost = false;
        }
    }

    function refundTiles() private {
        Tile memory currTile;
        for (uint i = 0; i < SIDE_LENGTH; i++) {
            for (uint j = 0; j < SIDE_LENGTH; j++) {
                currTile = tiles[i][j];
                if (currTile.gameClaimed == currentGameNumber) {
                    address payable tileOwner = address(uint160(currTile.claimedBy));
                    if (tileOwner.send(currentGameCost)) {
                        tiles[i][j] = Tile(0, address(0));
                    }
                }
            }
        }
    }

    function refundWinnings() private {
        for (uint i = STARTING_GAME_NUMBER; i < currentGameNumber; i++) {
            address payable currAddress = address(uint160(gameToWinner[i]));
            uint currAmount = pendingWithdrawals[currAddress];
            if (currAmount != 0) {
                if (currAddress.send(currAmount)) {
                    pendingWithdrawals[currAddress] = 0;
                }
            }
        }
    }

    function claimWinnings() public {
        uint amount = pendingWithdrawals[msg.sender];
        if (amount != 0) {
            address payable sender = msg.sender;
            if (sender.send(amount)) {
                emit WinningsClaimed(sender, amount);
                pendingWithdrawals[sender] = 0;
            } else {
                emit FailedToClaim(sender, amount);
            }
        }
    }

    function updateGameCost(uint newGameCost) public onlyOwner returns (bool) {
        if (newGameCost > 0) {
            nextGameCost = newGameCost;
            willChangeCost = true;
            return true;
        }
        return false;
    }

    function claimOwnersEarnings() public onlyOwner {
        uint amount = gameEarnings;
        if (amount != 0) {
            owner.transfer(amount);
            gameEarnings = 0;
        }
    }
}
