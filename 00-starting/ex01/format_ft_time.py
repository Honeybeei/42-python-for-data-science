from datetime import datetime

current_time = datetime.now()
time_stamp = current_time.timestamp()

formatted_float_time = "{:,.4f}".format(time_stamp)
formatted_scientific_time = "{:.2e}".format(time_stamp)
formatted_date = current_time.strftime("%b %d %Y")

print(
    f"Seconds since January 1, 1970: {formatted_float_time} or \
         {formatted_scientific_time} in scientific notation"
)

print(formatted_date)
