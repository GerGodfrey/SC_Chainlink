//SPDX-License_Identifier: MIT

pragma solidity ^0.8.7;

contract SaveNumber{

  uint256 public numero; // se crea automaticamente un get 

  function SetNumber(uint256 _numero) public{
    numero = _numero;
  }
  
}