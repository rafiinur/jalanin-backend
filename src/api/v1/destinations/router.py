from fastapi import APIRouter

router = APIRouter(prefix="/destinations", tags=["destinations"])

@router.get("/")
def read_destinations():
    """
    Retrieve a list of all destinations.
    """
    return {"message": "List of destinations"}

@router.post("/")
def create_destination():
    """
    Create a new destination.
    """
    return {"message": "Destination created"}

@router.put("/{destination_id}")
def update_destination(destination_id: int):
    """
    Update an existing destination.
    """
    return {"message": f"Destination {destination_id} updated"}

@router.delete("/{destination_id}")
def delete_destination(destination_id: int):
    """
    Delete a destination.
    """
    return {"message": f"Destination {destination_id} deleted"}