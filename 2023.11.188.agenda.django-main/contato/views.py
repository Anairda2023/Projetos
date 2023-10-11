from django.shortcuts import render

def index(request):

    dados = {
        1: {
            "nome": "weskley bezerra",
            "fone": "99675-3679",
            "email": "weskley@xpto.com"
        },
        2: {
            "nome": "filipe oliveira",
            "fone": "98787-5972",
            "email": "filipe@xpto.com"
        },
        3: {
            "nome": "adriana silva",
            "fone": "98595-5684",
            "email": "adriana@xpto.com"
        },
    }

    return render(request, "contato/index.html", {"contatos": dados})