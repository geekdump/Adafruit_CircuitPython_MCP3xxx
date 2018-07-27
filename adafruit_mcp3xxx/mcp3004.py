# The MIT License (MIT)
#
# Copyright (c) 2018 Brent Rubell for Adafruit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`mcp3004.py`
================================================
MCP3004 4-channel, 10-bit, analog-to-digital
converter instance.

* Author(s): Brent Rubell
"""

from .mcp3xxx import MCP3xxx

class MCP3004(MCP3xxx):
    """
    MCP3004 Pin Mapping.
    """
    pin_0 = 0
    pin_1 = 1
    pin_2 = 2
    pin_3 = 3
    max_pin = pin_3

    """
    MCP3004 Diff. Channel Mapping.
    """
    MCP3004_DIFF_PINS = {
        (0, 1) : pin_0,
        (1, 0) : pin_1,
        (2, 3) : pin_2,
        (3, 2) : pin_3
    }

    def __init__(self, spi_bus, cs, ref_voltage=3.3):
        super().__init__(spi_bus, cs, ref_voltage)
        self.ref_voltage = ref_voltage
