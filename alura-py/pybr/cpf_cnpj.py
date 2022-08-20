from pydoc import doc
from validate_docbr import CPF
from validate_docbr import CNPJ


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento) 
        if self.tipo_documento == 'cpf':       
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == 'cnpj':
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError ("Documento inválido!!")
        else:
            raise ValueError("Documento inválido!")
        
    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!") 
   
    def formata_cpf(self):
       mascara = CPF()
       return mascara.mask(self.cpf)
   
    def __str__(self):
        return self.formata_cpf()
    
    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos inválida!")