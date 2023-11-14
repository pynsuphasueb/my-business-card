from PIL import Image, ImageDraw, ImageFont


name = "sky"
title = "DATA ENGINEER"
phone = "+669 725 1144"
email = "pynsuphasueb@gmail.com"
medium_url = "medium.com/pynsuphasueb"
linkedin_url = "linkedin.com/in/pynsuphasueb"


font_heading = ImageFont.truetype("fonts/Lexend-Bold.ttf", 80)
font_sub_heading = ImageFont.truetype("fonts/Lexend-Medium.ttf", 18)
font_body = ImageFont.truetype("fonts/Lexend-Regular.ttf", 14)
font_body_bold = ImageFont.truetype("fonts/Lexend-Bold.ttf", 14)


card_width = 800
card_height = 400

card = Image.new("RGB", (card_width, card_height), "#ffc0cb")

draw = ImageDraw.Draw(card)

# Add left contents
draw.text((130, 130), name, fill="#ff0065", font=font_heading)
# draw.line((100, 220, 100, 250), fill="gray", width=3) # Add a green line
draw.text((140, 235), title, fill="#ff0065", font=font_sub_heading) # Adjust the position

# Add right contents -[1]- `text`
# draw.text((454, 160), f"t. {phone}", fill="white", font=font_body)
# draw.text((454, 180), f"e. {email}", fill="white", font=font_body)
# draw.text((454, 200), f"m. {medium_url}", fill="white", font=font_body)
# draw.text((454, 220), f"l. {linkedin_url}", fill="white", font=font_body)

# Add right contents -[2]- `multiline_text`
# draw.multiline_text(
#     (400, 160),
#     f"t. {phone}\ne. {email}\nm. {medium_url}\nl. {linkedin_url}",
#     fill="white",
#     font=font_body,
#     spacing=6,
# )

# Add right contents -[3]- `multiline_text` + alignment
contact_prepends = ["t.", "e.",  "m.", "l."]
draw.multiline_text(
    (400, 160),
    "\n".join(contact_prepends),
    fill="#ff0065",
    font=font_body_bold,
    spacing=6,
)
contact_texts = [phone, email, medium_url, linkedin_url]
draw.multiline_text(
    (422, 160),
    "\n".join(contact_texts),
    fill="white",
    font=font_body,
    spacing=6,
)
logo = Image.open("logo4.png").resize((60, 60))
card.paste(logo, (95, 223), logo)
qr_code = Image.open("my-qr.png").resize((80, 80))
card.paste(qr_code, (660, 160), qr_code)

card.show()
# Save the business card
card.save("card.png")