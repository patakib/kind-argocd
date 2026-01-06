from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Wood Species API")

# -----------------------------
# Data model
# -----------------------------
class WoodSpecies(BaseModel):
    name: str
    density_kg_m3: float
    hardness_janka: int
    origin: str


# -----------------------------
# In-memory "database"
# -----------------------------
wood_db: Dict[int, WoodSpecies] = {
    1: WoodSpecies(
        name="Oak",
        density_kg_m3=750,
        hardness_janka=1360,
        origin="Europe / North America",
    ),
    2: WoodSpecies(
        name="Pine",
        density_kg_m3=500,
        hardness_janka=420,
        origin="Worldwide",
    ),
    3: WoodSpecies(
        name="Mahogany",
        density_kg_m3=850,
        hardness_janka=800,
        origin="Central and South America",
    ),
    4: WoodSpecies(
        name="Teak",
        density_kg_m3=660,
        hardness_janka=1150,
        origin="Southeast Asia",
    ),
}

# -----------------------------
# Endpoints
# -----------------------------

# GET all wood species
@app.get("/woods")
def get_all_woods():
    return wood_db


# GET a single wood species
@app.get("/woods/{wood_id}")
def get_wood(wood_id: int):
    if wood_id not in wood_db:
        raise HTTPException(status_code=404, detail="Wood species not found")
    return wood_db[wood_id]


# POST: add new wood species
@app.post("/woods/{wood_id}")
def add_wood(wood_id: int, wood: WoodSpecies):
    if wood_id in wood_db:
        raise HTTPException(status_code=400, detail="Wood ID already exists")
    wood_db[wood_id] = wood
    return {"message": "Wood species added", "wood": wood}


# PUT: update existing wood species
@app.put("/woods/{wood_id}")
def update_wood(wood_id: int, wood: WoodSpecies):
    if wood_id not in wood_db:
        raise HTTPException(status_code=404, detail="Wood species not found")
    wood_db[wood_id] = wood
    return {"message": "Wood species updated", "wood": wood}


# DELETE: remove wood species
@app.delete("/woods/{wood_id}")
def delete_wood(wood_id: int):
    if wood_id not in wood_db:
        raise HTTPException(status_code=404, detail="Wood species not found")
    del wood_db[wood_id]
    return {"message": "Wood species deleted"}