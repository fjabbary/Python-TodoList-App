print("Welcome to the To-Do List App! \n")
print("Menu \n 1. Add a task \n 2. View tasks \n 3. Mark a task as complete \n 4. Delete a task \n 5. Quit")


incompleted_tasks = []
completed_tasks = []

# ============== Functions ============= 
def add_task(inc_list, comp_lst):
  task = input("\nEnter your task:")
  # Prevent to add same task if it already exists in completed
  if task not in inc_list and task not in comp_lst: 
     inc_list.append(task)
     print(inc_list)
  else:
    print("\nTask already exists.")
  
def view_tasks(inc_list, comp_lst):
  action = input("Enter 'C' to see completed tasks or Enter 'I' to see Incompleted tasks ")
  if action.lower() == 'I'.lower():
    print("Incompleted Tasks: ", inc_list)
  elif action.lower() == 'C'.lower():    
    print("Completed Tasks", comp_lst)
    
# removes task from incompleted list and add to the completed list    
def mark_task_completed(inc_lst, comp_lst):
  task = input("Enter the task that you want to mark as completed: ")
  try:
    inc_lst.remove(task)
    comp_lst.append(task)
  except:
     print("\n Task does not exist.\n")       
     
# Handles the error in case of removing non-existent task
def delete_task(inc_list):  
  task = input("Which task you want to remove? ")
  try:
      inc_list.remove(task)
      print(inc_list)
  except:
    print("\n Task does not exist.\n")


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