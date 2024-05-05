print("Welcome to the To-Do List App! \n")
print("Menu \n 1. Add a task \n 2. View tasks \n 3. Mark a task as complete \n 4. Delete a task \n 5. Quit")


incompleted_tasks = []
completed_tasks = []

# ============== Functions ============= 
def add_task(inc_list, comp_list):
  task = input("\nEnter your task:")
  # Prevent to add same task if it already exists in completed
  if task not in inc_list and task not in comp_list: 
     inc_list.append(task)
     print("\033[91m" + "Incompleted tasks: ", inc_list , "\033[0m")
  else:
    print("\nTask already exists.")
  
def view_tasks(inc_list, comp_list):
  sort_by = input("Enter 'OR', 'ASC', or 'DESC' to view tasks in order of their creation (original state), ascending, or descending, respectively ")
  if sort_by.lower() == 'OR'.lower():
    print("\033[91m" + "Incompleted tasks: ", inc_list , "\033[0m")
    print("\033[92m" + "Completed tasks: ", comp_list, "\033[0m")
    
  elif sort_by.lower() == 'ASC'.lower():
    print("\033[91m" + "Incompleted tasks: ", sorted(inc_list), "\033[0m")
    print("\033[92m" + "Completed tasks: ", sorted(comp_list), "\033[0m")
      
  elif sort_by.lower() == 'DESC'.lower():    
    print("\033[91m" + "Incomplete tasks: ", sorted(inc_list, reverse=True), "\033[0m")
    print("\033[92m" + "Complete tasks: ", sorted(comp_list, reverse=True), "\033[0m")  
# removes task from incompleted list and add to the completed list    
def mark_task_completed(inc_list, comp_list):
  task = input("Enter the task that you want to mark as completed: ")
  try:
    inc_list.remove(task)
    comp_list.append(task)
  except:
    print("\n Task does not exist.\n")   
  finally:
    print("\033[91m" + "Incompleted tasks: ", inc_list , "\033[0m")
    print("\033[92m" + "Completed tasks: ", comp_list, "\033[0m")   
     
# Handles the error in case of removing non-existent task
def delete_task(inc_list):  
  task = input("Which task you want to remove? ")
  try:
      inc_list.remove(task)
  except:
    print("\n Task does not exist.\n")
  finally:
    print("\033[91m" + "Incompleted tasks: ", inc_list , "\033[0m")

# ============== Run App =============== 
def run_app():
  while True:
    action = input("Choose number with the associated action: ")
    if action.isdigit():
        if action == "1":
          add_task(incompleted_tasks, completed_tasks)
          
        elif action == "2":
          view_tasks(incompleted_tasks, completed_tasks)  
          
        elif action == "3":
          mark_task_completed(incompleted_tasks, completed_tasks)   
          
        elif action == "4":
          delete_task(incompleted_tasks)
          
        elif action == "5":
          break  
    else:
      print("Please enter number from 1 to 5")
  
  print("Completed Tasks: ", completed_tasks)    
  print("Incompleted Tasks: ", incompleted_tasks)    
      
run_app()      