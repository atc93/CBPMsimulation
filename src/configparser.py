import json
import re
import sys
from pprint import pprint


# read in configuration file

class ConfigParser:

    def parse_config(self):
        with open(sys.argv[1]) as config_file:
            comment_pattern = r"(?m)^\s*#.*\n?"
            config_text = re.sub(comment_pattern, "", config_file.read())
            config = json.loads(config_text)

        self.output_file_name = config['output_file_name']
        self.verbose = config['verbose']
        self.n_turns = config['n_turns']
        self.x_pos = config['x_pos']
        self.y_pos = config['y_pos']
        self.x_drift = config['x_drift']
        self.y_drift = config['y_drift']
        self.x_modulation_std = config['x_modulation_std']
        self.y_modulation_std = config['y_modulation_std']
        self.x_modulation_freq = config['x_modulation_freq']
        self.y_modulation_freq = config['y_modulation_freq']
        self.kx = config['kx']
        self.ky = config['ky']
        self.amplitude = config['amplitude']
        self.frequency = config['frequency']
        self.timing_offset = config['timing_offset']
        self.corr_timing_jitter = config['corr_timing_jitter']
        self.uncorr_timing_jitter = config['uncorr_timing_jitter']
        self.timing_jitter_correlated = config['timing_jitter_correlated']
        self.noise = config['noise']
        self.cbpm = config['cbpm'].split()
        self.n_cbpm = len(self.cbpm)
        self.apply_noise = config['apply_noise']
        self.apply_timing_jitter = config['apply_timing_jitter']
        self.apply_timing_offset = config['apply_timing_offset']

    def check_config(self):
        if self.verbose > 2:
            self.dump()

    def dump(self):
        pprint(vars(self))
