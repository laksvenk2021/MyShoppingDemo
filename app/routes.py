from fastapi import APIRouter, HTTPException
from app.models import Item, ItemCreate, ItemUpdate
from typing import List

router = APIRouter()

items_db = {
    1: Item(id=1, name="Laptop", description="14-inch laptop", price=999.99, in_stock=True),
    2: Item(id=2, name="Headphones", description="Noise-cancelling", price=199.99, in_stock=True),
}

@router.get("/", response_model=List[Item])
def list_items():
    return list(items_db.values())

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item, status_code=201)
def create_item(item_create: ItemCreate):
    next_id = max(items_db.keys(), default=0) + 1
    item = Item(id=next_id, **item_create.dict())
    items_db[next_id] = item
    return item

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemUpdate):
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    update_data = item_update.dict(exclude_unset=True)
    updated_item = item.copy(update=update_data)
    items_db[item_id] = updated_item
    return updated_item

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
