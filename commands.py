# OS dependent commands
#  https://developer.valvesoftware.com/wiki/Console_Command_List
#  https://wiki.teamfortress.com/wiki/Scripting

import platform

# cfg by class
commands_config = {
    # for default state restoring
    "reset": {
        "base": [
            "r_drawviewmodel 1",
            "viewmodel_fov 90",
            'unbind "mouse3"',
        ],
    },
    "demoman.cfg": {
        "base": [
            "exec reset",
            'unbind "E"',
            "viewmodel_fov 60",
        ],
    },
    "soldier": {
        "base": [
            "exec reset",
            'unbind "E"',
            "viewmodel_fov 60",
        ],
        "linux": [
            # 1600 dpi sensitivity 1.45
            # 3200 dpi sensitivity 0.8
            "sensitivity 0.8",
        ],
        "windows": [
            "sensitivity 1.2",
        ],
    },
}


def generate_configuration(base_config: dict):
    system = platform.system().lower()
    final_config = {}

    for key in base_config:
        commands = base_config[key]["base"]
        os_variant_commands = base_config[key].get(system, [])
        commands = commands + os_variant_commands
        final_config[key] = commands

    return final_config


if __name__ == "__main__":
    from pprint import pprint

    pprint(generate_configuration(base_config=commands_config))

