import logging
import unittest


class ParserTestCase(unittest.TestCase):

	def setUp(self):

		self.setting_string = """
[profile]
layer_height = 0.1
retraction_enable = False
solid_layer_thickness = 0.6
nozzle_size = 0.5
print_speed = 50
print_temperature = 220
print_temperature2 = 0
start2.gcode = ;Sliced at: {day} {date} {time}
	;Basic settings: Layer height: {layer_height} Walls: {wall_thickness} Fill: {fill_density}
	;Print time: {print_time}
	;Filament used: {filament_amount}m {filament_weight}g
	;Filament cost: {filament_cost}
	G21        ;metric values
	G90        ;absolute positioning
	M107       ;start with the fan off
	G28 X0 Y0  ;move X/Y to min endstops
	M117 Printing...
end2.gcode = ;End GCode
	M104 T0 S0                     ;extruder heater off
	M104 T1 S0                     ;extruder heater off
	M140 S0                     ;heated bed heater off (if you have it)
	G91                                    ;relative positioning
	G1 E-1 F300                            ;retract the filament a bit before lifting the nozzle, to release some of the pressure
	G1 Z+0.5 E-5 X-20 Y-20 F{travel_speed} ;move Z up a bit and retract filament even more
	G28 X0 Y0                              ;move X/Y to min endstops, so the head is out of the way
	M84                         ;steppers off
	G90                         ;absolute positioning
"""

	def test_process_setting_line(self):
		
		from octoprint.cura.parser import process_setting_line

		setting_line = "print_speed_size2 = 3.22"

		data = {}

		data = process_setting_line(data, setting_line)
		
		logging.info(data)
		self.assertEqual(len(data.values()), 1)

	def test_format_command(self):

		from octoprint.cura.parser import format_data_for_command

		data = {'layerHeight': '0.1',
				'printTemperature': '220'}

		result = []

		result = format_data_for_command(data)

		self.assertIsNotNone(result)
		self.assertEqual(len(result), len(data.values()) * 2)
		