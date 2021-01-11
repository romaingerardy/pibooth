import json

from pibooth.config import PiConfigParser

# person = '{"name": "Bob", "languages": ["English", "Fench"]}'
config = '{"version":"2.0.1","general":{"language":"fr","directory":"~/Pictures/pibooth","debug":false,"plugins":null,"vkeyboard":true},"window":{"size":"(1920, 1080)","background":{"background_type":"color","background_color":"(255, 255, 255)","background_path":null},"text_color":"(0, 0, 0)","flash":true,"animate":true,"animate_delay":3,"final_image_delay":-1,"arrows":"bottom","arrows_x_offset":0,"preview_delay":3,"preview_countdown":true,"preview_stop_on_capture":false},"picture":{"orientation":"auto","captures":"(1, 4)","captures_effects":"cartoon","captures_cropping":false,"margin_thick":100,"footer_text1":"Pix Me Box","footer_text2":"Premi\u00e8re photo","text_colors":"(0, 0, 0)","text_fonts":"(Amatic-Bold, AmaticSC-Regular)","text_alignments":"center","overlays":null,"backgrounds":"(255, 255, 255)"},"camera":{"iso":100,"flip":false,"rotation":0,"resolution":"(1934, 2464)","delete_internal_memory":false},"printer":{"printer_name":"default","printer_delay":30,"max_pages":10,"max_duplicates":0,"pictures_per_page":1},"controls":{"debounce_delay":0.3,"multi_press_delay":0.5,"picture_btn_pin":11,"picture_led_pin":7,"print_btn_pin":13,"print_led_pin":15}}'
config_dict = json.loads(config)

print(config_dict)
print('')
print(config_dict['version'])

# plugin_manager = create_plugin_manager()
config = PiConfigParser("~/.config/pibooth/pibooth.cfg", None)

# **************
# GENERAL
# **************

general = config_dict['general']

config.set('GENERAL', 'language', general['language'])
config.set('GENERAL', 'directory', general['directory'])
config.set('GENERAL', 'debug', general['debug'])
config.set('GENERAL', 'plugins', general['plugins'])
config.set('GENERAL', 'vkeyboard', general['vkeyboard'])

# **************
# WINDOW
# **************

window = config_dict['window']

config.set('WINDOW', 'size', window['size'])
config.set('WINDOW', 'text_color', window['text_color'])
config.set('WINDOW', 'flash', window['flash'])
config.set('WINDOW', 'animate', window['animate'])
config.set('WINDOW', 'animate_delay', window['animate_delay'])
config.set('WINDOW', 'final_image_delay', window['final_image_delay'])
config.set('WINDOW', 'arrows', window['arrows'])
config.set('WINDOW', 'arrows_x_offset', window['arrows_x_offset'])
config.set('WINDOW', 'preview_delay', window['preview_delay'])
config.set('WINDOW', 'preview_countdown', window['preview_countdown'])
config.set('WINDOW', 'preview_stop_on_capture', window['preview_stop_on_capture'])

background = window['background']
if background['background_type'] == 'path' and background['background_path']:
    config.set('WINDOW', 'background', background['background_path'])
elif background['background_type'] == 'color' and background['background_color']:
    config.set('WINDOW', 'background', background['background_color'])
else:
    config.set('WINDOW', 'background', '(255, 255, 255')


# **************
# PICTURE
# **************

picture = config_dict['picture']

config.set('PICTURE', 'orientation', picture['orientation'])
config.set('PICTURE', 'captures', picture['captures'])
config.set('PICTURE', 'captures_effects', picture['captures_effects'])
config.set('PICTURE', 'captures_cropping', picture['captures_cropping'])
config.set('PICTURE', 'margin_thick', picture['margin_thick'])
config.set('PICTURE', 'footer_text1', picture['footer_text1'])
config.set('PICTURE', 'footer_text2', picture['footer_text2'])
config.set('PICTURE', 'text_colors', picture['text_colors'])
config.set('PICTURE', 'text_fonts', picture['text_fonts'])
config.set('PICTURE', 'text_alignments', picture['text_alignments'])
config.set('PICTURE', 'overlays', picture['overlays'])
config.set('PICTURE', 'backgrounds', picture['backgrounds'])



config.save()
