from dataclasses import dataclass
from typing import List, Optional

@dataclass
class StaffMember:
    """
    Clase para representar a un miembro del personal.
    Esta es la clase central donde puedes editar la información.
    """
    name: str
    role: str
    email: str
    image_url: str = "/static/img/placeholder.jpg"
    order_index: int = 0

def get_local_staff_list() -> List[StaffMember]:
    """
    Retorna la lista de personal definida localmente.
    EDITA ESTA LISTA para cambiar los nombres y cargos.
    """
    return [
        StaffMember(
            name="Pablo Matus",
            role="Director",
            email="p.matus@educunco.cl",
            order_index=1
        ),
        StaffMember(
            name="Luis Cofre Reyes",
            role="Docente",
            email="l.reyes@educunco.cl",
            order_index=2
        ),
        StaffMember(
            name="Dariana Herriquez Palma",
            role="Docente",
            email="d.herriquez@educunco.cl",
            order_index=3
        ),
        StaffMember(
            name="Daniela Mendez Martinez",
            role="Docente",
            email="d.mendez@educunco.cl",
            order_index=4
        ),
        StaffMember(
            name="Cristian Neculqueo Saavendra",
            role="Doncente",
            email="c.neculqueo@educunco.cl",
            order_index=5
        ),
        StaffMember(
            name="Gladys Osorio Valdivia",
            role="Docente",
            email="g.osorio@educunco.cl",
            order_index=6
        ),
        StaffMember(
            name="Marcela Reyes Rifo",
            role="Docente",
            email="m.reyes@educunco.cl",
            order_index=7
        ),
        StaffMember(
            name="Natalie Roman Fernandez",
            role="Docente",
            email="n.roman@educunco.cl",
            order_index=8
        ),
        StaffMember(
            name="Laura Catrilaf Pino",
            role="Docente",
            email="l.catrilaf@educunco.cl",
            order_index=9
        ),
        StaffMember(
            name="Juan Vallejos",
            role="Encargado de Informática",
            email="it@escuelaaurora.cl",
            order_index=10
        ),
        StaffMember(
            name="Alicia Catrilaf Huenchulaf",
            role="Asistente de la Educación",
            email="a.catrilaf@educunco.cl",
            order_index=11
        ),
        StaffMember(
            name="Juan Trecanao Cheuqueo",
            role="Asistente de la Educación",
            email="j.trecanao@educunco.cl",
            order_index=12
        ),
        StaffMember(
            name="Ulda Inostroza Arias",
            role="Asistente de la Educación",
            email="u.inostroza@educunco.cl",
            order_index=13
        ),
        StaffMember(
            name="Alexis Candia Burgos",
            role="Asistente de la Educación",
            email="a.candia@educunco.cl",
            order_index=14
        ),
        StaffMember(
            name="Camila Olave Marín",
            role="Asistente de la Educación",
            email="c.olave@educunco.cl",
            order_index=15
        ),
        StaffMember(
            name="Vanesa Jara Matus",
            role="Asistente de la Educación",
            email="v.jara@educunco.cl",
            order_index=16
        ),
        StaffMember(
            name="Gloria Sepúlveda Lagos",
            role="Asistente de la Educación",
            email="g.sepulveda@educunco.cl",
            order_index=17
        ),
        
    ]

def get_staff_as_dicts():
    """Convierte la lista de objetos StaffMember a diccionarios para compatibilidad con las plantillas."""
    return [member.__dict__ for member in get_local_staff_list()]
