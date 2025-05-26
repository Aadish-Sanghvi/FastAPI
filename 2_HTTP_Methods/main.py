from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('2_HTTP_Methods/patients.json', 'r') as file:
        data = json.load(file)
    return data

@app.get('/')
def hello():
    return {'message': 'Patients Management System API!'}

@app.get('/about')
def hello():
    return {'message': 'Fully Functional API for Patients Management System!'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve", example="P001")):
    # load all the patients 
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
# '...' means this is a required parameter i.e. sort_by  query parameter is required and 'order' query parameter is optional
def sort_patients(sort_by: str = Query(..., description = 'Sort on the basis of height, weight or bmi'), order: str = Query('asc', description = 'Sort by ascending or descending order')):
    valid_fields = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid sort order")
    
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)
    return sorted_data

# uvicorn 2_HTTP_Methods.main:app --reload
# http://127.0.0.1:8000/docs