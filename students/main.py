from fastapi import FastAPI
import uvicorn
from student_service import router

app = FastAPI()
app.include_router(router,prefix="/students",tags=["students"])

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)