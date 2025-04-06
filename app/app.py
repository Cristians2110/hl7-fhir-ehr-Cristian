from fastapi import FastAPI, Request
from app.controlador.PatientCrud import GetPatientById,WritePatient,GetPatientByIdentifier
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Form
from pydantic import BaseModel 
import uvicorn


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solo este dominio
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get("/patient/{patient_id}", response_model=dict)
async def get_patient_by_id(patient_id: str):
    print("solicitud datos:",patient_id)
    status,patient = GetPatientById(patient_id)
    if status=='success':
        return patient  # Return patient
    elif status=='notFound':
        raise HTTPException(status_code=404, detail="Patient not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")




@app.get("/patient", response_model=dict)
async def get_patient_by_identifier(system: str, value: str):
    print("solicitud datos:",system,value)
    status,patient = GetPatientByIdentifier(system, value)
    if status=='success':
        return patient  # Return patient
    elif status=='notFound':
        raise HTTPException(status_code=404, detail="Patient not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")


@app.post("/patient", response_model=dict)
async def add_patient(request: Request):
    new_patient_dict = dict(await request.json())
    status,patient_id = WritePatient(new_patient_dict)
    if status=='success':
        return {"_id":patient_id}  # Return patient id
    else:
        raise HTTPException(status_code=500, detail=f"Validating error: {status}")



# Endpoint para crear una nueva solicitud de servicio
from app.controlador.PatientCrud import WriteServiceRequest

@app.post("/service_request")
async def create_service_request(request: Request):
    data = await request.json()

    print("Datos recibidos:", data)  # Para ver en consola qué llega

    request_json = {
        "tipo_documento": data.get("document_type"),
        "numero_documento": data.get("patient_id"),
        "tipo_examen": data.get("service_type"),
        "descripcion": data.get("description"),
        "solicitante": data.get("requester"),
        "prioridad": data.get("priority"),
    }

    status, id = WriteServiceRequest(request_json)
    return {"status": status, "id": id}

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/service_request_form", response_class=HTMLResponse)
async def serve_form():
    with open("static/service_request_form.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app.app:app", host="0.0.0.0", port=10000, reload=False)

