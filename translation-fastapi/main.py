from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from trans import translate_to_spanish  # Import your translation function

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/download")
async def download_translation(text: str):
    response = PlainTextResponse(content=text, headers={"Content-Disposition": "attachment; filename=translated_text.txt"})
    return response

@app.post("/translate")
async def translate(request: Request):
    form_data = await request.form()
    english_text = form_data.get("english_input")
    if english_text:
        spanish_text = translate_to_spanish(english_text)
        return templates.TemplateResponse("home.html", {"request": request, "translated_text": spanish_text})
    return templates.TemplateResponse("home.html", {"request": request})


