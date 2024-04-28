pragma solidity ^0.8.12;

contract recordstore {

    /*uint256 supply;

    function get_supply() public view returns (uint256) {
        return supply;
    }*/

    struct Data{
        string sector;
        uint256 supply;
        uint256 demand;
        uint256 temp;
    }

    Data public data_struct;

    function set_data(string memory _sector,
    uint256 _supply , 
    uint256 _demnad, 
    uint256 _temp) 
    public {
        data_struct = Data(_sector,_supply,_demnad,_temp);
    }

    /*function update_supply(uint256 _supply) public returns (uint256){
        supply = _supply;
        return supply;
    }*/

    function print_data() public view returns (string memory,
    uint256,
    uint256,
    uint256) {
        return (data_struct.sector,
        data_struct.supply,
        data_struct.demand,
        data_struct.temp);
    }

    function update_data(string memory _sector,
    uint256 _supply,
    uint256 _demand,
    uint256 _temp) public {
        data_struct.sector = _sector;
        data_struct.supply = _supply;
        data_struct.demand = _demand;
        data_struct.temp = _temp;
    }

    function update_supp(uint256 _supply) public{
        data_struct.supply = _supply;
    }

    function update_sector(string memory _sector) public{
        data_struct.sector = _sector;
    }
    
    function update_demand(uint256 _demand) public{
        data_struct.demand = _demand;
    }
    
    function update_temperature(uint256 _temperature) public{
        data_struct.temp = _temperature;
    }

    function get_sector() public view returns(string memory) {
        return data_struct.sector;
    }

    function get_supply() public view returns(uint256) {
        return data_struct.supply;
    }

    function get_demand() public view returns(uint256) {
        return data_struct.demand;
    }

    function get_temp() public view returns(uint256) {
        return data_struct.temp;
    }

}