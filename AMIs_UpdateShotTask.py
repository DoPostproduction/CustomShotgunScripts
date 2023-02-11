status = shotgun.dialogs.ask_choice("Seleccione el estado para la tarea de Denoise:", ["Pendiente", "En Progreso", "Finalizado"])
user = shotgun.users.find("HumanUser", [["sg_status_list", "is", "act"]])
assigned_user = shotgun.dialogs.ask_user("Seleccione el artista al que desea asignar la tarea de Denoise:", multi_select=False, valid_types=["HumanUser"])
if assigned_user is not None:
    task = shotgun.create("Task", {"content": "Denoise", "project": context.project, "entity": context.entity, "task_assignees": [assigned_user], "sg_status_list": status})
    shotgun.update(task, {"sg_status_list": status, "task_assignees": [assigned_user]})
    shotgun.refresh()
    shotgun.clear_cache()
    shotgun.navigate_to(task)
