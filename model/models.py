from typing import List
from pydantic import BaseModel

class InvoiceItem(BaseModel):
    description: str
    quantity: str
    unit_price: str
    total: str

class FormatCreationArgs(BaseModel):
    invoice_type: str
    recipient_name: str
    invoice_number: str
    invoice_date: str
    due_date: str
    items: List[InvoiceItem]

