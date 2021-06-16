## GameObject

| Attribute | Description |
| --- | --- |
| id  | A unique id that identifies this specific object | 
| object_type | What type of object it is |
| name | A string that represents what **type** the object is |
| world_y | Y position in world |
| world_x | X position in world |
| orientation | What orientation the objects has |

### object_type == 'Environment'


### object_type == 'Npc'
| hp | Current Hitpoints for the object |
| level | The level of the npc |
| state | What state the object is, attacking, idle etc |
| hostile | If the npc is hostile or friendly |
| aggresive | If the npc is aggressive or not |

### object_type == 'Player'
The `player` object has all the traits that `npc` has as well as:
| gearpieces | The gear of the player |
| hp | Current Hitpoints for the object |
| level | The level of the npc |
| state | What state the object is, attacking, idle etc |
| skills | All the skills of the player. |

Once you have the `name`, you can find the objects blueprint and retrieve the rest of the object information, including `size`, sprites etc.

