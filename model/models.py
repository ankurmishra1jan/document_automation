from typing import List
from pydantic import BaseModel

class InvoiceItem(BaseModel):
    description: str
    quantity: int
    unit_price: float
    total: float

class FormatCreationArgs(BaseModel):
    invoice_type: str
    invoice_number: str
    invoice_date: str
    due_date: str
    items: List[InvoiceItem]

