from src.views.http_types.http_requests import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:

        #Responsavel por Interações com o HTTP

    def validate_and_create(self,http_requests: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreatorController()

        body = http_requests.body
        product_code = body["product_code"]

        # Logica de regra de Negocio
        formatted_response = tag_creator_controller.create(product_code)

        # Retorno http
        return  HttpResponse(status_code=200, body=formatted_response)
    
