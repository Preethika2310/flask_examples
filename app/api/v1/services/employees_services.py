employees = [
    {"id": 1, "name": "Pree"},
    {"id": 2, "name": "Siva"},
]

def fetch_employees():
    return employees

def create_employee(data):
    new_id = max([e["id"] for e in employees], default=0) + 1
    new_employee = {"id": new_id, "name": data.get("name")}
    employees.append(new_employee)
    return new_employee
    #return {"id":3,"name":data.get("name")}

def fetch_employee_by_id(id):
    for employee in employees:
        if employee["id"] == id:
            return employee
    return None
    #return {"id":1,"name":"pree"}

def edit_employee(id, data):
    for employee in employees:
        if employee["id"] == id:
            employee["name"] =data.get("name", employee["name"])
            return employee
    return None
    #return {"id":data.get("id"),"name":data.get("name")}

def delete_employee_by_id(id):
    for employee in employees:
        if employee["id"] == id:
            employees.remove(employee)
            return True
    return False
    #return {"status": f"Employee id {id} deleted successfully}
