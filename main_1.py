import models as m

# ################## MEI EXAMPLE #######################
# user_task = input("Gimme your Dammn Task: ")

# todo_list = m.TodoList.get_by_id(1)

# todo_task = m.TodoTask(task=user_task, todo_list=todo_list)

# todo_task.save()
'''
username
	password
		print(table of list)
		select list
		create list
		delete list
			print(table of task)
			create task
			update task
			delete task
'''
current_user = "0"
while current_user == "0":
    if current_user == "0":
        print("=================")
        print(current_user)
        print('''
        1. Log In
        2. Sign Up
        ''')
        print("=================")
        input_login_signup = input('Do you want to login or sign up?:  ')
        if input_login_signup == '1':  # login
            login_username = input("username:    ")
            login_password = input("password:    ")
            if m.UserProfile.get_or_none(m.UserProfile.username == login_username) != None and m.UserProfile.get_or_none(m.UserProfile.password == login_password) != None:
                current_user = m.UserProfile.get(
                    m.UserProfile.username == login_username)
                while current_user == m.UserProfile.get(
                        m.UserProfile.username == login_username):
                    print(f"Hello {login_username}")
                    print("=================")
                    print(current_user)
                    print('''
1. Create list
2. Create task
3. Update task
4. Delete list
5. Delete task
9. LOGOUT
                        ''')
                    print("=================")
                    user_choice = input('Choose 1 ffs ')
                    if user_choice == '1':
                        list_input = input('give me a list: ')
                        m.TodoList(name=list_input,
                                   user_profile=current_user).save()
                    elif user_choice == '2':
                        print('----------2-----------')
                        print('')
                        for todo in m.TodoList.select().where(m.TodoList.user_profile_id == current_user):
                            print(f'''{todo.id}: {todo.name}''')
                        print('')
                        print('---------------------')
                        table_id = input('give me table id: ')
                        user_input = input('Give me a task: ')
                        m.TodoTask(task=user_input, todo_list=table_id).save()
                    elif user_choice == '3':
                        print('----------3-----------')
                        print('')
                        for tlist in current_user.lists:
                            print(f'''{tlist.id}: {tlist.name}''')
                        print('')
                        print('---------------------')

                        table_id = input('give me table id: ')
                        for task in m.TodoTask.select().where(m.TodoTask.todo_list_id == table_id):
                            if task.completed == False:
                                symbol = '|X|'
                            else:
                                symbol = '|V|'
                            print(f'''{task.id}: {task.task}: {symbol}''')
                        update_task = input(
                            'select task by id :slightly_smiling_face: ')
                        m.TodoTask.update(completed=True).where(
                            m.TodoTask.id == update_task).execute()

                    elif user_choice == '4':

                        print('----------4-----------')
                        print('')
                        for todo in m.TodoList.select().where(m.TodoList.user_profile_id == current_user):
                            print(f'''{todo.id}: {todo.name}''')
                        print('')
                        print('---------------------')
                        table_id_delete = input(
                            'Select the list you want to delete: ')

                        m.TodoTask.delete().where(m.TodoTask.todo_list_id == table_id_delete).execute()
                        m.TodoList.delete().where(m.TodoList.id == table_id_delete).execute()
                        print('-----------4----------')
                        print(f'deleted your list {table_id_delete}')
                        print('')
                        for todo in m.TodoList.select().where(m.TodoList.user_profile_id == current_user):
                            print(f'''{todo.id}: {todo.name}''')
                        print('')
                        print('---------------------')

                    elif user_choice == '5':

                        print('----------5-----------')
                        print('')
                        for tlist in m.TodoList.select().where(m.TodoList.user_profile_id == current_user):
                            print(f'''{tlist.id}: {tlist.name}''')
                        print('')
                        print('---------------------')

                        table_id = input('give me table id: ')
                        print('----------5-----------')
                        for task in m.TodoTask.select().order_by(m.TodoTask.id):
                            if task.completed == False:
                                symbol = '|X|'
                            else:
                                symbol = '|V|'
                            print(f'''{task.id}: {task.task}: {symbol}''')
                        print('---------------------')
                        task_id_delete = input(
                            'Select the task you want to delete: ')
                        m.TodoTask.delete().where(m.TodoTask.id == task_id_delete).execute()
                        print('----------5-----------')
                        for task in m.TodoTask.select().order_by(m.TodoTask.id):
                            if task.completed == False:
                                symbol = '|X|'
                            else:
                                symbol = '|V|'
                            print(f'''{task.id}: {task.task}: {symbol}''')
                        print('---------------------')
                    elif user_choice == '9':
                        current_user = '0'
            else:
                print(
                    f"{login_username} is not found. Please make sure you created your account")
        elif input_login_signup == '2':  # sign Up

            signup_username = input("username:    ")
            signup_password = input("password:    ")
            if m.UserProfile.get_or_none(m.UserProfile.username == signup_username) != True:
                m.UserProfile(username=signup_username,
                              password=signup_password).save()
                print("signup completed you may login now")
            else:
                print(
                    f"{signup_username} is already taken. Please try something else")

        #         print("=================")
        #         print('''
        #         1. Create list
        #         2. Create task
        #
        #        3. Update task
        #         4. Delete list
        #         5. Delete task
        #             ''')
        #         print("=================")

        #         user_choice = input('Choose 1 ffs ')
        #         if user_choice == '1':
        #         list_input = input('give me a list: ')
        #         m.TodoList(name=list_input).save()
        #         elif user_choice == '2':

        #         print('---------------------')
        #         print('')
        #         for todo in m.TodoList.select():
        #             print(f'''{todo.id}: {todo.name}''')
        #         print('')
        #         print('---------------------')

        #         table_id = input('give me table id: ')
        #         user_input = input('Give me a task: ')
        #         m.TodoTask(task=user_input, todo_list=table_id).save()
        #         elif user_choice == '3':

                # print('---------------------')
                # print('')
                # for tlist in m.TodoList.select():
                #     print(f'''{tlist.id}: {tlist.name}''')
                # print('')
                # print('---------------------')

                # table_id = input('give me table id: ')
                # for task in m.TodoTask.select():
                #     if task.completed == False:
                #         symbol = '|X|'
                #     else:
                #         symbol = '|V|'
                #     print(f'''{task.id}: {task.task}: {symbol}''')
                # update_task = input('select task by id :slightly_smiling_face: ')
                # m.TodoTask.update(completed=True).where(
                #     m.TodoTask.id == update_task).execute()

                # elif user_choice == '4':

                # print('---------------------')
                # print('')
                # for todo in m.TodoList.select():
                #     print(f'''{todo.id}: {todo.name}''')
                # print('')
                # print('---------------------')
                # table_id_delete = input('Select the list you want to delete: ')

                # m.TodoTask.delete().where(m.TodoTask.todo_list_id == table_id_delete).execute()
                # m.TodoList.delete().where(m.TodoList.id == table_id_delete).execute()
                # print('---------------------')
                # print(f'deleted your list {table_id_delete}')
                # print('')
                # for todo in m.TodoList.select():
                #     print(f'''{todo.id}: {todo.name}''')
                # print('')
                # print('---------------------')

                # elif user_choice == '5':

                # print('---------------------')
                # print('')
                # for tlist in m.TodoList.select():
                #     print(f'''{tlist.id}: {tlist.name}''')
                # print('')
                # print('---------------------')

                # table_id = input('give me table id: ')
                # for task in m.TodoTask.select().order_by(m.TodoTask.id):
                #     if task.completed == False:
                #         symbol = '|X|'
                #     else:
                #         symbol = '|V|'
                #     print(f'''{task.id}: {task.task}: {symbol}''')
                # task_id_delete = input('Select the task you want to delete: ')
                # m.TodoTask.delete().where(m.TodoTask.id == task_id_delete).execute()
                # for task in m.TodoTask.select().order_by(m.TodoTask.id):
                #     if task.completed == False:
                #         symbol = '|X|'
                #     else:
                #         symbol = '|V|'
                #     print(f'''{task.id}: {task.task}: {symbol}''')
