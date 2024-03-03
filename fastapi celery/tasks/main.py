from fastapi import FastAPI, HTTPException, BackgroundTasks
from datetime import datetime
from tasks.tasks import scheduled_taskss
app = FastAPI()

@app.post("/schedule-task/{task_id}")
async def schedule_tasks(task_id: int, message: str, execute_at: datetime, background_tasks: BackgroundTasks):
    # Invoke the task using the correct name
    
    scheduled_taskss.apply_async(args=[task_id, message], eta=execute_at)

    return {"message": f"Task {task_id} scheduled for execution at {execute_at}."}
