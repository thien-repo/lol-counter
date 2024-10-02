from dataclasses import dataclass
import config

import json


query_data = create_player_query_from_template( config.player['templates_query'], 'reap', 1 )


