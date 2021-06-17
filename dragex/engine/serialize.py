#from objects import BaseObject
#from objects import Player


class Serializer:

    def serialize(self):
        """ Serializes the object into XX. """
        pass

    def _serialize_object(self):
        return {
            'id': self.id,
            'object_type': self.__class__.__name__,
            'name': self.name,
            'world_y': self.position.y,
            'world_x': self.position.x,
            'orientation': self.position.orientation,
        }

    def _serialize_npc(self):
        return {
            **super().serialize(),
            'hp': self.hp,
            'level': self.level,
            'state': self.state,
            'hostile': self.hostile,
            'aggresive': self.aggresive,
        }


    def _serialize_player(self):
        return {
            **super().serialize(),
            'hp': self.hp,
            'level': self.level,
            'state': self.state,
            'gear': self.gear,
        }
