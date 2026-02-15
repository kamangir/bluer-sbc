from bluer_objects.README.items import ImageItems

from bluer_sbc.README.designs.shelter import image_template

items = ImageItems(
    {image_template.format(f"{index+1:02}.png"): "" for index in range(4)}
) + ImageItems(
    {
        image_template.format("20251005_180841.jpg"): "",
        image_template.format("20251006_181432.jpg"): "",
        image_template.format("20251006_181509.jpg"): "",
        image_template.format("20251006_181554.jpg"): "",
        image_template.format("20251028_113245.jpg"): "",
        image_template.format("20251103_182323.jpg"): "",
        image_template.format("20251104_000755.jpg"): "",
        image_template.format("20251109_000501.jpg"): "",
        image_template.format("20251109_000641.jpg"): "",
        image_template.format("20251109_002124.jpg"): "",
        image_template.format("20251109_002639.jpg"): "",
        image_template.format("20251124_094744.jpg"): "",
        image_template.format("20251202_101949.jpg"): "",
        image_template.format("20251202_102912.jpg"): "",
        image_template.format("20251231_095746.jpg"): "",
        image_template.format("20251231_100222.jpg"): "",
        image_template.format("20251231_100305.jpg"): "",
    }
)
