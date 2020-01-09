import sys

from src.beam import Beam
from src.button import Button
from src.configparser import ConfigParser
from src.header import Header
from src.printout import welcome_message


def main():
    # retrieve configuration file information
    config = ConfigParser()
    config.parse_config()
    config.check_config()

    # create header
    header = Header(config)
    header.create_main_header()

    button = []
    beam = []

    # loop over the cbpm(s)
    for idx_cbpm in range(len(config.cbpm)):

        # open output text file to append cbpm data
        file_object = open(config.output_file_name, 'a')
        # create cbpm specific header
        header.create_cbpm_header(idx_cbpm)

        # create class instances
        button.append(Button(config))
        beam.append(Beam(config))

        # loop over the turn(s)
        for idx_turn in range(config.n_turns):
            # retrieve x,y position for a given turn
            x_pos, y_pos = beam[idx_cbpm].get_beam_position(idx_cbpm, idx_turn)

            # retrieve button reading given beam position
            button_reading = button[idx_cbpm].get_reading(x_pos, y_pos, idx_cbpm)

            # write button reading to output text file
            file_object.write('0       0000000     ' +
                              str(button_reading[0]) + '     ' +
                              str(button_reading[1]) + '     ' +
                              str(button_reading[2]) + '     ' +
                              str(button_reading[3]) + '     \n')


if __name__ == '__main__':

    # print welcome message
    welcome_message()

    # check that the configuration file was provided
    # exit if not provided
    if len(sys.argv) < 2:
        print(' RUNNING ERROR -- configuration file must be provided via command line argument')
        sys.exit(0)

    # run the analysis for associated configuration file
    sys.exit(main())
