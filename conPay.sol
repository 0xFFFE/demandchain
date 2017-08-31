pragma solidity ^0.4.16;

contract conPay {
    /* Define variable consumer of the type address */
    address public scOwnerAddress = 0x495169d940EA7499649fe6dD51C5d2D850A8A3E9;
    address public gridAddress;
    address public consumerAddress;
    uint public time;
    uint public energy;
    uint public refund;
    uint scWallet;
    /* This function is executed at initialization */
    function conPay(address gA, address cA, address scA) {
        gridAddress = gA;
        consumerAddress = cA;
        /* only scOwner can change scOwnerAddress */
        if (msg.sender == scOwnerAddress) {
            scOwnerAddress = scA;
        }
    }
    /* Fallback function is executed when someone send Ethers to the contract
    without providing any data or calling a function; thanks for the Ether */
    function () payable {
        scWallet += msg.value;
    }
    /* This function  */
    function conPay1(uint256 t, uint256 e) {
        consumerAddress = msg.sender;
        time = t;
        energy = e;
        refund = calcRefund(time, energy);
    }
    /* Function set grid address only by SC owner */
    function setGridAddress (address a) {
        if (msg.sender == scOwnerAddress) {
            gridAddress = a;
        }
    }
    /* Function set consumer address only by SC owner */
    function setConsumerAddress (address a) {
        if (msg.sender == scOwnerAddress) {
            consumerAddress = a;
        }
    }
    /* Function set sc owner address only by SC owner */
    function setScOwnerAddress (address a) {
        if (msg.sender == scOwnerAddress) {
            scOwnerAddress = a;
        }
    }
    /* Function to calculate refund for customer based on energy database of grid */
    function calcRefund(uint t, uint e) returns (uint refundSum) {
        uint cashPerWs = getRefundRate();
        refundSum = t * e * cashPerWs;
        return refundSum;
    }
    /* Read cash per WS rate from grid database */
    function getRefundRate() returns (uint rate) {
        return 1;
    }
    /**/
    function getGridConfirmation() returns (bool confirmation) {
        /* business logic ?? */
        return true;
    }
    /* Function to pay for energy reduction */
    function payCustomer (address target, uint balance) payable {
        if (gridAddress.balance >= balance) {
            target.transfer(balance);
        }
    }
/*
    function pay(address receiver) payable returns(bool success) {
      uint paid = msg.value;
      balance[msg.sender] += paid;
      return true;
    }
*/
/*
    function claimFromGrid() returns(bool success) {
      if (gridWallet==0) throw;
      msg.sender.transfer(refund);
      return true;
    }
*/
/*
    function kill() {
        if (msg.sender == gridAddress) selfdestruct(consumerAddress);
    }
*/
}
