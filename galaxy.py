#!/usr/bin/env python3
import colorschemes

NUM_LED = 18


while True:

        MY_CYCLE = colorschemes.Solid(num_led=NUM_LED, pause_value=60,
                             num_steps_per_cycle=1, num_cycles=1)
        MY_CYCLE.start()