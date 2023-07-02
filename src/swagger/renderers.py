from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


class CustomSwaggerUIRenderer(SwaggerUIRenderer):
    template = "templates/swagger_index.html"
