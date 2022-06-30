def generate_form_errors(form):
    message = ''
    for line in form:
        if line.errors:
            message += line.errors
    for error in form.errors:
        message += str(error)
    return message


# def is_author(request,pk):
#     if request.user.author.id == pk:
#         return True
#     else:
#         return False