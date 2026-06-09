# Interface
# Abstract class without attribute 

from abc import ABC, abstractmethod
class BankAPI(ABC):
    @abstractmethod
    def get_loan(self,details):
        ...

    @abstractmethod
    def donate(self,amount,charity):
        ...




# Concrete Class
class HDFCBANK(BankAPI):
    def get_loan(self, details):
        # check credit_score, trust
        pass

    def donate(self, amount, charity):
        if charity.size > 100:
            print(f"amout eligbile")
        else:
            pass 


class SBIBANK(BankAPI):
    def get_loan(self, details):
        # check 6m history, relability
        pass

    def donate(self, amount, charity):
        pass


if __name__=='__main__':
    api:BankAPI = HDFCBANK()    #  api:BankAPI = SBIBANK()
    # api doesn't care about Which bank you're using
    api.donate() 




# Base Class
# https://github.com/huggingface/transformers/blob/380e3cc5d59912a48508cb6d4959a31cd460e12e/src/transformers/pipelines/base.py#L372
# Concrete Class
# https://github.com/huggingface/transformers/blob/380e3cc5d59912a48508cb6d4959a31cd460e12e/src/transformers/pipelines/table_question_answering.py#L24