import math

paint_cans = int(input())
wallpaper_rolls = int(input())
pair_of_gloves_price = float(input())
paint_brush_price = float(input())

paint_can_price = 21.50
wallpaper_rolls_price = 5.20
pair_of_gloves_needed = math.ceil(wallpaper_rolls * 0.35)
paint_brush_needed = round(paint_cans * 0.48)

total_price = (paint_cans * paint_can_price) + (wallpaper_rolls * wallpaper_rolls_price) + (
    pair_of_gloves_needed * pair_of_gloves_price) + (paint_brush_needed * paint_brush_price)
total_price /= 15
print(f'This delivery will cost {total_price:.2f} lv.')
