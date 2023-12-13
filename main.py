# function for reading patients data from file, the name of file as an argument
from datetime import datetime

def readPatientsFromFile(filename):

    # creating a dictionary to store patients data with respective id
    patientData = {}
    with filename as f:
        for line in f:
            data = line.strip().split(",")
            patientId = int(data[0])
            visit = [data[1], float(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7])]
            if patientId in patientData:
                patientData[patientId].append(visit)
            else:
                patientData[patientId] = [visit]
    return patientData


# function which displays the patient data, takes patients file and the id as parameter
def displayPatientData(patients, patientId):

    if not isinstance(patients, dict):
        print("Error: patients must be a dictionary.")
        return
    if patientId < 0 or not isinstance(patientId, int):
        print("Error: patientId must be a non-negative integer.")
        return
    if patientId != 0 and patientId not in patients:
        print(f"Patient with ID {patientId} not found.")
        return

    if patientId == 0:
        # Display data for all patients
        print(f"\nAll Patients Data")
        for pid, visits in patients.items():
            print(f"\nPatient ID: {pid}")
            for visit in visits:
                print(f"\n\tVisit Date: {visit[0]}")
                print(f"\tTemperature: {visit[1]} °C")
                print(f"\tHeart Rate: {visit[2]} bpm")
                print(f"\tRespiratory Rate: {visit[3]} bpm")
                print(f"\tSystolic BP: {visit[4]} mmHg")
                print(f"\tDiastolic BP: {visit[5]} mmHg")
                print(f"\tOxygen Saturation: {visit[6]} %")
    else:
        # Display data for the specified patient
        visits = patients[patientId]
        print(f"\nPatient ID: {patientId}")
        for visit in visits:
            print(f"\n\tVisit Date: {visit[0]}")
            print(f"\tTemperature: {visit[1]} °C")
            print(f"\tHeart Rate: {visit[2]} bpm")
            print(f"\tRespiratory Rate: {visit[3]} bpm")
            print(f"\tSystolic BP: {visit[4]} mmHg")
            print(f"\tDiastolic BP: {visit[5]} mmHg")
            print(f"\tOxygen Saturation: {visit[6]} %")


def displayStats(patients, patientId=0):
    if type(patients) is not dict:
        print("Error: Invalid patient data")
        return
    if patientId < 0:
        print("Error: Invalid patient ID")
        return
    
    if patientId == 0:
        # Calculate averages for all patients
        all_temps = []
        all_hr = []
        all_rr = []
        all_sbp = []
        all_dbp = []
        all_o2sat = []

        for patient_id in patients:
            for visit in patients[patient_id]:
                all_temps.append(visit[1])
                all_hr.append(visit[2])
                all_rr.append(visit[3])
                all_sbp.append(visit[4])
                all_dbp.append(visit[5])
                all_o2sat.append(visit[6])

        if len(all_temps) == 0:
            print("No data found for any patients.")
            return

        avg_temp = sum(all_temps) / len(all_temps)
        avg_hr = sum(all_hr) / len(all_hr)
        avg_rr = sum(all_rr) / len(all_rr)
        avg_sbp = sum(all_sbp) / len(all_sbp)
        avg_dbp = sum(all_dbp) / len(all_dbp)
        avg_o2sat = sum(all_o2sat) / len(all_o2sat)

        print("\nVital Signs for All Patients:")
        print(f"\n\tAverage heart rate: {avg_hr:.2f} bpm")
        print(f"\tAverage temperature: {avg_temp:.2f} °C")
        print(f"\tAverage respiratory rate: {avg_rr:.2f} bpm")
        print(f"\tAverage systolic blood pressure: {avg_sbp:.2f} mmHg")
        print(f"\tAverage diastolic blood pressure: {avg_dbp:.2f} mmHg")
        print(f"\tAverage oxygen saturation: {avg_o2sat:.2f} %")
        
    else:
        # Calculate averages for specified patient
        if patientId not in patients:
            print(f"No data found for patient with ID {patientId}.")
            return

        patient_data = patients[patientId]

        if len(patient_data) == 0:
            print(f"No data found for patient with ID {patientId}.")
            return

        all_temps = [visit[1] for visit in patient_data]
        all_hr = [visit[2] for visit in patient_data]
        all_rr = [visit[3] for visit in patient_data]
        all_sbp = [visit[4] for visit in patient_data]
        all_dbp = [visit[5] for visit in patient_data]
        all_o2sat = [visit[6] for visit in patient_data]

        avg_temp = sum(all_temps) / len(all_temps)
        avg_hr = sum(all_hr) / len(all_hr)
        avg_rr = sum(all_rr) / len(all_rr)
        avg_sbp = sum(all_sbp) / len(all_sbp)
        avg_dbp = sum(all_dbp) / len(all_dbp)
        avg_o2sat = sum(all_o2sat) / len(all_o2sat)

        print(f"\nVital Signs for Patient {patientId}:")
        print(f"\n\tAverage temperature: {avg_temp:.2f} °C")
        print(f"\tAverage heart rate: {avg_hr:.2f} bpm")
        print(f"\tAverage respiratory rate: {avg_rr:.2f} bpm")
        print(f"\tAverage systolic blood pressure: {avg_sbp:.2f} mmHg")
        print(f"\tAverage diastolic blood pressure: {avg_dbp:.2f} mmHg")
        print(f"\tAverage oxygen saturation: {avg_o2sat:.2f} %")


def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    # Check if patientId is valid
    if not isinstance(patientId, int) or patientId <= 0:
        print("Invalid patient ID. Please enter a positive integer.")
        return

    # Check if date is valid
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date. Please enter date in the format 'yyyy-mm-dd'.")
        return

    # Check if vital sign values are valid
    if not isinstance(temp, float) or temp < 0:
        print("Invalid temperature value. Please enter a non-negative float.")
        return

    if not isinstance(hr, int) or hr < 0:
        print("Invalid heart rate value. Please enter a non-negative integer.")
        return

    if not isinstance(rr, int) or rr < 0:
        print("Invalid respiratory rate value. Please enter a non-negative integer.")
        return

    if not isinstance(sbp, int) or sbp < 0:
        print("Invalid systolic blood pressure value. Please enter a non-negative integer.")
        return

    if not isinstance(dbp, int) or dbp < 0:
        print("Invalid diastolic blood pressure value. Please enter a non-negative integer.")
        return

    if not isinstance(spo2, int) or spo2 < 0 or spo2 > 100:
        print("Invalid oxygen saturation value. Please enter an integer between 0 and 100.")
        return

    # Add new patient data to dictionary
    if patientId not in patients:
        patients[patientId] = []
    patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])

    # Append new patient data to file
    with open('patients.txt', 'a') as fn:
        fn.write(f"\n{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}")

    print(f"\nVisit is saved successfully for Patient {patientId}.")


def findVisitsByDate(patients, year, month):
    results = []
    for patient_id, visits in patients.items():
        for visit in visits:
            # Check if visit date is in the provided year and/or month
            if year and visit[0].startswith(str(year)):
                if month and visit[0].startswith(f"{year}-{month:02}"):
                    results.append((patient_id, visit))
                elif not month:
                    results.append((patient_id, visit))
            elif not year:
                results.append((patient_id, visit))
    return results


def findPatientsWhoNeedFollowUp(patients):
    
    followup_patients = []
    for patient_id, visits in patients.items():
        for visit in visits:
            if (visit[2] > 100 or visit[2] < 60 or visit[4] > 140 or visit[5] > 90 or visit[6] < 90):
                followup_patients.append(patient_id)
                break # once a patient is added, no need to check further visits
    return followup_patients

def deleteAllVisitsOfPatient(patients, patientId, filename):

    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}")
        return
 
    # delete all visits of the patient
    patients.pop(patientId)
 
    print(f"Data for patient {patientId} has been deleted.")


def menu():

    patientsFile = open("patients.txt")
    patients = readPatientsFromFile(patientsFile)

    print(f"\n\nWelcome to the Health Information System")
    print(f"\n\n1. Display all patient data")
    print(f"2. Display patient data by ID")
    print(f"3. Add patient data")
    print(f"4. Display patient statistics")
    print(f"5. Find visits by year, month, or both")
    print(f"6. Find patients who need follow up")
    print(f"7. Delete all visits of a particular patient")
    print(f"8. Quit")
    choice = input("Enter your choice (1-8): ")
 
    match choice:
            case '1':
                displayPatientData(patients,0)

            case '2':
                patientId = int(input(f"\nEnter patient ID: "))
                displayPatientData(patients, patientId)

            case '3':
                patientId = int(input(f"\nEnter patient ID: "))
                date = input(f"Enter visit date (yyyy-mm-dd): ")
                temp = float(input(f"Enter temperature: "))
                hr = int(input(f"Enter heart rate: "))
                rr = int(input(f"Enter respiratory rate: "))
                sbp = int(input(f"Enter systolic blood pressure: "))
                dbp = int(input(f"Enter diastolic blood pressure: "))
                spo2 = int(input(f"Enter oxygen saturation level: "))
                addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, patientsFile)
    
            case '4':
                patientId = int(input(f"\nEnter patient ID (or '0' for all patients): "))
                displayStats(patients, patientId)
            
            case '5':
                year = int(input("\nEnter visit year: "))
                month = int(input("Enter visit month: "))
                print(findVisitsByDate(patients, year, month))

            case '6':
                print("\nPatient with following ID(s) need follow up: ")
                print(findPatientsWhoNeedFollowUp(patients))

            case '7':
                patientId = int(input("\nEnter patient ID to delete record: "))
                deleteAllVisitsOfPatient(patients, patientId, patientsFile)
            
            case '8':
                exit(1)
    
    menu()
    

# storing patients.txt file into variable object

menu()





