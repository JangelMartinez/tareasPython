
import datetime
import os


class Todo:
    """
    This class represents a todo.
    and it has a name, a state and a creation date.
    """
    
    def __init__(self, name):
        """
        Initializes a new instance of the tarea class.

        Args:
            name (str): The name of the todo.
            pending (bool): The state of the todo.
            date_create_todo (datetime): The date of the todo.

        Returns:
            None
        """
        self.name = name
        self.pending = True
        self.date_create_todo = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the Todo object.

        Returns:
            str: A string containing the name of the Todo, the creation date, and the state (pending or completed).
        """
        return '\nTodo:' + self.name + '\nCreate date: ' + str(self.date_create_todo) + '\nPending:' + self.str_pending()
    
    def __repr__(self):
        return self.name
    
    def nameshort(self, id):
        """
        Prints a shortened version of the name of the todo item with its corresponding ID.

        Parameters:
            id (int): The index of the todo item in the list.

        Returns:
            None
        """
    
        print(str(id + 1) + " - " + self.name + " - " + self.str_pending())
    
    def change_state(self):
        """
        Toggles the state of the todo between pending and completed.

        This method does not take any parameters.

        This method does not return any value.
        """
        self.pending = not self.pending

    def str_pending(self):
        """
        A function that returns a string indicating whether the todo is pending or completed.

        Returns:
            str: 'Pendiente' if the todo is pending, 'Completada' if the todo is completed.
        """
        if self.pending:
            return 'Pending'
        else:
            return 'Completed' 
        
class TodoList:
    """
    This class represents a todo list.
    and it has a list of todos.
    """
    def __init__(self):
        """
        Initializes a new instance of the TodoList class.

        Returns:
            None
        """
        self.todos = []

    def __str__(self):
        """
        Returns a string representation of the TodoList object.

        Returns:
            str: A string containing the name of the TodoList and a list of the todos in the TodoList.
        """
        text = ""

        for index, todo in enumerate(self.todos):
            text += (f"\nÍd: {index + 1} - {todo}\n")

        return text + "\n"

    def add_todo(self, newtodo):
        """
        Adds a new todo to the TodoList.

        Args:
            newtodo (Todo): The todo to add to the TodoList.

        Returns:
            None
        """
        self.todos.append(newtodo)

    def remove_todo(self, removetodo):
        """
        Removes a todo from the TodoList.

        Args:
            removetodo (int): The todo to remove from the TodoList.

        Returns:
            None
        """
        self.todos.pop(removetodo)

    def change_state(self, changetodo):
        """
        Changes the state of a todo in the TodoList.

        Args:
            changetodo (Todo): The todo to change the state of.

        Returns:
            None
        """
        changetodo.change_state()

    def sort_by_date(self):
        """
        Sorts the todos in the TodoList by creation date.

        This method does not take any parameters.

        This method does not return any value.
        """
        self.todos.sort(key=lambda todo: todo.date_create_todo)
    


lista_tareas = TodoList()

while True:
    print("\nMenu:")  
    print("1. Crear Tarea")
    print("2. Ver Tareas")
    print("3. Ver Tareas Pendientes")
    print("4. Ver Tareas Completadas")
    print("5. Marcar Tarea como Completada")
    print("6. Eliminar Tarea")
    print("7. Salir")
    option = int(input("Elige una opcion: "))

    if option == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("Introduce el nombre de la Tarea: ")
        tarea = Todo(name)
        lista_tareas.add_todo(tarea)

    elif option == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n==================")
        print("Tareas:")
        print("==================")
        print(lista_tareas)

    elif option == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n==================")
        print("Tareas pendientes:")
        print("==================")
        count = 0
        for todo in lista_tareas.todos:
            if todo.pending:
                print(todo)
                count+=1
        if count == 0:
            print("No hay tareas pendientes")

    elif option == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n==================")
        print("Tareas completadas:")
        print("==================")
        count = 0
        for todo in lista_tareas.todos:
            if not todo.pending:
                print(todo)
                count+=1
        if count == 0:
            print("No hay tareas completadas")

    elif option == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        for index, todo in enumerate(lista_tareas.todos):
            todo.nameshort(index)
            
        idtochangestate = int(input("Introduce el indice que quieres cambiar el estado de la Tarea: "))
        
        try:
            if lista_tareas.todos[idtochangestate-1]:
                lista_tareas.todos[idtochangestate-1].change_state()
            else:
                print("Tarea no encontrada")
        except IndexError:
            print("Tarea no encontrada")
        

    elif option == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        for index, todo in enumerate(lista_tareas.todos):
            todo.nameshort(index)
            
        idtoremove = int(input("Introduce el indice de la tarea que quieres borrar: "))
        
        try:
            if lista_tareas.todos[idtoremove-1]:
                lista_tareas.remove_todo(idtoremove-1)
            else:
                print("Tarea no encontrada")
        except IndexError:
            print("Tarea no encontrada")

    elif option == 7:
        break

    else:
        print("Opcion no valida")

print("Adios")