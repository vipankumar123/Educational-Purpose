from fastapi import FastAPI, Request, Response

app = FastAPI()

#Event handler for startup
@app.on_event("startup")
async def startup_event():
    print("app is starting now!!$$$$$$$$$$$###########")
    #add your functionlaity

#Event handler for shutdown
@app.on_event("shutdown")
async def shutdown_event():
    print("app is shutdown now!!!!!!!!!!")
    #add your functionlaity

@app.get("/")
async def read_root():
    return {"message": "Hello Mind Blowing."}