import flet as ft

def main(page: ft.Page):
    tasks = []

    def add_task(e):
        task_name = task_input.value
        if task_name:
            tasks.append(task_name)
            task_input.value = ""
            task_list.controls.append(ft.Text(task_name))
            page.update()

    task_input = ft.TextField(label="Digite uma nova tarefa", autofocus=True)
    add_button = ft.ElevatedButton("Adicionar tarefa", on_click=add_task)
    task_list = ft.Column()

    page.add(
        task_input,
        add_button,
        task_list,
    )

ft.app(target=main)
