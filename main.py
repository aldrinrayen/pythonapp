from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI App", version="1.0.0")

@app.get("/")
async def read_root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Hello, World! Welcome to FastAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
