from datetime import datetime

from src.configparser import ConfigParser


class Header(ConfigParser):
    def __init__(self, config):
        self.config = config

    def create_main_header(self):
        file_object = open(self.config.output_file_name, 'w')
        file_object.write('Instrument_Type   : BPM\n')
        file_object.write('Command_ID        : SIMULATION\n')
        file_object.write('File_type         : SIMULATION\n')
        file_object.write('File_ID           : *\n')
        file_object.write('File_Version      : *\n')
        file_object.write('Timestamp         : ' + str(datetime.today().strftime('%a %b %d %I:%M:%S %Y')) + '\n')
        file_object.write('Core_commstruct_v : **********\n')
        file_object.write('Plat_commstruct_v : **********\n')
        file_object.write('Bunch_Patt_Name   : ****\n')
        file_object.write(
            'Bunch_Patt_(hex)  : * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n')
        file_object.write('Species           : SIMULATION\n')
        file_object.write('Num_Instruments   : 3\n')
        file_object.write('Number_of_Bunches : *\n')
        file_object.write('Number_of_Turns   : ' + str(self.config.n_turns) + '\n')
        file_object.write('Turn_Spacing      : *\n')
        file_object.write('Timing_Setup      : *\n')
        file_object.write('Trigger           : ****\n')
        file_object.write('\n')
        file_object.write('CESR CONDX        : ******\n')
        file_object.write('CERN Current Raw  : ***\n')
        file_object.write('CERN Current mA   : ***\n')
        file_object.write('\n')

    def create_cbpm_header(self, idx_cbpm):
        file_object = open(self.config.output_file_name, 'a')
        file_object.write('Location          : ' + self.config.cbpm[idx_cbpm] + '\n')
        file_object.write('BPM_hostname      : ********\n')
        file_object.write('BPM_IP_Address    : ***.***.**.**\n')
        file_object.write('Detector_Type     : ***\n')
        file_object.write('Detector_Coeffs   : *** ***\n')
        file_object.write('EXE_Name          : ***\n')
        file_object.write('EXE_Build_ID      : **********\n')
        file_object.write('Dig.Board_FPGA    : ***\n')
        file_object.write('Front-End_FPGAs   : ** ** ** **\n')
        file_object.write('Timing_Setup      : ***\n')
        file_object.write('Number_of_Turns   : ' + str(self.config.n_turns) + '\n')
        file_object.write('Turn_sync_counter : ******\n')
        file_object.write('Turn_spacing      : *\n')
        file_object.write('Trigger           : ***\n')
        file_object.write('Bunch_Pat_offsets : *** ***\n')
        file_object.write('Com_Turnmrk_Dly   : *\n')
        file_object.write('Blk_Turnmrk_Dlys  : * *\n')
        file_object.write('Block_Delays      : *** ****\n')
        file_object.write('Channel_Delays    : *** *** *** *** *** *** *** ***\n')
        file_object.write('Gain_Settings     : * * * *    * * * *\n')
        file_object.write('Gain_Codes        : * * * *    * * * *\n')
        file_object.write('Gain_Coeffs       : * * * * * * * *\n')
        file_object.write('Pedestals         : * * * * * * * *\n')
        file_object.write('Digital_Temp_C    : *\n')
        file_object.write('Card_Temps_C      : * * * *\n')
        file_object.write('ADC_saturation    : ****    ****\n')
        file_object.write('ADC_High          : ****    ****\n')
        file_object.write('ADC_Low           : ****    ****\n')
        file_object.write('# Timing  Encoded     Card-0   Card-1   Card-2   Card-3\n')
        file_object.write('# Block  Phase word   b3(TI)   b1(BI)   b2(BO)   b4(TO)\n')
        file_object.write('--BEGIN DATA--\n')
