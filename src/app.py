from fastapi import FastAPI
from core.database import Base, engine
from routes import router


app = FastAPI()
app.include_router(router)
Base.metadata.create_all(bind=engine)

    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5000)