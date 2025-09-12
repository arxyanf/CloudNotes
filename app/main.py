from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import random

app = FastAPI()
BASE_DIR = Path(__file__).parent

# Mount static folder
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Templates
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Notes storage
notes = []
note_id_counter = 0
COLORS = ['#fffa65','#a0e7e5','#ffd6a5','#bdb2ff']

@app.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})

@app.post("/", response_class=HTMLResponse)
async def add_note(request: Request, title: str = Form(...), content: str = Form(...)):
    global note_id_counter
    note_id_counter += 1
    color = random.choice(COLORS)
    notes.append({
        "id": note_id_counter,
        "title": title,
        "content": content,
        "color": color
    })
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{note_id}", response_class=HTMLResponse)
async def delete_note(request: Request, note_id: int):
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    return RedirectResponse(url="/", status_code=303)

@app.post("/edit/{note_id}", response_class=HTMLResponse)
async def edit_note(request: Request, note_id: int, title: str = Form(...), content: str = Form(...)):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["content"] = content
            break
    return RedirectResponse(url="/", status_code=303)
