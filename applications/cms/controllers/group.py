from kokoropy.controller import Crud_Controller
from ..models.structure import Group

class Group_Controller(Crud_Controller):
    __model__               = Group

Group_Controller.publish_route()