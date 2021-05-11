import uvicorn
from fastapi import FastAPI

from routers import city, PackageHistory
from routers import message

app = FastAPI()

app.include_router(city.router)
app.include_router(message.router)
app.include_router(PackageHistory.router)



@app.get("/")
def welcome():
    return {'Welcome'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
