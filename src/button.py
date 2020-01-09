import math
import random

from src.configparser import ConfigParser


class Button(ConfigParser):

    def __init__(self, config):
        self.config = config

    def get_reading(self, x, y, idx_cbpm):

        self.button_reading = []

        # get readings from beam position
        self.raw_reading_from_beam_position(x, y, idx_cbpm)
        if self.config.verbose > 2:
            print(self.button_reading)

        # get scaled amplitude on sine wave pulse
        self.sine_wave_amplitude(idx_cbpm)
        if self.config.verbose > 2:
            print(self.button_reading)

        # add the electronic noise that is simulated
        # as a Gaussian gain error
        if self.config.apply_noise:
            self.gain_correction(idx_cbpm)
            if self.config.verbose > 2:
                print(self.button_reading)

        # extract digitized value with errors onn sine wave

        return self.button_reading

    def raw_reading_from_beam_position(self, x, y, idx_cbpm):

        self.button_reading.append(int(self.config.amplitude[idx_cbpm] * (1 - x / self.config.kx + y / self.config.ky)))
        self.button_reading.append(int(self.config.amplitude[idx_cbpm] * (1 - x / self.config.kx - y / self.config.ky)))
        self.button_reading.append(int(self.config.amplitude[idx_cbpm] * (1 + x / self.config.kx - y / self.config.ky)))
        self.button_reading.append(int(self.config.amplitude[idx_cbpm] * (1 + x / self.config.kx + y / self.config.ky)))

    def sine_wave_amplitude(self, idx_cbpm):

        jitter = 0.

        if self.config.timing_jitter_correlated and self.config.apply_timing_jitter:
            jitter = random.normalvariate(0,
                                          self.config.corr_timing_jitter[idx_cbpm + 4 * idx_cbpm] * 1e-12)  # unit of ps

        for i in range(4):

            if not self.config.timing_jitter_correlated and self.config.apply_timing_jitter:
                jitter = random.normalvariate(0,
                                              self.config.uncorr_timing_jitter[i + 4 * idx_cbpm] * 1e-12)  # unit of ps

            if self.config.apply_timing_offset:
                self.button_reading[i] = int(self.button_reading[i] * math.cos(
                    2 * math.pi * self.config.frequency * (
                            self.config.timing_offset[i + 4 * idx_cbpm] * 1e-12 + jitter)))
            else:
                self.button_reading[i] = int(self.button_reading[i] * math.cos(
                    2 * math.pi * self.config.frequency * (jitter)))

        return self.button_reading

    def gain_correction(self, idx_cbpm):

        for i in range(4):
            gain = random.normalvariate(1, self.config.noise[i + 4 * idx_cbpm] / self.button_reading[i])

            self.button_reading[i] = int(self.button_reading[i] * gain)

        return self.button_reading
