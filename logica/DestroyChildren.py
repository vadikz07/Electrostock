def destroy_children(parent):
    try:
        for child in parent.winfo_children():
            child.destroy()
    except Exception as error:
        print(f'Ha habido un problema: {error}')
        