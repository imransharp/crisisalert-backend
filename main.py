from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from models import CrisisReport, SessionLocal
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
# Allow frontend to connect (CORS setup)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/reports")
def get_reports():
    db = SessionLocal()
    reports = db.query(CrisisReport).all()
    db.close()
    return JSONResponse(content=[{
        "id": r.id,
        "name": r.name,
        "district": r.district,
        "crisis": r.crisis
    } for r in reports])


@app.post("/api/reports")
async def receive_report(request: Request):
    data = await request.json()
    print("Received crisis report:", data)

    # Save to DB
    db = SessionLocal()
    report = CrisisReport(
        name=data["name"],
        district=data["district"],
        crisis=data["crisis"]
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    db.close()

    return {"message": "Report saved"}
