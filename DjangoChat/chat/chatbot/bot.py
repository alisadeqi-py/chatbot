import g4f

def chatbot(prompt):

    response = g4f.ChatCompletion.create(
         model = g4f.models.default,
         messages = [{"content": prompt,
                      "role": 'user'
                      }],
         timeout = 300,
     )
    return response


