from fastapi import FastAPI
from core.database import Base, engine
from routes import router
from loguru import logger
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()
app.include_router(router)
Base.metadata.create_all(bind=engine)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc: RequestValidationError):
    error_messages = []
    for error in exc.errors():
        loc = error['loc']
        field = ".".join(map(str, loc[1:])) # map(str,xxx) 將 loc[1:] 中的每個元素都轉換成string
        msg = error['msg']
        error_messages.append(f"{field}: {msg}")
    errors_string = ", ".join(error_messages)
    content = {"detail": errors_string}
    return JSONResponse(content=content, status_code=422)

@app.exception_handler(500)
async def internal_exception_handler(request, exc: Exception):
    logger.error(f"Internal Server Error: {exc}")
    content = {
        "code": "internal_server_error",
        "message": "An unexpected error occurred.",
        "description": str(exc)
    }
    return JSONResponse(status_code=500, content=content)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=9000, reload=True)