from kokoropy.controller import Crud_Controller
from ..models.structure import Widget

class Widget_Controller(Crud_Controller):
    __model__               = Widget

Widget_Controller.publish_route()