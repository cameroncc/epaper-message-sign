#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys

# Set up paths (adjust these if your directory structure is different)
picdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "pic/2in13"
)
fontdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "fonts"
)
libdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "lib"
)

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging

# import random
import time
import traceback

from PIL import Image, ImageDraw, ImageFont
from TP_lib import epd2in13_V4

logging.basicConfig(level=logging.DEBUG)

partial_refresh_count = 0
first_run = True


def display_message(message: str, full_update=False):
    try:
        logging.info("Starting simple quote display")

        # Initialize the e-paper display
        epd = epd2in13_V4.EPD()

        global first_run
        global partial_refresh_count

        if first_run or full_update or partial_refresh_count > 5:
            logging.info("Initializing display...")
            epd.init(epd.FULL_UPDATE)
            partial_refresh_count = 0
            logging.info("resetting partial_refresh_count")
        else:
            logging.info("Partial display refresh...")
            epd.init(epd.PART_UPDATE)
            partial_refresh_count += 1
            logging.info(f"that's {partial_refresh_count} partial refreshes")

        if first_run:
            logging.info("first run, whiting out display")
            epd.Clear(0xFF)  # Clear with white background
            first_run = False

        # Create a new image with white background
        # The display is 122x250 pixels
        image = Image.new("1", (epd.height, epd.width), 255)  # 255 = white background
        draw = ImageDraw.Draw(image)

        # Load fonts - try different sizes
        try:
            font_large = ImageFont.truetype(
                os.path.join(fontdir, "fira_code/FiraCode-Regular.ttf"), 32
            )
            print("successfully loaded firacode")
        except:
            # Fallback to default font if custom font not found
            font_large = ImageFont.load_default()
            print("failed to load firacode. Using default font")

        # Simple message
        # num = random.randint(0, 1)
        quote_text = message  # "In a meeting" if num else "Free"

        # Get text dimensions for centering
        quote_bbox = draw.textbbox((0, 0), quote_text, font=font_large)

        quote_width = quote_bbox[2] - quote_bbox[0]
        quote_height = quote_bbox[3] - quote_bbox[1]

        # Calculate positions for centering
        display_width = epd.height  # 122
        display_height = epd.width  # 250

        # Center both lines with spacing
        total_text_height = quote_height
        start_y = (display_height - total_text_height) // 2

        quote_x = (display_width - quote_width) // 2
        quote_y = start_y

        # Draw the text
        draw.text((quote_x, quote_y), quote_text, font=font_large, fill=0)  # 0 = black

        # Display the image
        logging.info("Displaying message...")
        epd.display(epd.getbuffer(image))

        logging.info("Message displayed successfully!")
        logging.info(
            "The display will remain showing the quote until you run another script or power off."
        )

        # Put the display to sleep to save power
        time.sleep(2)
        epd.sleep()
        print()
        print()

    except IOError as e:
        logging.error(f"IO Error: {e}")

    except KeyboardInterrupt:
        logging.info("Interrupted by user")
        epd.sleep()

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        traceback.print_exc()


def clean_up_display_resources():
    try:
        epd = epd2in13_V4.EPD()
        print("cleaning up display resources")
        epd.Dev_exit()
    except Exception as e:
        print(f"cleanup raised an exception {e}. {traceback.format_exc()}")


display_message("Free", full_update=True)
