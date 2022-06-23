//Begin
// SPDX-License-Identifier: MIT
pragma solidity 0.8.13;
// Array
 
contract RegisterAccess {
    string[] private info;
    address public owner;
    mapping (address => bool) public whiteList;
 
    constructor() {
        // msg.sender : billetera que manda la transacción
        owner = msg.sender;
        whiteList[msg.sender] = true;
    }
 
    // esto no es grabado en la block pero es una información externa que nos ayuda a monitorear las 
    // trx, un archivo en javascript y cada vez que un SC hace un movimiento 
    event InfoChange(string oldInfo, string newInfo);
   
   // sirve para ser agregado a las fuunciones , hago de una manera más clara más limpia 
    modifier onlyOwner {
        require(msg.sender == owner,"Only owner");
        _;
    }
 
    modifier onlyWhitelist {
        require(whiteList[msg.sender] == true, "Only whitelist");
        _;
    }
 
    // tienes que pasar al parametro la info que quieres consultar .... 
    function getInfo(uint index) public view returns (string memory) {
        return info[index];
    }
 
    function setInfo(uint index, string memory _info) public onlyWhitelist {
               emit InfoChange (info[index], _info);
        info[index] = _info;
    }
   
    function addInfo(string memory _info) public onlyWhitelist returns (uint index) {
        info.push (_info);//agregamos la infor 
        index = info.length -1; //retornamos el tamaño de la información 
    }
     
    //listar toda la iinfo que está en nuestra lista 
    function listInfo() public view returns (string[] memory) {
        return info;
    }
 
    function addMember (address _member) public onlyOwner {
        whiteList[_member] = true;
    }
   
    function delMember (address _member) public onlyOwner {
        whiteList[_member] = false;
    }    
}
 
//End
