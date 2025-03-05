from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/submit-message/")
async def submit_message(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    return JSONResponse(
        content={
            "status": "success", 
            "message": "Message received", 
            "data": {"name": name, "email": email, "message": message}
        }
    )


@app.get("/")
def read_root():
    return {"message": "OI! I'm alive!"}
