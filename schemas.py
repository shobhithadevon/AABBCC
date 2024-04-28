from typing import Optional,List,Generic,TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class SchoolSchema(BaseModel):
    stud_id: Optional[int]=None
    stud_name: Optional[str]=None
    stud_class: Optional[str]=None
    stud_age: Optional[int]=None
    
    class config:
        orm_mode = True

class requestSchool(BaseModel):
    parameter: SchoolSchema = Field(...)

class Response(GenericModel,Generic[T]):
    code:str
    status:str
    message:str
    result: Optional[T]



    

    