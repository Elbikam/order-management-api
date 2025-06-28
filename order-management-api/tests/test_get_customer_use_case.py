from unittest import mock
from main import get_info
from  use_cases.get_customer_info_use_Case import GetCustomerInfoUseCase
from interfaces.services import GetCustomerRepository,GetInfo
from data_base import CustomerDB
from interfaces.repositores import CreateCustomerRepository
from data_base import CustomerDB

def test_get_info(customer_id=1):
    m = CustomerDB()
    m.execute = mock.Mock()
    m.execute.return_value = {"id":customer_id,
                    "name":"boubaker","phone":"0663366915","balance":100}
    
    n = GetInfo(m)
    result = n.get_info(customer_id=1)
    assert result == {"id":customer_id,
                    "name":"boubaker","phone":"0663366915","balance":100}
    
