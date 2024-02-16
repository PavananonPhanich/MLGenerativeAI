from pyscript import document,window,display
from pyweb import pydom

async def  refresh_page(e):
    await window.location.reload()

task_foodType = pydom["#task-foodType"][0]
task_foodCal = pydom["#task-foodCal"][0]
task_foodTaste = pydom["#task-foodTaste"][0]
task_foodCountry = pydom["#task-foodCountry"][0]
task_foodClean = pydom["#task-foodClean"][0]
task_foodHalan = pydom["#task-foodHalan"][0]

    
def add_task(e):
    
    # ignore empty task  or (task_foodCal.value) or (task_foodTaste.value) or (task_foodCountry.value) 
    if not (task_foodType.value or task_foodCal.value or task_foodTaste.value or task_foodCountry.value):
        return None
    if not task_foodClean:
        return False
    if not task_foodHalan:
        return False
    
    display(task_foodType.value, target="task-foodshow-1", append=False)
    display(task_foodCal.value, target="task-foodshow-2", append=False)
    display(task_foodTaste.value, target="task-foodshow-3", append=False)
    display(task_foodCountry.value, target="task-foodshow-4", append=False)
    display(task_foodClean.value, target="task-foodshow-5", append=False)
    display(task_foodHalan.value, target="task-foodshow-6", append=False)

