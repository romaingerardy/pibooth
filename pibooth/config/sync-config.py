import json
from pibooth.config import PiConfigParser

#person = '{"name": "Bob", "languages": ["English", "Fench"]}'
config = '{"version":"2.0.1","general":{"language":"fr","directory":"pibooth","debug":false,"plugins":null,"vkeyboard":true},"window":{"size":"(1920, 1080)","background":{"background_type":"color","background_color":"(255, 255, 255)","background_path":null},"text_color":"(0, 0, 0)","flash":true,"animate":true,"animate_delay":3,"final_image_delay":-1,"arrows":"bottom","arrows_x_offset":0,"preview_delay":3,"preview_countdown":true,"preview_stop_on_capture":false},"picture":{"orientation":"auto","captures":"(1, 4)","captures_effects":"cartoon","captures_cropping":false,"margin_thick":100,"footer_text1":"Pix Me Box","footer_text2":"Premi\u00e8re photo","text_colors":"(0, 0, 0)","text_fonts":"(Amatic-Bold, AmaticSC-Regular)","text_alignments":"center","overlays":null,"backgrounds":"(255, 255, 255)"},"camera":{"iso":100,"flip":false,"rotation":0,"resolution":"(1934, 2464)","delete_internal_memory":false},"printer":{"printer_name":"default","printer_delay":30,"max_pages":10,"max_duplicates":0,"pictures_per_page":1},"controls":{"debounce_delay":0.3,"multi_press_delay":0.5,"picture_btn_pin":11,"picture_led_pin":7,"print_btn_pin":13,"print_led_pin":15}}'
config_dict = json.loads(config)

print(config_dict)
print('')
# Output: ['English', 'French']
print(config_dict['version'])

general = config_dict['general']

print(general['language'])

#plugin_manager = create_plugin_manager()
config = PiConfigParser("~/.config/pibooth/pibooth.cfg", None)

config.set('GENERAL', 'language', general['language'])
config.save()

#self.cfg.set(kwargs['section'], kwargs['option'], str(value[0]))