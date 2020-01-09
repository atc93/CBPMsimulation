import math

import src.constants as cst
from src.configparser import ConfigParser


class Beam(ConfigParser):

    def __init__(self, config):
        self.config = config

    def get_beam_position(self, idx_cbpm, idx_turn):

        # horizontal direction
        # initial horizontal beam position
        x = self.config.x_pos[idx_cbpm]

        # add drift
        x += self.config.x_drift[idx_cbpm] / (self.config.n_turns - 1) * idx_turn

        # add modulation(s)
        n_modulation = int(len(self.config.x_modulation_std) / self.config.n_cbpm)
        for i in range(n_modulation):
            modulation_index = idx_cbpm + self.config.n_cbpm * i
            # the sqrt(2) amplitude is to scale from standard deviation to amplitude
            x += math.sqrt(2) * self.config.x_modulation_std[modulation_index] * math.sin(
                2 * math.pi * self.config.x_modulation_freq[modulation_index] * idx_turn * cst.ring_revolution_period)

        # vertical direction
        # initial vertical beam position
        y = self.config.y_pos[idx_cbpm]

        # add drift
        y += self.config.y_drift[idx_cbpm] / (self.config.n_turns - 1) * idx_turn

        # add modulation(s)
        n_modulation = int(len(self.config.y_modulation_std) / self.config.n_cbpm)
        for i in range(n_modulation):
            modulation_index = idx_cbpm + self.config.n_cbpm * i
            # the sqrt(2) amplitude is to scale from standard deviation to amplitude
            y += math.sqrt(2) * self.config.y_modulation_std[modulation_index] * math.sin(
                2 * math.pi * self.config.y_modulation_freq[modulation_index] * idx_turn * cst.ring_revolution_period)

        return x, y
