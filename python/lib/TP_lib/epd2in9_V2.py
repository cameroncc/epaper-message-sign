# *****************************************************************************
# * | File        :	  epd2in9_V2.py
# * | Author      :   Waveshare team
# * | Function    :   Electronic paper driver
# * | Info        :
# *----------------
# * | This version:   V1.0
# * | Date        :   2020-10-20
# # | Info        :   python demo
# -----------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import logging
from . import epdconfig
import numpy as np

# Display resolution
EPD_WIDTH = 128
EPD_HEIGHT = 296


class EPD_2IN9_V2:
    def __init__(self):
        self.reset_pin = epdconfig.EPD_RST_PIN
        self.dc_pin = epdconfig.EPD_DC_PIN
        self.busy_pin = epdconfig.EPD_BUSY_PIN
        self.cs_pin = epdconfig.EPD_CS_PIN
        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT
        epdconfig.address = 0x48

    WF_PARTIAL_2IN9 = [
        0x0,
        0x40,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x80,
        0x80,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x40,
        0x40,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x80,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0A,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x1,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x1,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x22,
        0x22,
        0x22,
        0x22,
        0x22,
        0x22,
        0x0,
        0x0,
        0x0,
        0x22,
        0x17,
        0x41,
        0xB0,
        0x32,
        0x36,
    ]

    WF_PARTIAL_2IN9_Wait = [
        0x0,
        0x40,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x80,
        0x80,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x40,
        0x40,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x80,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0A,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x2,
        0x1,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x1,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x0,
        0x22,
        0x22,
        0x22,
        0x22,
        0x22,
        0x22,
        0x0,
        0x0,
        0x0,
        0x22,
        0x17,
        0x41,
        0xB0,
        0x32,
        0x36,
    ]

    Gray4 = [
        0x00,
        0x60,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x20,
        0x60,
        0x10,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x28,
        0x60,
        0x14,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x2A,
        0x60,
        0x15,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x90,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x02,
        0x00,
        0x05,
        0x14,
        0x00,
        0x00,
        0x1E,
        0x1E,
        0x00,
        0x00,
        0x00,
        0x00,
        0x01,
        0x00,
        0x02,
        0x00,
        0x05,
        0x14,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x24,
        0x22,
        0x22,
        0x22,
        0x23,
        0x32,
        0x00,
        0x00,
        0x00,
        0x22,
        0x17,
        0x41,
        0xAE,
        0x32,
        0x28,
    ]

    WF_FULL = [
        0x90,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x60,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x90,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x60,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x19,
        0x19,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x00,
        0x24,
        0x42,
        0x22,
        0x22,
        0x23,
        0x32,
        0x00,
        0x00,
        0x00,
        0x22,
        0x17,
        0x41,
        0xAE,
        0x32,
        0x38,
    ]

    # Hardware reset
    def reset(self):
        epdconfig.digital_write(self.reset_pin, 1)
        epdconfig.delay_ms(20)
        epdconfig.digital_write(self.reset_pin, 0)
        epdconfig.delay_ms(2)
        epdconfig.digital_write(self.reset_pin, 1)
        epdconfig.delay_ms(20)

    def send_command(self, command):
        epdconfig.digital_write(self.dc_pin, 0)
        epdconfig.digital_write(self.cs_pin, 0)
        epdconfig.spi_writebyte([command])
        epdconfig.digital_write(self.cs_pin, 1)

    def send_data(self, data):
        epdconfig.digital_write(self.dc_pin, 1)
        epdconfig.digital_write(self.cs_pin, 0)
        epdconfig.spi_writebyte([data])
        epdconfig.digital_write(self.cs_pin, 1)

    def send_data2(self, data):
        epdconfig.digital_write(self.dc_pin, 1)
        epdconfig.digital_write(self.cs_pin, 0)
        epdconfig.spi_writebyte2(data)
        epdconfig.digital_write(self.cs_pin, 1)

    def ReadBusy(self):
        # logging.debug("e-Paper busy")
        while epdconfig.digital_read(self.busy_pin) == 1:  #  0: idle, 1: busy
            epdconfig.delay_ms(0.1)
        # logging.debug("e-Paper busy release")

    def TurnOnDisplay(self):
        self.send_command(0x22)  # DISPLAY_UPDATE_CONTROL_2
        self.send_data(0xF7)
        self.send_command(0x20)  # MASTER_ACTIVATION
        self.ReadBusy()

    def TurnOnDisplay_Partial(self):
        self.send_command(0x22)  # DISPLAY_UPDATE_CONTROL_2
        self.send_data(0x0F)
        self.send_command(0x20)  # MASTER_ACTIVATION
        # self.ReadBusy()

    def TurnOnDisplay_Partial_Wait(self):
        self.send_command(0x22)  # DISPLAY_UPDATE_CONTROL_2
        self.send_data(0x0F)
        self.send_command(0x20)  # MASTER_ACTIVATION
        self.ReadBusy()

    def TurnOnDisplay_4Gray(self):
        self.send_command(0x22)  # DISPLAY_UPDATE_CONTROL_2
        self.send_data(0xC7)
        self.send_command(0x20)  # MASTER_ACTIVATION
        self.ReadBusy()

    def SendLut(self, lut):
        self.send_command(0x32)
        # for i in range(0, 153):
        # self.send_data(self.WF_PARTIAL_2IN9[i])
        if lut:
            self.send_data2(self.WF_PARTIAL_2IN9)
        else:
            self.send_data2(self.WF_PARTIAL_2IN9_Wait)
        self.ReadBusy()

    def lut(self, lut):
        self.send_command(0x32)
        for i in range(0, 153):
            self.send_data(lut[i])
        self.ReadBusy()

    def SetLut(self, lut):
        self.lut(lut)
        self.send_command(0x3F)
        self.send_data(lut[153])
        self.send_command(0x03)  # gate voltage
        self.send_data(lut[154])
        self.send_command(0x04)  # source voltage
        self.send_data(lut[155])  # VSH
        self.send_data(lut[156])  # VSH2
        self.send_data(lut[157])  # VSL
        self.send_command(0x2C)  # VCOM
        self.send_data(lut[158])

    def SetWindow(self, x_start, y_start, x_end, y_end):
        self.send_command(0x44)  # SET_RAM_X_ADDRESS_START_END_POSITION
        # x point must be the multiple of 8 or the last 3 bits will be ignored
        self.send_data((x_start >> 3) & 0xFF)
        self.send_data((x_end >> 3) & 0xFF)
        self.send_command(0x45)  # SET_RAM_Y_ADDRESS_START_END_POSITION
        self.send_data(y_start & 0xFF)
        self.send_data((y_start >> 8) & 0xFF)
        self.send_data(y_end & 0xFF)
        self.send_data((y_end >> 8) & 0xFF)

    def SetCursor(self, x, y):
        self.send_command(0x4E)  # SET_RAM_X_ADDRESS_COUNTER
        # x point must be the multiple of 8 or the last 3 bits will be ignored
        self.send_data(x & 0xFF)

        self.send_command(0x4F)  # SET_RAM_Y_ADDRESS_COUNTER
        self.send_data(y & 0xFF)
        self.send_data((y >> 8) & 0xFF)
        self.ReadBusy()

    def init(self):
        if epdconfig.module_init() != 0:
            return -1
        # EPD hardware init start
        self.reset()

        self.ReadBusy()
        self.send_command(0x12)  # SWRESET
        self.ReadBusy()

        self.send_command(0x01)  # Driver output control
        self.send_data(0x27)
        self.send_data(0x01)
        self.send_data(0x00)

        self.send_command(0x11)  # data entry mode
        self.send_data(0x03)

        self.SetWindow(0, 0, self.width - 1, self.height - 1)

        self.send_command(0x21)  #  Display update control
        self.send_data(0x00)
        self.send_data(0x80)

        self.SetCursor(0, 0)
        self.ReadBusy()
        # EPD hardware init end
        return 0

    def init_Fast(self):
        if epdconfig.module_init() != 0:
            return -1
        # EPD hardware init start
        self.reset()

        self.ReadBusy()
        self.send_command(0x12)  # SWRESET
        self.ReadBusy()

        self.send_command(0x01)  # Driver output control
        self.send_data(0x27)
        self.send_data(0x01)
        self.send_data(0x00)

        self.send_command(0x11)  # data entry mode
        self.send_data(0x03)

        self.SetWindow(0, 0, self.width - 1, self.height - 1)

        self.send_command(0x3C)
        self.send_data(0x05)

        self.send_command(0x21)  #  Display update control
        self.send_data(0x00)
        self.send_data(0x80)

        self.SetCursor(0, 0)
        self.ReadBusy()

        self.SetLut(self.WF_FULL)
        # EPD hardware init end
        return 0

    def Init_4Gray(self):
        if epdconfig.module_init() != 0:
            return -1
        self.reset()
        epdconfig.delay_ms(100)

        self.ReadBusy()
        self.send_command(0x12)  # SWRESET
        self.ReadBusy()

        self.send_command(0x01)  # Driver output control
        self.send_data(0x27)
        self.send_data(0x01)
        self.send_data(0x00)

        self.send_command(0x11)  # data entry mode
        self.send_data(0x03)

        self.SetWindow(8, 0, self.width, self.height - 1)

        self.send_command(0x3C)
        self.send_data(0x04)

        self.SetCursor(1, 0)
        self.ReadBusy()

        self.SetLut(self.Gray4)
        # EPD hardware init end
        return 0

    def getbuffer(self, image):
        # logging.debug("bufsiz = ",int(self.width/8) * self.height)
        buf = [0xFF] * (int(self.width / 8) * self.height)
        image_monocolor = image.convert("1")
        imwidth, imheight = image_monocolor.size
        pixels = image_monocolor.load()
        # logging.debug("imwidth = %d, imheight = %d",imwidth,imheight)
        if imwidth == self.width and imheight == self.height:
            # logging.debug("Vertical")
            for y in range(imheight):
                for x in range(imwidth):
                    # Set the bits for the column of pixels at the current position.
                    if pixels[x, y] == 0:
                        buf[int((x + y * self.width) / 8)] &= ~(0x80 >> (x % 8))
        elif imwidth == self.height and imheight == self.width:
            # logging.debug("Horizontal")
            for y in range(imheight):
                for x in range(imwidth):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0:
                        buf[int((newx + newy * self.width) / 8)] &= ~(0x80 >> (y % 8))
        return buf

    def getbuffer_4Gray(self, image):
        # logger.debug("bufsiz = ",int(self.width/8) * self.height)
        buf = [0xFF] * (int(self.width / 4) * self.height)
        image_monocolor = image.convert("L")
        imwidth, imheight = image_monocolor.size
        pixels = image_monocolor.load()
        i = 0
        # logger.debug("imwidth = %d, imheight = %d",imwidth,imheight)
        if imwidth == self.width and imheight == self.height:
            # logger.debug("Vertical")
            for y in range(imheight):
                for x in range(imwidth):
                    # Set the bits for the column of pixels at the current position.
                    if pixels[x, y] == 0xC0:
                        pixels[x, y] = 0x80
                    elif pixels[x, y] == 0x80:
                        pixels[x, y] = 0x40
                    i = i + 1
                    if i % 4 == 0:
                        buf[int((x + (y * self.width)) / 4)] = (
                            (pixels[x - 3, y] & 0xC0)
                            | (pixels[x - 2, y] & 0xC0) >> 2
                            | (pixels[x - 1, y] & 0xC0) >> 4
                            | (pixels[x, y] & 0xC0) >> 6
                        )

        elif imwidth == self.height and imheight == self.width:
            # logger.debug("Horizontal")
            for x in range(imwidth):
                for y in range(imheight):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0xC0:
                        pixels[x, y] = 0x80
                    elif pixels[x, y] == 0x80:
                        pixels[x, y] = 0x40
                    i = i + 1
                    if i % 4 == 0:
                        buf[int((newx + (newy * self.width)) / 4)] = (
                            (pixels[x, y - 3] & 0xC0)
                            | (pixels[x, y - 2] & 0xC0) >> 2
                            | (pixels[x, y - 1] & 0xC0) >> 4
                            | (pixels[x, y] & 0xC0) >> 6
                        )
        return buf

    def display(self, image):
        if image == None:
            return
        self.send_command(0x24)  # WRITE_RAM
        # for j in range(0, self.height):
        # for i in range(0, int(self.width / 8)):
        # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)
        self.TurnOnDisplay()

    def display_Base(self, image):
        if image == None:
            return

        self.send_command(0x24)  # WRITE_RAM
        # for j in range(0, self.height):
        # for i in range(0, int(self.width / 8)):
        # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)

        self.send_command(0x26)  # WRITE_RAM
        # for j in range(0, self.height):
        # for i in range(0, int(self.width / 8)):
        # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)

        self.TurnOnDisplay()

    def display_Partial(self, image):
        if image == None:
            return

        # epdconfig.digital_write(self.reset_pin, 0)
        # epdconfig.delay_ms(2)
        # epdconfig.digital_write(self.reset_pin, 1)
        # epdconfig.delay_ms(2)

        self.SendLut(1)
        self.send_command(0x37)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x40)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)

        self.send_command(0x3C)  # BorderWavefrom
        self.send_data(0x80)

        self.send_command(0x22)
        self.send_data(0xC0)
        self.send_command(0x20)
        self.ReadBusy()

        self.SetWindow(0, 0, self.width - 1, self.height - 1)
        self.SetCursor(0, 0)

        self.send_command(0x24)  # WRITE_RAM
        # for j in range(0, self.height):
        # for i in range(0, int(self.width / 8)):
        # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)

        self.TurnOnDisplay_Partial()

    def display_Partial_Wait(self, image):
        if image == None:
            return

        epdconfig.digital_write(self.reset_pin, 0)
        epdconfig.delay_ms(1)
        epdconfig.digital_write(self.reset_pin, 1)
        # epdconfig.delay_ms(2)

        self.SendLut(0)
        self.send_command(0x37)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x40)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)
        self.send_data(0x00)

        self.send_command(0x3C)  # BorderWavefrom
        self.send_data(0x80)

        self.send_command(0x22)
        self.send_data(0xC0)
        self.send_command(0x20)
        self.ReadBusy()

        self.SetWindow(0, 0, self.width - 1, self.height - 1)
        self.SetCursor(0, 0)

        self.send_command(0x24)  # WRITE_RAM
        # for j in range(0, self.height):
        # for i in range(0, int(self.width / 8)):
        # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)

        self.TurnOnDisplay_Partial_Wait()

    def Clear(self, color):
        self.send_command(0x24)  # WRITE_RAM
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(color)
        self.TurnOnDisplay()

    def display_4Gray(self, image):
        self.send_command(0x24)
        for i in range(0, 4736):
            temp3 = 0
            for j in range(0, 2):
                temp1 = image[i * 2 + j]
                for k in range(0, 2):
                    temp2 = temp1 & 0xC0
                    if temp2 == 0xC0:
                        temp3 |= 0x00
                    elif temp2 == 0x00:
                        temp3 |= 0x01
                    elif temp2 == 0x80:
                        temp3 |= 0x01
                    else:  # 0x40
                        temp3 |= 0x00
                    temp3 <<= 1

                    temp1 <<= 2
                    temp2 = temp1 & 0xC0
                    if temp2 == 0xC0:
                        temp3 |= 0x00
                    elif temp2 == 0x00:
                        temp3 |= 0x01
                    elif temp2 == 0x80:
                        temp3 |= 0x01
                    else:  # 0x40
                        temp3 |= 0x00
                    if j != 1 or k != 1:
                        temp3 <<= 1
                    temp1 <<= 2
            self.send_data(temp3)

        self.send_command(0x26)
        for i in range(0, 4736):
            temp3 = 0
            for j in range(0, 2):
                temp1 = image[i * 2 + j]
                for k in range(0, 2):
                    temp2 = temp1 & 0xC0
                    if temp2 == 0xC0:
                        temp3 |= 0x00
                    elif temp2 == 0x00:
                        temp3 |= 0x01
                    elif temp2 == 0x80:
                        temp3 |= 0x00
                    else:  # 0x40
                        temp3 |= 0x01
                    temp3 <<= 1

                    temp1 <<= 2
                    temp2 = temp1 & 0xC0
                    if temp2 == 0xC0:
                        temp3 |= 0x00
                    elif temp2 == 0x00:
                        temp3 |= 0x01
                    elif temp2 == 0x80:
                        temp3 |= 0x00
                    else:  # 0x40
                        temp3 |= 0x01
                    if j != 1 or k != 1:
                        temp3 <<= 1
                    temp1 <<= 2
            self.send_data(temp3)

        self.TurnOnDisplay_4Gray()

    def sleep(self):
        self.send_command(0x10)  # DEEP_SLEEP_MODE
        self.send_data(0x01)

    def Dev_exit(self):
        epdconfig.module_exit()


### END OF FILE ###
