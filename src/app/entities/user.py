class User:

    name = str
    agency = str
    account = str
    current_balance = float
    
    def __init__(self, name : str, agency: str, account: str, current_balance:float):
        if len(agency) != 4 or not agency.isdigit():
            raise ValueError("Agencia deve conter exatamente 4 dígitos.")
        
        parts = account.split("-")
        if len(parts) != 2 or not (parts[0].isdigit() and len(parts[0])) == 5 and parts[1].isdigit() and len(parts[1]) == 1:
            raise ValueError("Conta deve coter 5 dígitos no formato XXXX-X")

        
        def validate_name(name: str) -> bool:

            if name.type !=str:
                raise ValueError("Nome deve ser uma string")
        
            elif not name.isalpha():
                raise ValueError("Nome deve conter apenas letras")
            
            elif len(name) < 3:
                raise ValueError("Nome deve conter pelo menos 3 letras")
            return True
            


        self.name = name
        self.agency = agency
        self.account = account
        self.current_balance = current_balance
