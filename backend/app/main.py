from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import JSONResponse
from pydantic import EmailStr

app = FastAPI()

@app.post("/contato")
async def submit_message(
    name: str = Form(...),
    email: EmailStr = Form(...),  # Validação de email usando Pydantic
    message: str = Form(...),
):
    if not name or not message:
        raise HTTPException(status_code=400, detail="Name and message are required")
    
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": "Message received",
            "data": {"name": name, "email": email, "message": message}
        }
    )
